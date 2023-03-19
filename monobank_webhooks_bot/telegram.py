from telegram.ext import ApplicationBuilder

from .config import settings
from .handlers import start
from .handlers.monobank import menu, personal_data, rates

telegram_api = ApplicationBuilder().token(settings.telegram_bot_token).build()

telegram_api.add_handler(start.handler)

telegram_api.add_handler(menu.handler)
telegram_api.add_handler(rates.handler)
telegram_api.add_handler(personal_data.handler)
