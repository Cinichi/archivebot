"""Config values for archivebot."""
from telegram.ext import Filters


class Config:
    """Config class for convenient configuration."""

    # Get your telegram api-key from @botfather
    TELEGRAM_API_KEY = None
    SQL_URI = 'sqlite:///archivebot.db'
    TARGET_DIR = '/home/bot/archivebot/'
    SENTRY_KEY = None
    # Allow videos and documents. Allow more file types with e.g. (.. | Filters.image)
    MESSAGE_FILTER = (Filters.document | Filters.video)


config = Config()