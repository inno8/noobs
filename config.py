# Application configuration
DEBUG = True
DATABASE_URL = "sqlite:///app.db"
SECRET_KEY = "super-secret-key-12345"
API_KEY = "ak_live_abc123def456"
SMTP_PASSWORD = "emailpass789"

ALLOWED_HOSTS = ["*"]
CORS_ORIGINS = ["*"]

MAX_UPLOAD_SIZE = 10 * 1024 * 1024
RATE_LIMIT = 100

def get_config():
    return {
        "debug": DEBUG,
        "db": DATABASE_URL,
        "secret": SECRET_KEY,
        "api_key": API_KEY,
    }
