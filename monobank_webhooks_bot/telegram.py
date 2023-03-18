from telegram.ext import ApplicationBuilder

from .config import settings
from .handlers import start

telegram_api = ApplicationBuilder().token(settings.telegram_bot_token).build()
telegram_api.add_handler(start.handler)
