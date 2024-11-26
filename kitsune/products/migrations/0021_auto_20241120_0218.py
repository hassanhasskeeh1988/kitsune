# Generated by Django 4.2.16 on 2024-11-20 02:18

from django.db import migrations

TIER3_TOPICS_DATA = [
    {
        "title": "Listen",
        "slug": "listen",
        "description": "Listen to your favorite podcasts and audiobooks.",
        "products": ["firefox", "mobile", "ios", "pocket"],
        "parent_slug": "text-to-speech",
    },
    {
        "title": "Edit account details",
        "slug": "edit-account-details",
        "description": "Edit your account details.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "account-management",
    },
    {
        "title": "Location",
        "slug": "location",
        "description": "Change your location.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "account-management",
    },
    {
        "title": "Sync and backup confusion",
        "slug": "sync-and-backup-confusion",
        "description": "Troubleshoot sync and backup confusion.",
        "products": ["firefox", "mobile", "ios", "mozilla-account"],
        "parent_slug": "recover-data",
    },
    {
        "title": "Sync configuration",
        "slug": "sync-configuration",
        "description": "Change your sync configuration.",
        "products": ["firefox", "mobile", "ios"],
        "parent_slug": "sync-data",
    },
    {
        "title": "Sync failure",
        "slug": "sync-failure",
        "description": "Troubleshoot sync issues.",
        "products": ["firefox", "mobile", "ios"],
        "parent_slug": "sync-data",
    },
    {
        "title": "Billing inquiry",
        "slug": "billing-inquiry",
        "description": "Inquire about your billing.",
        "products": [
            "firefox-private-network-vpn",
            "relay",
            "monitor",
            "pocket",
            "mdn-plus",
            "mozilla-account",
        ],
        "parent_slug": "manage-billing",
    },
    {
        "title": "Declined payment",
        "slug": "declined-payment",
        "description": "Troubleshoot declined payment issues.",
        "products": [
            "firefox-private-network-vpn",
            "relay",
            "monitor",
            "pocket",
            "mdn-plus",
            "mozilla-account",
        ],
        "parent_slug": "manage-billing",
    },
    {
        "title": "Sales tax",
        "slug": "sales-tax",
        "description": "Troubleshoot sales tax issues.",
        "products": [
            "firefox-private-network-vpn",
            "relay",
            "monitor",
            "pocket",
            "mdn-plus",
            "mozilla-account",
        ],
        "parent_slug": "manage-billing",
    },
    {
        "title": "Cancellation",
        "slug": "cancellation",
        "description": "Troubleshoot cancellation issues.",
        "products": [
            "firefox-private-network-vpn",
            "relay",
            "monitor",
            "pocket",
            "mdn-plus",
            "mozilla-account",
        ],
        "parent_slug": "manage-subscriptions",
    },
    {
        "title": "Upgrade/downgrade subscription",
        "slug": "upgrade-downgrade-subscription",
        "description": "Troubleshoot upgrade/downgrade subscription issues.",
        "products": [
            "firefox-private-network-vpn",
            "relay",
            "monitor",
            "pocket",
            "mdn-plus",
            "mozilla-account",
        ],
        "parent_slug": "manage-subscriptions",
    },
    {
        "title": "Customized reader",
        "slug": "customized-reader",
        "description": "Troubleshoot customized reader issues.",
        "products": [],
        "parent_slug": "article-view",
    },
    {
        "title": "PiP",
        "slug": "picture-in-picture",
        "description": "Troubleshoot picture in picture issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
        ],
        "parent_slug": "audio-and-video",
    },
    {
        "title": "Cookies",
        "slug": "cookies",
        "description": "Troubleshoot cookies issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
        ],
        "parent_slug": "history",
    },
    {
        "title": "Dashboard",
        "slug": "dashboard",
        "description": "Troubleshoot dashboard issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
        ],
        "parent_slug": "home-screen",
    },
    {
        "title": "New tab",
        "slug": "new-tab",
        "description": "Troubleshoot new tab issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
        ],
        "parent_slug": "home-screen",
    },
    {
        "title": "Images",
        "slug": "images",
        "description": "Troubleshoot images issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
        ],
        "parent_slug": "images-and-documents",
    },
    {
        "title": "PDFs",
        "slug": "pdfs",
        "description": "Troubleshoot PDFs issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
        ],
        "parent_slug": "images-and-documents",
    },
    {
        "title": "Recommendations",
        "slug": "recommendations",
        "description": "Troubleshoot recommendations issues.",
        "products": [],
        "parent_slug": "links",
    },
    {
        "title": "Download failure",
        "slug": "download-failure",
        "description": "Troubleshoot download failure issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
        ],
        "parent_slug": "downloads",
    },
    {
        "title": "Print",
        "slug": "print",
        "description": "Troubleshoot print issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
        ],
        "parent_slug": "downloads",
    },
    {
        "title": "Highlighting",
        "slug": "highlighting",
        "description": "Troubleshoot highlighting issues.",
        "products": ["pocket"],
        "parent_slug": "save-content",
    },
    {
        "title": "Missing items",
        "slug": "missing-items",
        "description": "Troubleshoot missing items issues.",
        "products": [],
        "parent_slug": "save-content",
    },
    {
        "title": "Permanent library",
        "slug": "permanent-library",
        "description": "Troubleshoot permanent library issues.",
        "products": ["pocket"],
        "parent_slug": "save-content",
    },
    {
        "title": "Reading list",
        "slug": "reading-list",
        "description": "Troubleshoot reading list issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
        ],
        "parent_slug": "save-content",
    },
    {
        "title": "Events",
        "slug": "events",
        "description": "Troubleshoot events issues.",
        "products": [
            "thunderbird",
            "thunderbird-android",
        ],
        "parent_slug": "calendar",
    },
    {
        "title": "Email forwarding",
        "slug": "email-forwarding",
        "description": "Troubleshoot email forwarding issues.",
        "products": [],
        "parent_slug": "send-and-receive-email",
    },
    {
        "title": "ESR",
        "slug": "esr",
        "description": "Troubleshoot ESR issues.",
        "products": ["firefox", "mobile", "ios"],
        "parent_slug": "install",
    },
    {
        "title": "Install failure",
        "slug": "install-failure",
        "description": "Troubleshoot install failure issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "install",
    },
    {
        "title": "Update failure",
        "slug": "update-failure",
        "description": "Troubleshoot update failure issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "update",
    },
    {
        "title": "Password autofill",
        "slug": "password-autofill",
        "description": "Troubleshoot password autofill issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "save-passwords",
    },
    {
        "title": "Password manager",
        "slug": "password-manager",
        "description": "Troubleshoot password manager issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn", "monitor"],
        "parent_slug": "save-passwords",
    },
    {
        "title": "3rd party sign in",
        "slug": "third-party-sign-in",
        "description": "Troubleshoot 3rd party sign in issues.",
        "products": ["firefox-private-network-vpn"],
        "parent_slug": "sign-in",
    },
    {
        "title": "Email verify lockout",
        "slug": "email-verify-lockout",
        "description": "Troubleshoot email verify lockout issues.",
        "products": ["firefox-private-network-vpn"],
        "parent_slug": "sign-in",
    },
    {
        "title": "Sign in failure",
        "slug": "sign-in-failure",
        "description": "Troubleshoot sign in failure issues.",
        "products": ["firefox-private-network-vpn"],
        "parent_slug": "sign-in",
    },
    {
        "title": "Can't select server",
        "slug": "cant-select-server",
        "description": "Troubleshoot can't select server issues.",
        "products": ["firefox-private-network-vpn"],
        "parent_slug": "connectivity",
    },
    {
        "title": "Connection failure",
        "slug": "connection-failure",
        "description": "Troubleshoot connection failure issues.",
        "products": ["firefox-private-network-vpn"],
        "parent_slug": "connectivity",
    },
    {
        "title": "Slow connection",
        "slug": "slow-connection",
        "description": "Troubleshoot slow connection issues.",
        "products": [],
        "parent_slug": "connectivity",
    },
    {
        "title": "Two-factor lockout",
        "slug": "two-factor-lockout",
        "description": "Troubleshoot two-factor lockout issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "two-factor-authentication",
    },
    {
        "title": "App crash",
        "slug": "app-crash",
        "description": "Troubleshoot app crash issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
            "firefox-private-network-vpn",
            "thunderbird",
            "thunderbird-android",
        ],
        "parent_slug": "crashing-and-slow-performance",
    },
    {
        "title": "App responsiveness",
        "slug": "app-responsiveness",
        "description": "Troubleshoot app responsiveness issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "crashing-and-slow-performance",
    },
    {
        "title": "Launch failure",
        "slug": "launch-failure",
        "description": "Troubleshoot launch failure issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "crashing-and-slow-performance",
    },
    {
        "title": "Loading speed",
        "slug": "loading-speed",
        "description": "Troubleshoot loading speed issues.",
        "products": ["firefox", "mobile", "ios"],
        "parent_slug": "crashing-and-slow-performance",
    },
    {
        "title": "Web certificates",
        "slug": "web-certificates",
        "description": "Troubleshoot web certificates issues.",
        "products": ["firefox", "mobile", "ios"],
        "parent_slug": "error-codes",
    },
    {
        "title": "Blocked application/service/website",
        "slug": "blocked-application-service-website",
        "description": "Troubleshoot blocked application/service/website issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "site-breakages",
    },
    {
        "title": "Security software",
        "slug": "security-software",
        "description": "Troubleshoot security software issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "site-breakages",
    },
    {
        "title": "Web compatibility",
        "slug": "web-compatibility",
        "description": "Troubleshoot web compatibility issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "site-breakages",
    },
    {
        "title": "Data brokers",
        "slug": "data-brokers",
        "description": "Troubleshoot data brokers issues.",
        "products": ["monitor"],
        "parent_slug": "data-removal",
    },
    {
        "title": "Privacy scan",
        "slug": "privacy-scan",
        "description": "Troubleshoot privacy scan issues.",
        "products": ["monitor"],
        "parent_slug": "data-removal",
    },
    {
        "title": "Email masking",
        "slug": "email-masking",
        "description": "Troubleshoot email masking issues.",
        "products": ["relay"],
        "parent_slug": "masking",
    },
    {
        "title": "Email and phone masking",
        "slug": "email-and-phone-masking",
        "description": "Troubleshoot email and phone masking issues.",
        "products": ["relay"],
        "parent_slug": "masking",
    },
    {
        "title": "Phone masking",
        "slug": "phone-masking",
        "description": "Troubleshoot phone masking issues.",
        "products": ["relay"],
        "parent_slug": "masking",
    },
    {
        "title": "Browser security",
        "slug": "browser-security",
        "description": "Troubleshoot browser security issues.",
        "products": ["firefox", "mobile", "ios"],
        "parent_slug": "security",
    },
    {
        "title": "Device permissions",
        "slug": "device-permissions",
        "description": "Troubleshoot device permissions issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn", "relay"],
        "parent_slug": "security",
    },
    {
        "title": "Cookies",
        "slug": "cookies",
        "description": "Troubleshoot cookies issues.",
        "products": ["firefox", "mobile", "ios"],
        "parent_slug": "tracking-protection",
    },
    {
        "title": "Email trackers",
        "slug": "email-trackers",
        "description": "Troubleshoot email trackers issues.",
        "products": ["firefox-private-network-vpn", "relay"],
        "parent_slug": "tracking-protection",
    },
    {
        "title": "Full text search",
        "slug": "full-text-search",
        "description": "Troubleshoot full text search issues.",
        "products": [],
        "parent_slug": "search",
    },
    {
        "title": "Search suggestions",
        "slug": "search-suggestions",
        "description": "Troubleshoot search suggestions issues.",
        "products": ["firefox", "mobile", "ios"],
        "parent_slug": "search",
    },
    {
        "title": "Mask labels",
        "slug": "mask-labels",
        "description": "Troubleshoot mask labels issues.",
        "products": [],
        "parent_slug": "tags",
    },
    {
        "title": "Suggested tags",
        "slug": "suggested-tags",
        "description": "Troubleshoot suggested tags issues.",
        "products": ["pocket"],
        "parent_slug": "tags",
    },
    {
        "title": "Extensions",
        "slug": "extensions",
        "description": "Troubleshoot extensions issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
            "firefox-private-network-vpn",
            "relay",
            "focus-firefox",
            "firefox-enterprise",
            "pocket",
            "thunderbird",
            "mozilla-account",
        ],
        "parent_slug": "add-ons-extensions-and-themes",
    },
    {
        "title": "Themes",
        "slug": "themes",
        "description": "Troubleshoot themes issues.",
        "products": [
            "firefox",
            "mobile",
            "ios",
            "relay",
            "focus-firefox",
            "firefox-enterprise",
            "pocket",
            "thunderbird",
        ],
        "parent_slug": "add-ons-extensions-and-themes",
    },
    {
        "title": "Browser appearance",
        "slug": "browser-appearance",
        "description": "Troubleshoot browser appearance issues.",
        "products": ["firefox", "mobile", "ios"],
        "parent_slug": "customization",
    },
    {
        "title": "Add device",
        "slug": "add-device",
        "description": "Troubleshoot add device issues.",
        "products": ["firefox", "mobile", "ios", "firefox-private-network-vpn"],
        "parent_slug": "import-and-export-settings",
    },
    {
        "title": "Alerts",
        "slug": "alerts",
        "description": "Troubleshoot alerts issues.",
        "products": [],
        "parent_slug": "notifications",
    },
    {
        "title": "Forwarded message notification",
        "slug": "forwarded-message-notification",
        "description": "Troubleshoot forwarded message notification issues.",
        "products": [],
        "parent_slug": "notifications",
    },
    {
        "title": "Push notifications",
        "slug": "push-notifications",
        "description": "Troubleshoot push notifications issues.",
        "products": ["firefox", "mobile", "ios"],
        "parent_slug": "notifications",
    },
]


def create_tier3_topics(apps, schema_editor):
    Topic = apps.get_model("products", "Topic")
    Product = apps.get_model("products", "Product")

    for entry in TIER3_TOPICS_DATA:
        try:
            parent = Topic.objects.get(slug=entry["parent_slug"], is_archived=False)
        except Topic.DoesNotExist:
            continue

        topic, created = Topic.objects.get_or_create(
            slug=entry["slug"],
            is_archived=False,
            defaults={
                "title": entry["title"],
                "description": entry["description"],
                "display_order": 50,
                "visible": True,
                "parent": parent,
            },
        )

        if not created:
            topic.parent = parent
            topic.save()

        for product_slug in entry["products"]:
            try:
                product = Product.objects.get(slug=product_slug)
            except Product.DoesNotExist:
                continue
            topic.products.add(product)


def backwards(apps, schema_editor): ...


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_squashed_0020_remove_sumoplaceholderpage_page_ptr_and_more"),
    ]

    operations = [
        migrations.RunPython(create_tier3_topics, backwards),
    ]
