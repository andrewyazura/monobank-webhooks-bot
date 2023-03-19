from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import CallbackQueryHandler, ContextTypes


async def callback(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.message.edit_text(
        text="`available functions`",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("rates", callback_data="rates")],
                [
                    InlineKeyboardButton(
                        "personal data", callback_data="personal_data"
                    )
                ],
            ]
        ),
    )


handler = CallbackQueryHandler(callback=callback, pattern="^monobank_menu")
