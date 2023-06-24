# Created By @TM411
# Copyright By watan

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCMWFxWEGNKR7YuJjLjgDs3F5J6LCN7Zs6YfwQSWEFM9NbMdCn_iJMF8AcVfarK-A_aPF1TZSoBXX86F_dV5rbOzZ3iyD92WOw6dvUb5MEi9MQJDcrvEk1qo3oHE1-ECDXtoQ4AAwvVmqkjXSjAGLzI91CcqA0YUnqD89POm7A0-dAuDG4cjtd75Ub7vlFG60OCAXiCAeqqcz1IrW85bdX7-XPtXfOOtLEihH4_At6sqWtAfswDyNbzYlxLwXtPxyIkxiDpCSgi6tzaWs9ub9uk8MVKeRRg6Avg4IvggRjkiG8qejSBjFIv8QCzVnJRcXgivjkZf_HHdgzn9PQyMhUGAAAAAWAPW_kA")
BOT_TOKEN = getenv("BOT_TOKEN", "6168722005:AAGWS70T-Ok6cuI3OTr6GNxhHCK-OZIjods")
BOT_NAME = getenv("BOT_NAME", "bot")
BOT_USERNAME = getenv("BOT_USERNAME", "Saiadjabot")
ASSID = int(getenv("ASSID", "6174915391"))
ASSNAME = getenv("ASSNAME", "Kasijekg")
ASSUSERNAME = getenv("ASSUSERNAME", "Kasijekg")

BOT_ID = int(getenv("BOT_ID", "6168722005"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/LG")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
API_ID = int(getenv("API_ID", "28746916"))
API_HASH = getenv("API_HASH", "5f4eb51a1208fa6631fb8a5f3e225f17")
OWNER_ID = int(getenv("OWNER_ID", "6174915391"))
UPDATE = getenv("UPDATE", "TM_412")
SUPPORT = getenv("SUPPORT", "TM_412")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", ". / ! + - @ # $").split())
BG_IMG = getenv("BG_IMG", "https://graph.org/file/ce27991ed1e6ace351956.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6174915391").split()))
START_PIC = getenv("START_PIC", "https://graph.org/file/38cacf9b084eea3e1d600.mp4")
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
IMG_1 = getenv("IMG_1", "https://graph.org/file/475127193de2444183fd4.jpg")
IMG_2 = getenv("IMG_2", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
IMG_3 = getenv("IMG_3", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
IMG_4 = getenv("IMG_4", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
