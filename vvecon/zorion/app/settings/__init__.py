import os
from pathlib import Path

from dotenv import load_dotenv
from split_settings.tools import include, optional

load_dotenv()

BASE_DIR = Path(os.environ.get("DJANGO_SETTINGS_BASE_PATH", ".")).resolve()

ENV_PREFIX = "DJANGO_CORE_SETTINGS_"
LOCAL_SETTINGS_PATH = os.getenv(f"{ENV_PREFIX}LOCAL_SETTINGS_PATH", "core/settings.py")

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = os.path.join(BASE_DIR, LOCAL_SETTINGS_PATH)

include("base.py", "logger.py", optional(LOCAL_SETTINGS_PATH), "env.py")
