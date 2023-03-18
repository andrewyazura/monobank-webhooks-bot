import json

from fastapi import APIRouter
from pydantic import BaseModel
from telegram.constants import ParseMode

from ..config import settings
from ..telegram import telegram_api


class MonobankWebhook(BaseModel):
    type: str
    data: dict


router = APIRouter(prefix="/monobank", tags=["monobank"])


@router.get("/", status_code=200)
async def confirm_monobank_webhook() -> None:
    return


@router.post("/", status_code=200)
async def process_monobank_webhook(
    webhook_data: MonobankWebhook,
) -> None:
    data = json.dumps(webhook_data.dict(), indent=2, ensure_ascii=True)

    await telegram_api.bot.send_message(
        chat_id=settings.telegram_chat_id,
        text=f"`{data}`",
        parse_mode=ParseMode.MARKDOWN,
    )
