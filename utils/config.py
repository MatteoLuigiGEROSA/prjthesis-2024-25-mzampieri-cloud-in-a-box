import os

env = os.getenv("FLASK_ENV", "development")


class Config:
    FLASK_WEBAPP_NAME = os.getenv("FLASK_WEBAPP_NAME", "flask-webapp")
    DEBUG = False

    LOGS_DIR =                         os.getenv("LOGS_DIR", "logs")
    LOG_LEVEL_ALL_MODULES_DEFAULT =    os.getenv("LOG_LEVEL_ALL_MODULES_DEFAULT", "ERROR")
    LOG_CHANNELS_ALL_MODULES_DEFAULT = os.getenv("LOG_CHANNELS_ALL_MODULES_DEFAULT", "f") # "c"->console, "f"->file, "cf"->console+file

    APP_CONTROLLER_LOGGER_LOG_LEVEL =    os.getenv("APP_CONTROLLER_LOGGER_LOG_LEVEL", "INFO")
    APP_CONTROLLER_LOGGER_LOG_CHANNELS = os.getenv("APP_CONTROLLER_LOGGER_LOG_CHANNELS", "cf") # "c"->console, "f"->file, "cf"->console+file


class DevelopmentConfig(Config):
    DEBUG = True

    RESTFUL_API_LOGGER_LOG_LEVEL =     os.getenv("RESTFUL_API_LOGGER_LOG_LEVEL", "DEBUG")
    RESTFUL_API_LOGGER_LOG_CHANNELS =  os.getenv("RESTFUL_API_LOGGER_LOG_CHANNELS_", "f") # "c"->console, "f"->file, "cf"->console+file
    VIEW_MODEL_LOGGER_LOG_LEVEL =      os.getenv("VIEW_MODEL_LOGGER_LOG_LEVEL", "DEBUG")
    VIEW_MODEL_LOGGER_LOG_CHANNELS =   os.getenv("VIEW_MODEL_LOGGER_LOG_CHANNELS", "f") # "c"->console, "f"->file, "cf"->console+file


class ProductionConfig(Config):
    DEBUG = False
    # LOG_LEVEL = "ERROR"
    # LOG_CHANNELS = os.getenv("LOG_CHANNELS", "f") # "c"->console, "f"->file, "cf"->console+file

    # JSON endpoint(s) & credentials-file based configuration:
    RESTFUL_API_LOGGER_LOG_LEVEL =     os.getenv("RESTFUL_API_LOGGER_LOG_LEVEL", "ERROR")
    RESTFUL_API_LOGGER_LOG_CHANNELS =  os.getenv("RESTFUL_API_LOGGER_LOG_CHANNELS_", "f") # "c"->console, "f"->file, "cf"->console+file
    VIEW_MODEL_LOGGER_LOG_LEVEL =      os.getenv("VIEW_MODEL_LOGGER_LOG_LEVEL", "ERROR")
    VIEW_MODEL_LOGGER_LOG_CHANNELS =   os.getenv("VIEW_MODEL_LOGGER_LOG_CHANNELS", "f") # "c"->console, "f"->file, "cf"->console+file


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig

}
