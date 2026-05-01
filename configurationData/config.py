import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Config:

    # -------------------------
    # 🔹 Environment
    # -------------------------
    ENV = os.getenv("ENV", "qa")

    BASE_URLS = {
        "qa": "https://www.catawiki.com/en",
        "staging": "https://www.catawiki.com/en",
        "prod": "https://www.catawiki.com/en"
    }

    BASE_URL = BASE_URLS.get(ENV)

    # -------------------------
    # 🔹 Browser Config
    # -------------------------
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

    VIEWPORT = {
        "width": 1440,
        "height": 900
    }

    TIMEOUT = int(os.getenv("TIMEOUT", "10000"))

    # -------------------------
    # 🔹 Credentials (secure)
    # -------------------------
    TEST_EMAIL = os.getenv("TEST_EMAIL")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD")

    # -------------------------
    # 🔹 Parallel / CI
    # -------------------------
    WORKERS = os.getenv("WORKERS", "auto")

    # -------------------------
    # 🔹 Paths
    # -------------------------
    SCREENSHOT_PATH = "reports/screenshots/"
    TRACE_PATH = "traces/"
    VIDEO_PATH = "reports/videos/"