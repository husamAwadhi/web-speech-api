import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = False
    TESTING = False
    ORIGINS = "*"


class ProdConfig(Config):
    ORIGINS = ["https://domain", "https://www.domain.com"]


class DevConfig(Config):
    DEBUG = True
    ORIGINS = "http://localhost:8000"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
