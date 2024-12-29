import logging
from typing import Dict, List, Optional

from django.contrib.auth.models import Group, User
from django.db import transaction

from kitsune.messages.models import InboxMessage, OutboxMessage
from kitsune.messages.signals import message_sent
from kitsune.messages.tasks import email_private_message
from kitsune.users.models import Setting

logger = logging.getLogger(__name__)

def send_message(to: Dict[str, List[str]], text: Optional[str] = None, sender: Optional[User] = None) -> None:
    """Send a private message.
    :arg to: A dictionary with two keys, 'users' and 'groups',
            each containing a list of usernames or group names.
    """

    # We need a sender, a message, and someone to send it to
    if not sender or not text or not to:
        logger.warning("Missing sender, text, or recipients.")
        return

    try:
        # Resolve all unique user ids, including those in groups
        to_users = to.get("users", [])
        to_groups = to.get("groups", [])

        users = User.objects.filter(username__in=to_users)
        groups = Group.objects.filter(name__in=to_groups, profile__isnull=False)

        all_recipients_of_message = set(users.values_list("id", flat=True)) | set(
            User.objects.filter(groups__in=groups).values_list("id", flat=True)
        )

        with transaction.atomic():
            # Create the outbox message
            outbox_message = OutboxMessage.objects.create(sender=sender, message=text)
            outbox_message.to.set(users)
            outbox_message.to_group.set(groups)

            # Fetch settings for email notifications in one go
            users_to_email = set(
                Setting.objects.filter(
                    user__in=users, name="email_private_messages", value=True
                ).values_list("user__id", flat=True)
            )

            # Create inbox messages and handle emails
            inbox_messages = [
                InboxMessage(sender=sender, to_id=user_id, message=text)
                for user_id in all_recipients_of_message
            ]

            recipient_id_to_message_id = {
                msg.to_id: msg.id for msg in InboxMessage.objects.bulk_create(inbox_messages)
            }

            for user_id in users_to_email:
                if message_id := recipient_id_to_message_id.get(user_id):
                    email_private_message.delay(inbox_message_id=message_id)

        # Send a signal if needed
        message_sent.send(sender=InboxMessage, to=to, text=text, msg_sender=sender)

    except Exception as e:
        logger.error(f"Error sending message: {e}", exc_info=True)

def unread_count_for(user: User) -> int:
    """Returns the number of unread messages for the specified user."""
    return InboxMessage.objects.filter(to=user, read=False).count()
