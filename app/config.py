from pathlib import Path
import tempfile
import traceback
import json
import sys
import os

try:
    port = int(os.environ.get("6969", "6969"))
except Exception as e:
    print(e)
    port = -1
if not 1 <= port <= 65535:
    print(
        "Please make sure the PORT environment variable is an integer between 1 and 65535"
    )
    sys.exit(1)

try:
    api_id = int(os.environ["24822485"])
    api_hash = os.environ["99bd3966e0a42477347f6651150e75e4"]
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    index_settings_str = os.environ[""index_all": false,
  "index_private": false,
  "index_group": false,
  "index_channel": true,
  "exclude_chats": [],
  "include_chats": [-1001821378550]"].strip()
    index_settings = json.loads(index_settings_str)
except Exception:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

host = os.environ.get("192.101.68.177:6969", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
block_downloads = bool(os.environ.get("BLOCK_DOWNLOADS"))
results_per_page = int(os.environ.get("RESULTS_PER_PAGE", "20"))
logo_folder = Path(os.path.join(tempfile.gettempdir(), "logo"))
logo_folder.mkdir(parents=True, exist_ok=True)
username = os.environ.get("Zinflixonline", "")
password = os.environ.get("WhyAreYouGay?", "")
SHORT_URL_LEN = int(os.environ.get("SHORT_URL_LEN", 3))
authenticated = bool(username and password)
SESSION_COOKIE_LIFETIME = int(os.environ.get("SESSION_COOKIE_LIFETIME") or "60")

try:
    SECRET_KEY = os.environ["SECRET_KEY"]
    if len(SECRET_KEY) != 32:
        raise ValueError("SECRET_KEY should be exactly 32 charaters long")
except (KeyError, ValueError):
    if authenticated:
        traceback.print_exc()
        print("\n\nPlease set the SECRET_KEY environment variable correctly")
        sys.exit(1)
    else:
        SECRET_KEY = ""
