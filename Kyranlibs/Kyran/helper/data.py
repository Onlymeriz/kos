from pyrogram.types import InlineKeyboardButton, WebAppInfo
from utils.misc import prefix
class Data:

    text_help_menu = (
        f"**Command List & Help**\n**➣ Prefixes:**{prefix}"
    )
    reopen = [[InlineKeyboardButton("Re-Open", callback_data="reopen")]]
