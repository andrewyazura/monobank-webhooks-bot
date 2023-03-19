import json
from urllib.parse import urljoin

import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ChatAction, ParseMode
from telegram.ext import CallbackQueryHandler, ContextTypes

from ...config import settings


async def callback(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.message.reply_chat_action(
        action=ChatAction.TYPING
    )

    response = requests.get(
        url=urljoin(settings.monobank_url, "/personal/client-info"),
        timeout=settings.monobank_timeout,
        headers={"X-Token": settings.monobank_token},
    )

    data = json.dumps(response.json(), indent=2, ensure_ascii=False)

    await update.callback_query.message.edit_text(
        text=f"`{data}`",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("back", callback_data="monobank_menu")]]
        ),
    )


handler = CallbackQueryHandler(callback=callback, pattern="^personal_data")
