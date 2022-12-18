import logging
import os
import sys
import time
import spamwatch
from aiohttp import ClientSession
from Python_ARQ import ARQ
import telegram.ext as tg
from pyrogram import Client, errors, __version__ as pyrover
from telethon import TelegramClient
from aiohttp import web


routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Join Telegram Channal https://t.me/R_Mvzz_Group")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

pyrogram_version = pyrover

StartTime = time.time()

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, 8080).start()
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN = os.environ.get('TOKEN', None)

    try:
        OWNER_ID = int(os.environ.get('OWNER_ID', None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid BigInteger.")

    JOIN_LOGGER = os.environ.get('JOIN_LOGGER', None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception(
            "Your sudo or dev users list does not contain valid BigInteger.")

    try:
        DEMONS = set(int(x) for x in os.environ.get("DEMONS", "").split())
    except ValueError:
        raise Exception(
            "Your support users list does not contain valid BigInteger.")

    try:
        WOLVES = set(int(x) for x in os.environ.get("WOLVES", "").split())
    except ValueError:
        raise Exception(
            "Your whitelisted users list does not contain valid BigInteger.")

    try:
        TIGERS = set(int(x) for x in os.environ.get("TIGERS", "").split())
    except ValueError:
        raise Exception(
            "Your tiger users list does not contain valid BigInteger.")

    API_ID = os.environ.get('API_ID', None)
    API_HASH = os.environ.get('API_HASH', None)  
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    URL = os.environ.get('URL', "")  # Does not contain token
    REPOSITORY = os.environ.get("REPOSITORY", "")
    CERT_PATH = os.environ.get("CERT_PATH")
    INFOPIC = bool(os.environ.get('INFOPIC', True))
    EVENT_LOGS = os.environ.get('EVENT_LOGS', None)
    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    PORT = int(os.environ.get('PORT', 5000))
    DB_URI = 'postgres://uzrnuwgb:yBfwB0dYp88IZZ-5soWjXquQZOCydKT8@lucky.db.elephantsql.com/uzrnuwgb'
    DONATION_LINK = os.environ.get('DONATION_LINK')
    LOAD = os.environ.get("LOAD", "").split()
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', True))
    STRICT_GBAN = bool(os.environ.get('STRICT_GBAN', True))
    STRICT_GMUTE = bool(os.environ.get('STRICT_GMUTE', True))
    WORKERS = int(os.environ.get('WORKERS', 8))
    ALLOW_EXCL = os.environ.get('ALLOW_EXCL', True)
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", "") # From:- https://openweathermap.org/api
    SUPPORT_CHAT = os.environ.get('SUPPORT_CHAT', None)
    UPDATES_CHANNEL = os.environ.get('UPDATES_CHANNEL', None)
    SPAMWATCH_SUPPORT_CHAT = os.environ.get('SPAMWATCH_SUPPORT_CHAT', None)
    SPAMWATCH_API = os.environ.get('SPAMWATCH_API', None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None) # From:- https://www.remove.bg/
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "VegetRobot")
    LOG_GROUP_ID = os.environ.get('LOG_GROUP_ID', None)

    try:
        BL_CHATS = set(int(x) for x in os.environ.get('BL_CHATS', "").split())
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid BigInteger.")

else:
    from Millie.config import Development as Config
    TOKEN = "5967978022:AAEEL2RdFaXyoqVKw9WPh8yIz_pXPhV-JHs" 

    try:
        OWNER_ID = int(1927155351)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid BigInteger.")

    JOIN_LOGGER = -1001547941154
    OWNER_USERNAME = "renish_rgi"

    try:
        DRAGONS = set(int(x) for x in Config.DRAGONS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception(
            "Your sudo or dev users list does not contain valid BigInteger.")

    try:
        DEMONS = set(int(x) for x in Config.DEMONS or [])
    except ValueError:
        raise Exception(
            "Your support users list does not contain valid BigInteger.")

    try:
        WOLVES = set(int(x) for x in Config.WOLVES or [])
    except ValueError:
        raise Exception(
            "Your whitelisted users list does not contain valid BigInteger.")

    try:
        TIGERS = set(int(x) for x in Config.TIGERS or [])
    except ValueError:
        raise Exception(
            "Your tiger users list does not contain valid BigInteger.")


    EVENT_LOGS = -1001547941154
    WEBHOOK = None 
    URL = None
    PORT = 5000
    CERT_PATH = Config.CERT_PATH
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    JOIN_LOGGER = -1001547941154
    DEL_CMDS = True
    WORKERS = 8
    BAN_STICKER = "CAACAgQAAx0CU_rCTAABAczQXyBOv1TsVK4EfwnkCUT1H0GCkPQAAtwAAwEgTQaYsMtAltpEwhoE"
    ALLOW_EXCL = True 
    SUPPORT_CHAT = "r_from_rgi_support"
    REM_BG_API_KEY = Config.REM_BG_API_KEY
    UPDATES_CHANNEL = "millie_robot_update"
    SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = 'VWFUxtmR2dFHLpAGLAhh630bHcODm3E35d5bqUHUfpsQqqOc8iFknZUXMgS5Te2g'

    try:
        BL_CHATS = set(int(x) for x in Config.BL_CHATS or [])
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid BigInteger.")

DRAGONS.add(1927155351)
DEV_USERS.add(1927155351) #it you going to remove me don't ask me errors👿

if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key missing! recheck your config.")
else:
    sw = spamwatch.Client(SPAMWATCH_API)
   

from Millie.config import ARQ_API_KEY, ARQ_API_URL

API_ID = 18706633
API_HASH = '1d7c16e89a28c5e332d457e5e1027d0c'
TOKEN = '5967978022:AAEEL2RdFaXyoqVKw9WPh8yIz_pXPhV-JHs'

aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

telethn = TelegramClient("Vegeta", API_ID, API_HASH)
pgram = Client("Millie", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = pgram.dispatcher

DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(['1927155351 5570402782 1733484689 1061059757'])
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from Millie.modules.helper_funcs.handlers import (CustomCommandHandler,
                                                        CustomMessageHandler,
                                                        CustomRegexHandler)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler

print("Starting Pyrogram Client")
pgram.start()

print("Aquiring BOT Client Info")
telethn.start(bot_token=TOKEN)

bottie = pgram.get_me()

BOT_ID = bottie.id
BOT_USERNAME = bottie.username
BOT_NAME = bottie.first_name
BOT_MENTION = bottie.mention

app = Bot()
app.run()
