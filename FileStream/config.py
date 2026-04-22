from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID", "16073849"))
    API_HASH = env.get("API_HASH", "e84dd69cd0504b8b45b2fd6a4e19068d")
    BOT_TOKEN = env.get("BOT_TOKEN", "6476554204:AAEXUHdO6GcRDaT5qd1eNnhGbZ-i7K0jWfQ")
    OWNER_ID = int(env.get('OWNER_ID', '5536032493'))

    WORKERS = int(env.get("WORKERS", "6"))

    DATABASE_URL = env.get(
        "DATABASE_URL",
        "mongodb+srv://bsadmin:bsadmin12@cluster0.anisucu.mongodb.net/?retryWrites=true&w=majority"
    )

    UPDATES_CHANNEL = env.get('UPDATES_CHANNEL', "BSHEGDE5")

    SESSION_NAME = env.get('SESSION_NAME', 'FileStream')

    FORCE_SUB_ID = env.get("FORCE_SUB_ID", "-1002088921495")  # ✅ fixed indent
    FORCE_SUB = str(env.get("FORCE_SUB", "True")).lower() == "true"

    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))

    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")

    MULTI_CLIENT = False

    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", "-1001997350110"))
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", "-1001997350110"))

    MODE = env.get("MODE", "primary")
    SECONDARY = MODE.lower() == "secondary"

    AUTH_USERS = list(set(
        int(x) for x in env.get("AUTH_USERS", "5536032493").split()
    ))


class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))

    HAS_SSL = env.get("HAS_SSL", "0").lower() in ("1", "true", "yes")
    NO_PORT = env.get("NO_PORT", "0").lower() in ("1", "true", "yes")

   FQDN = env.get("FQDN", "filestreambot.herokuapp.com")

    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "",
        FQDN,
        "" if NO_PORT else ":" + str(PORT)
    )
