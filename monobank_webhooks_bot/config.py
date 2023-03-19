from pydantic import BaseSettings


class Settings(BaseSettings):
    app_root_path: str

    telegram_bot_token: str
    telegram_header_token: str
    telegram_chat_id: int

    monobank_url: str
    monobank_timeout: int

    monobank_token: str
    monobank_path_token: str

    currencies: list[int]

    class Config:
        env_file = ".env"


settings = Settings()
