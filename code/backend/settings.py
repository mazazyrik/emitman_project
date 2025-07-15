from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Dict, Any, List


class Settings(BaseSettings):
    database_url: str = Field(
        default="sqlite://db.sqlite3", env="DATABASE_URL")

    redis_host: str = Field(default="localhost", env="REDIS_HOST")
    redis_port: int = Field(default=6379, env="REDIS_PORT")
    redis_password: str = Field(default="", env="REDIS_PASSWORD")
    redis_db: int = Field(default=0, env="REDIS_DB")

    app_name: str = Field(default="EMITMAN RANEPA", env="APP_NAME")
    debug: bool = Field(default=False, env="DEBUG")
    host: str = Field(default="127.0.0.1", env="HOST")
    port: int = Field(default=8000, env="PORT")

    cors_origins: List[str] = Field(default=["*"], env="CORS_ORIGINS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def redis_url(self) -> str:
        if self.redis_password:
            return (f"redis://:{self.redis_password}@{self.redis_host}:"
                    f"{self.redis_port}/{self.redis_db}")
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"

    @property
    def tortoise_orm_config(self) -> Dict[str, Any]:
        return {
            "connections": {
                "default": self.database_url
            },
            "apps": {
                "db": {
                    "models": ["db", "aerich.models"],
                    "default_connection": "default",
                }
            },
            "use_tz": False,
            "timezone": "UTC"
        }

    @property
    def aerich_config(self) -> Dict[str, Any]:
        return {
            "tortoise_orm": self.tortoise_orm_config,
            "location": "./migrations",
            "src_folder": "./."
        }


settings = Settings()
