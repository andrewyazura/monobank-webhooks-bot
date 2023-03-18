from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CommandHandler, ContextTypes


async def callback(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        text="`hi!`", parse_mode=ParseMode.MARKDOWN
    )


handler = CommandHandler(command="start", callback=callback)
