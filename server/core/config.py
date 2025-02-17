import contextvars
import pathlib
from typing import Literal, Optional, Union, List
from uuid import uuid4

from pydantic import RedisDsn
from pydantic_settings import BaseSettings

BASE_DIR = pathlib.Path(__file__).parent.parent
PROJECT_DIR = BASE_DIR / "src"
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

CONTEXT_ID = contextvars.ContextVar("context_id", default=str(uuid4()))


class ServerConfig(BaseSettings):
    database_uri: str
    redis_url: Union[str, RedisDsn]
    update_last_scanned_block: bool = False
    ton_rpc_url: Optional[str]
    rpc_api_keys: Optional[str]


    @property
    def rpc_api_keys_list(self):

        rpc_api_keys_list: List[str] = [key.strip() for key in self.rpc_api_keys.split(",") if
                                        key.strip()]
        return rpc_api_keys_list

    class Config:
        extra = "ignore"
        env_file = ".env"
        protected_namespaces = ("model_",)


class LoggerSettings(BaseSettings):
    settings_module: Literal["DEV", "PROD"] = "DEV"
    graylog_host: Optional[str] = "localhost"
    graylog_port: Union[int, str] = 12201

    class Config:
        env_file = ".env"
        extra = "allow"
        protected_namespaces = ("model_",)


base_config = ServerConfig()
