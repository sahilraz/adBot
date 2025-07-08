from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT, OWNER_ID
from StringGen import Anony


async def get_start_keyboard():
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text="⌯ ᴀᴅᴅ ᴍє ᴛσ ʏσᴜʀ ɢʀσᴜᴘ ⌯",
                url=f"https://t.me/{(await Anony.get_me()).username}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(text="⊚ σᴡηєʀ ⊚", url=f"tg://user?id={OWNER_ID}"),
            InlineKeyboardButton(text="❣ ꜱᴜᴘᴘσʀᴛ ❣", url=SUPPORT_CHAT)
        ],
        [
            InlineKeyboardButton(text="↬ ᴀʙσᴜᴛ ᴍє ↬", callback_data="about"),
            InlineKeyboardButton(text="☞ ʜєʟᴩ ☜", callback_data="features")
        ],
        [
            InlineKeyboardButton(text="⌜ᴄσᴍᴍᴀηᴅꜱ ⌟", callback_data="commands")
        ]
    ])
    return keyboard


gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="⌯ ᴘʏʀσɢʀᴀᴍ ᴠ1 ⌯", callback_data="pyrogram1"),
            InlineKeyboardButton(text="⌯ ᴘʏʀσɢʀᴀᴍ ᴠ2 ⌯", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="⌯ ᴛєʟєᴛʜση ⌯", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="➻ ᴛʀʏ ᴀɢᴀɪη ➻", callback_data="gensession")]]
)

async def get_features_keyboard():
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="⌯ ʙᴀᴄᴋ", callback_data="back_to_start"),
            InlineKeyboardButton(text="❣ ᴄʟσꜱє", callback_data="close_message")
        ]
    ])
    return keyboard

async def get_owner_command_keyboard():
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="⌯ ғσʀᴄє ꜱᴜʙ", callback_data="force_sub"),
            InlineKeyboardButton(text="❣ ʙʀσᴀᴅᴄᴀꜱᴛ", callback_data="broadcast")
        ],
        [
            InlineKeyboardButton(text="➻ ᴘʟᴀηꜱ", callback_data="plans"),
            InlineKeyboardButton(text="⊚ ᴜꜱєʀꜱ", callback_data="users")
        ],
        [
            InlineKeyboardButton(text="❣ ᴠᴀʀꜱ", callback_data="vars"),
            InlineKeyboardButton(text="⌯ ʟσɢꜱ", callback_data="logs")
        ],
        [
            InlineKeyboardButton(text="➻ ᴜᴘᴅᴀᴛє", callback_data="update"),
            InlineKeyboardButton(text="❣ ʟσɢɪη", callback_data="login")
        ],
        [
            InlineKeyboardButton(text="⌯ ʙᴀᴄᴋ", callback_data="back_to_start"),
            InlineKeyboardButton(text="❣ ᴄʟσꜱє", callback_data="close_message")
        ]
    ])
    return keyboard

async def get_user_command_keyboard():
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="❣ ʟσɢɪη", callback_data="login")
        ],
        [
            InlineKeyboardButton(text="⌯ ʙᴀᴄᴋ", callback_data="back_to_start"),
            InlineKeyboardButton(text="❣ ᴄʟσꜱє", callback_data="close_message")
        ]
    ])
    return keyboard
