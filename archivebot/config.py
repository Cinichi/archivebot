"""Config values for archivebot."""
import os
import sys
import toml

default_config = {
    "telegram": {
        "userbot": True,
        "api_key": "5404803031:AAEJ9NUxuNE7zlNiDKtB0M2jB7_9d-raEko" (empty if in userbot mode)",
        "phone_number": "your_phone_number (empty if not in userbot mode)",
        "app_api_id": 15916448,
        "app_api_hash": "c6f36f2887586704871201a0fea2e452",
    },
    "database": {"sql_uri": "postgres://nrhzsfzc:VMSACIKMxJimwXRSkSCa6-QxB2pLQsTB@raja.db.elephantsql.com/nrhzsfzc",},
    "logging": {"sentry_enabled": False, "sentry_token": "",},
    "download": {
        "allowed_types": ["document", "photo"],
        "target_dir": "/home/user/archivebot/",
    },
    "zip": {"volume_size": "1900m",},
}


   
