from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE)

    database_url: str
    rabbitmq_url: str = "amqp://guest:guest@localhost:5672/"
    hold_minutes: int = 10
    max_seats_per_user: int = 4
    hold_isolation_level: str = "READ COMMITTED"
    db_pool_size: int = 60


@lru_cache
def get_settings() -> Settings:
    return Settings()
