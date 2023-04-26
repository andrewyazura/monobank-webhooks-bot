from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from telegram import Update

from ..config import settings
from ..telegram import telegram_api


class TelegramUpdate(BaseModel):
    update_id: int

    message: dict | None = None
    edited_message: dict | None = None

    channel_post: dict | None = None
    edited_channel_post: dict | None = None

    inline_query: dict | None = None
    chosen_inline_query: dict | None = None

    callback_query: dict | None = None
    shipping_query: dict | None = None
    pre_checkout_query: dict | None = None

    poll: dict | None = None
    poll_answer: dict | None = None

    my_chat_answer: dict | None = None
    chat_member: dict | None = None
    chat_join_request: dict | None = None


router = APIRouter(prefix="/telegram", tags=["telegram"])


@router.post("/")
async def process_telegram_webhook(
    update: TelegramUpdate,
    x_telegram_bot_api_secret_token: str | None = Header(default=None),
) -> None:
    if x_telegram_bot_api_secret_token != settings.telegram_header_token:
        raise HTTPException(
            status_code=403,
            detail="X-Telegram-Bot-Api-Secret-Token is invalid",
        )

    await telegram_api.process_update(
        Update.de_json(update.dict(), telegram_api.bot)
    )
