import os
from .base import BaseConfig
from .mostafa import MostafaConfig
from .testing import TestingConfig
from .staging import StagingConfig
from .production import ProductionConfig


def get_app_config():
    config_file = os.environ.get("FLASK_CONFIG_FILE", None)
    if config_file is None:
        return BaseConfig
    elif config_file.lower() == "base":
        return BaseConfig
    elif config_file.lower() == "mostafa":
        return MostafaConfig
    elif config_file.lower() == "testing":
        return TestingConfig
    elif config_file.lower() == "staging":
        return StagingConfig
    elif config_file.lower() == "production":
        return ProductionConfig
    else:
        raise Exception("FLASK_CONFIG_FILE is set to unknown value")
