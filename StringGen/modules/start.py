from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import ChatWriteForbidden, ChannelPrivate, UserNotParticipant
from pyrogram.enums import ParseMode

from StringGen import Anony, LOGGER
from StringGen.utils import add_served_user, get_start_keyboard
from config import LOGGER_GROUP_ID, OWNER_ID, START_IMAGE


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    user = message.from_user
    user_mention = f"[{user.first_name}](tg://user?id={user.id})"
    username = user.username or user.first_name
    bot_mention = f"[{Anony.me.first_name}](tg://user?id={Anony.me.id})"
    
    # Send log to the logger group
    try:
        log_text = f"{user_mention} ʜᴀs sᴛᴀʀᴛᴇᴅ ʙᴏᴛ.\n\n"
        log_text += f"ᴜsᴇʀ ɪᴅ : {user.id}\n"
        log_text += f"ᴜsᴇʀ ɴᴀᴍᴇ: {username}"
        
        await Anony.get_chat_member(LOGGER_GROUP_ID, Anony.id)  # Check if bot is in the group
        await Anony.send_message(
            chat_id=LOGGER_GROUP_ID,
            text=log_text,
            parse_mode=ParseMode.MARKDOWN
        )
    except (ChatWriteForbidden, ChannelPrivate, UserNotParticipant) as e:
        LOGGER.error(f"Failed to send log message: Bot is not in the logger group or doesn't have proper permissions. Error: {str(e)}")
    except Exception as e:
        LOGGER.error(f"Failed to send log message: {str(e)}")
    
    await message.reply_photo(
        photo=START_IMAGE,
        caption=f"""
┌────── ˹ ᴡєʟᴄσᴍє ˼ ──────⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⟡  
┆◦ ʜєʏ {message.from_user.first_name},  
┆◦ ɪ'ᴍ : {bot_mention} ⌯  
└─────────────────────────────•

❣ ᴀ ꜱᴛʀɪηɢ + ᴀᴅ ᴘσꜱᴛɪηɢ ʙσᴛ ғσʀ ᴛєʟєɢʀᴀᴍ.  
➻ ʟσɢɪη ᴡɪᴛʜ ᴀᴘɪ ɪᴅ, ʜᴀꜱʜ & σᴛᴘ ᴛσ ɢєηєʀᴀᴛє ꜱєꜱꜱɪση.  
➻ ᴘσꜱᴛ ᴀᴅꜱ ᴀᴜᴛσᴍᴀᴛɪᴄᴀʟʟʏ ɪη ʏσᴜʀ ɢʀσᴜᴘꜱ ⌯  
➻ ꜱᴜʙꜱᴄʀɪᴘᴛɪση ᴄʜєᴄᴋ + ᴜꜱєʀ ᴅᴀꜱʜʙσᴀʀᴅ ᴀᴄᴛɪᴠє ⌯  

•────────────────────────────•  
❣ 𝐏σᴡєʀєᴅ ʙʏ :- [ᴅєᴠɪʟ ʙσʏ](tg://user?id={OWNER_ID}) ❣  
•────────────────────────────•
""",
        reply_markup=await get_start_keyboard(),
        parse_mode=ParseMode.MARKDOWN
    )
    await add_served_user(message.from_user.id)
