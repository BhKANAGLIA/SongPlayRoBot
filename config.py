import os
API_ID = int(os.getenv("9988097"))
API_HASH = os.getenv("99cdeb3acf692621af804eb15214546a")
BOT_TOKEN = os.getenv("5836336885:AAEr-ojX1zotuIpvkYeE0sUK_QZHRe3cunE")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
