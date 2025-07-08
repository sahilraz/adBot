from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from StringGen import Anony
from StringGen.utils import get_served_users

import os
import aiohttp
from pyrogram.enums import ParseMode


@Anony.on_message(filters.command(["stats", "users"]) & filters.user(OWNER_ID))
async def get_stats(_, message: Message):
    users = len(await get_served_users())
    await message.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ {Anony.name} :\n\n {users} ᴜsᴇʀs")


@Anony.on_message(filters.command("logs") & filters.private & filters.incoming)
async def log_command(_, message: Message):
    user_id = message.from_user.id
    
    if user_id != OWNER_ID:
        return await message.reply_text(
            "⌯ ꜱσʀʀʏ, σηʟʏ σᴡηєʀ ᴄᴀη ᴜꜱє ᴛʜɪꜱ ᴄσᴍᴍᴀηᴅ ⌯",
            parse_mode=ParseMode.MARKDOWN
        )
    
    try:
        # Read last 100 lines of log file
        with open("log.txt", "r", encoding="utf-8") as file:
            logs = file.readlines()[-100:]
            log_text = "".join(logs)
        
        # Upload to 0x0.st
        async with aiohttp.ClientSession() as session:
            async with session.post("https://0x0.st", data={"file": log_text}) as response:
                if response.status == 200:
                    url = await response.text()
                    await message.reply_text(
                        f"⌯ ʟσɢꜱ ᴜᴘʟσᴀᴅєᴅ ꜱᴜᴄᴄєꜱꜱғᴜʟʟʏ\n\n❣ ᴜʀʟ: {url.strip()}",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text(
                        "❣ ғᴀɪʟєᴅ ᴛσ ᴜᴘʟσᴀᴅ ʟσɢꜱ ᴛσ 0x0.st",
                        parse_mode=ParseMode.MARKDOWN
                    )
    except FileNotFoundError:
        await message.reply_text(
            "⌯ ησ ʟσɢ ғɪʟє ғσᴜηᴅ",
            parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        await message.reply_text(
            f"❣ ᴀη єʀʀσʀ σᴄᴄᴜʀʀєᴅ: {str(e)}",
            parse_mode=ParseMode.MARKDOWN
        )
