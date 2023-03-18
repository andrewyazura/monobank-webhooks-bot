from pydantic import BaseSettings


class Settings(BaseSettings):
    telegram_bot_token: str
    telegram_header_token: str
    telegram_chat_id: int

    monobank_token: str

    class Config:
        env_file = ".env"


settings = Settings()
