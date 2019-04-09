import os

from typing import List, Tuple

BASE_DIR: str = os.path.dirname(os.path.realpath(__file__))

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'filename': os.path.join(BASE_DIR, '..', 'debug.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 3,
            'formatter': 'default',
        },
    },
    'loggers': {
        '__main__': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
    },
}


TOKEN: str = os.environ.get("DISCORD_TOKEN", "")
DEV_IDS: Tuple[int] = (int(os.environ.get("DISCORD_DEV_ID", 0)),)
ERROR_CHANNEL_ID: Tuple[int] = (int(os.environ.get("DISCORD_ERROR_CHANNEL", 0)),)

COGS: List[str] = [
    'cogs.devtools',
    'cogs.global_listeners',
    'cogs.loading',
]
