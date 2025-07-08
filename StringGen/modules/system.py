import os
import sys
import httpx
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

from StringGen import Anony, LOGGER
from config import OWNER_ID


async def post_log_to_batbin(file_path: str, max_lines: int = 100) -> str:
    try:
        # Read the last `max_lines` lines from the log file
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            recent_log = "".join(lines[-max_lines:])

        # Post to Batbin
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://batbin.me/api/v2/paste",
                headers=headers,
                json={
                    "content": recent_log,
                    "title": "Bot Logs"
                }
            )

        if response.status_code == 201:
            data = response.json()
            return f"https://batbin.me/{data['id']}"
        else:
            LOGGER.error(f"Batbin API error: {response.status_code} - {response.text}")
            return f"⚠️ ʙᴀᴛʙɪɴ ᴜᴘʟᴏᴀᴅ ғᴀɪʟᴇᴅ. sᴛᴀᴛᴜs: {response.status_code}"

    except Exception as e:
        LOGGER.error(f"Log upload error: {str(e)}")
        return f"❌ ᴇʀʀᴏʀ ʀᴇᴀᴅɪɴɢ ᴏʀ ᴜᴘʟᴏᴀᴅɪɴɢ ʟᴏɢ: {str(e)}"


@Anony.on_message(filters.command("log") & filters.private & filters.incoming)
async def send_log(_, message: Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "» sᴏʀʀʏ, ᴏɴʟʏ ᴍʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.",
            parse_mode=ParseMode.MARKDOWN
        )

    try:
        # Send "uploading" message
        status_msg = await message.reply_text(
            "» ᴜᴘʟᴏᴀᴅɪɴɢ ʟᴏɢs ᴛᴏ ʙᴀᴛʙɪɴ...",
            parse_mode=ParseMode.MARKDOWN
        )

        # Upload to Batbin
        log_url = await post_log_to_batbin("log.txt", max_lines=100)
        
        # Update message with the result
        await status_msg.edit_text(
            f"» ʟᴏɢs ʜᴀᴠᴇ ʙᴇᴇɴ ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ ʙᴀᴛʙɪɴ.\n\n» ᴜʀʟ: {log_url}",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
    except Exception as e:
        await status_msg.edit_text(
            f"» ғᴀɪʟᴇᴅ ᴛᴏ ᴜᴘʟᴏᴀᴅ ʟᴏɢs: {str(e)}",
            parse_mode=ParseMode.MARKDOWN
        )


@Anony.on_message(filters.command("restart") & filters.private & filters.incoming)
async def restart_bot(_, message: Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "» sᴏʀʀʏ, ᴏɴʟʏ ᴍʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ."
        )

    msg = await message.reply_text("» ʙᴏᴛ ɪs ʀᴇsᴛᴀʀᴛɪɴɢ, ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    
    # Store the chat_id and message_id in a file for deletion after restart
    with open("restart.txt", "w") as f:
        f.write(f"{msg.chat.id}\n{msg.id}")
    
    # Restart the bot
    os.execl(sys.executable, sys.executable, "-m", "StringGen") 