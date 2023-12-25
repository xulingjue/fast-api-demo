from decouple import config

# 读取配置
DEBUG = config("DEBUG", default=False, cast=bool)
DATABASE_URL = config("DATABASE_URL", default="sqlite:///./test.db")
SECRET_KEY = config("SECRET_KEY", default="mysecretkey")
LOGGING_FILE = config("LOGING_FILE", default="log/access.log")

# 日志配置
LOGGING_CONF = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
    'handlers': {
        'terminal': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default',
            'filename': LOGGING_FILE,
            'when': 'H',
            'interval': 1,
            'backupCount': 50,
            'encoding': 'utf8'
        }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['file', 'terminal']
    }
}

# 使用配置
if DEBUG:
    print("Debug mode is enabled.")
