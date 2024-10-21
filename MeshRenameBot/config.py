from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://j32025026:<diTBNy6AvTzCpOYi>@cluster0.mmcgi.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "ba25181c01b50d945748801b6c8b6ecc"]
        API_ID = [int, 26162072]
        BOT_TOKEN = [str, "7858858787:AAH0LqQiKhYXtGer-ak9N-X1gB6Y5NlUiuc"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[123456789]]
        OWNER_ID = [int, 7538143921]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,""]
        FORCEJOIN_ID = [int,-1002215819339]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
