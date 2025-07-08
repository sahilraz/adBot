from pyrogram import filters
from pyrogram.types import CallbackQuery
from pyrogram.enums import ParseMode

from StringGen import Anony
from StringGen.utils import (
    gen_key,
    get_start_keyboard,
    get_features_keyboard,
    get_owner_command_keyboard,
    get_user_command_keyboard,
    is_owner
)
from config import OWNER_ID
from StringGen.modules.gen import gen_session


@Anony.on_callback_query(
    filters.regex(pattern=r"^(gensession|pyrogram|pyrogram1|telethon)$")
)
async def cb_choose(_, cq: CallbackQuery):
    await cq.answer()
    query = cq.matches[0].group(1)
    if query == "gensession":
        return await cq.message.reply_text(
            text="<b>» ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ :</b>",
            reply_markup=gen_key,
        )
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await gen_session(cq.message, cq.from_user.id)
            elif query == "pyrogram1":
                await gen_session(cq.message, cq.from_user.id, old_pyro=True)
            elif query == "telethon":
                await gen_session(cq.message, cq.from_user.id, telethon=True)
        except Exception as e:
            await cq.edit_message_text(e, disable_web_page_preview=True)


@Anony.on_callback_query(filters.regex(pattern=r"^commands$"))
async def commands_callback(_, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    
    if is_owner(user_id):
        await callback_query.edit_message_text(
            """┌────── ˹ σᴡηєʀ ᴄσᴍᴍᴀηᴅꜱ ˼ ──────⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⟡
┆◦ ғσʀᴄє ꜱᴜʙ: ᴍᴀηᴀɢє ғσʀᴄє ꜱᴜʙꜱᴄʀɪᴘᴛɪση
┆◦ ʙʀσᴀᴅᴄᴀꜱᴛ: ꜱєηᴅ ᴍєꜱꜱᴀɢє ᴛσ ᴀʟʟ ᴜꜱєʀꜱ
┆◦ ᴘʟᴀηꜱ: ᴍᴀηᴀɢє ꜱᴜʙꜱᴄʀɪᴘᴛɪση ᴘʟᴀηꜱ
┆◦ ᴜꜱєʀꜱ: ᴠɪєᴡ ʙσᴛ ᴜꜱєʀꜱ
┆◦ ᴠᴀʀꜱ: ᴍᴀηᴀɢє ʙσᴛ ᴠᴀʀɪᴀʙʟєꜱ
┆◦ ʟσɢꜱ: ᴠɪєᴡ ʙσᴛ ʟσɢꜱ
┆◦ ᴜᴘᴅᴀᴛє: ᴜᴘᴅᴀᴛє ʙσᴛ
┆◦ ʟσɢɪη: ɢєηєʀᴀᴛє ꜱєꜱꜱɪση
└─────────────────────────────•""",
            reply_markup=await get_owner_command_keyboard(),
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        await callback_query.edit_message_text(
            """┌────── ˹ ᴄσᴍᴍᴀηᴅꜱ ˼ ──────⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⟡
┆◦ ʟσɢɪη: ɢєηєʀᴀᴛє ꜱєꜱꜱɪση ꜱᴛʀɪηɢ
└─────────────────────────────•""",
            reply_markup=await get_user_command_keyboard(),
            parse_mode=ParseMode.MARKDOWN
        )


@Anony.on_callback_query(filters.regex(pattern=r"^about$"))
async def about_callback(_, callback_query: CallbackQuery):
    await callback_query.edit_message_text(
        """┌────── ˹ ᴀʙσᴜᴛ ᴍє ˼ ──────⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⟡
┆◦ ʙσᴛ ηᴀᴍє: {bot_name}
┆◦ ᴠєʀꜱɪση: 2.5.1
┆◦ ᴄʀєᴀᴛσʀ: [ᴅєᴠɪʟ ʙσʏ](tg://user?id=7530212474)
┆◦ ʟᴀηɢᴜᴀɢє: ᴘʏᴛʜση 3.11.4
┆◦ ʟɪʙʀᴀʀʏ: ᴘʏʀσɢʀᴀᴍ 2.0.106
┆◦ ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ: ᴠ2.5.1 ꜱᴛᴀʙʟє
└─────────────────────────────•

❣ ᴘσᴡєʀєᴅ ʙʏ @DholakpurOfficial""".format(
            bot_name=Anony.me.first_name
        ),
        reply_markup=await get_features_keyboard(),
        parse_mode=ParseMode.MARKDOWN
    )


@Anony.on_callback_query(filters.regex(pattern=r"^features$"))
async def features_callback(_, callback_query: CallbackQuery):
    await callback_query.edit_message_text(
        """┌────── ˹ ғєᴀᴛᴜʀєꜱ ˼ ──────⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⟡
┆◦ ꜱᴛʀɪηɢ ɢєηєʀᴀᴛɪση ᴡɪᴛʜ ᴀʟʟ ᴍєᴛʜσᴅꜱ
┆◦ ᴀᴜᴛσᴍᴀᴛɪᴄ ᴀᴅ ᴘσꜱᴛɪηɢ ɪη ɢʀσᴜᴘꜱ
┆◦ ꜱᴜʙꜱᴄʀɪᴘᴛɪση ᴄʜєᴄᴋ ꜱʏꜱᴛєᴍ
┆◦ ᴜꜱєʀ ᴅᴀꜱʜʙσᴀʀᴅ ᴡɪᴛʜ ꜱᴛᴀᴛꜱ
┆◦ ᴀᴜᴛσᴍᴀᴛɪᴄ ʙʀσᴀᴅᴄᴀꜱᴛ ᴛσ ᴜꜱєʀꜱ
┆◦ ᴀᴅᴠᴀηᴄєᴅ єʀʀσʀ ʜᴀηᴅʟɪηɢ
└─────────────────────────────•""",
        reply_markup=await get_features_keyboard(),
        parse_mode=ParseMode.MARKDOWN
    )


@Anony.on_callback_query(filters.regex(pattern=r"^back_to_start$"))
async def back_to_start_callback(_, callback_query: CallbackQuery):
    user = callback_query.from_user
    bot_mention = f"[{Anony.me.first_name}](tg://user?id={Anony.me.id})"
    
    await callback_query.edit_message_text(
        f"""┌────── ˹ ᴡєʟᴄσᴍє ˼ ──────⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⟡  
┆◦ ʜєʏ {user.first_name},  
┆◦ ɪ'ᴍ : {bot_mention} ⌯  
└─────────────────────────────•

❣ ᴀ ꜱᴛʀɪηɢ + ᴀᴅ ᴘσꜱᴛɪηɢ ʙσᴛ ғσʀ ᴛєʟєɢʀᴀᴍ.  
➻ ʟσɢɪη ᴡɪᴛʜ ᴀᴘɪ ɪᴅ, ʜᴀꜱʜ & σᴛᴘ ᴛσ ɢєηєʀᴀᴛє ꜱєꜱꜱɪση.  
➻ ᴘσꜱᴛ ᴀᴅꜱ ᴀᴜᴛσᴍᴀᴛɪᴄᴀʟʟʏ ɪη ʏσᴜʀ ɢʀσᴜᴘꜱ ⌯  
➻ ꜱᴜʙꜱᴄʀɪᴘᴛɪση ᴄʜєᴄᴋ + ᴜꜱєʀ ᴅᴀꜱʜʙσᴀʀᴅ ᴀᴄᴛɪᴠє ⌯  

•────────────────────────────•  
❣ 𝐏σᴡєʀєᴅ ʙʏ :- [ᴅєᴠɪʟ ʙσʏ](tg://user?id=7530212474) ❣  
•────────────────────────────•""",
        reply_markup=await get_start_keyboard(),
        parse_mode=ParseMode.MARKDOWN
    )


@Anony.on_callback_query(filters.regex(pattern=r"^close_message$"))
async def close_message_callback(_, callback_query: CallbackQuery):
    user_mention = f"[{callback_query.from_user.first_name}](tg://user?id={callback_query.from_user.id})"
    await callback_query.message.edit_text(
        f"ᴄʟσꜱєᴅ ʙʏ: {user_mention}",
        parse_mode=ParseMode.MARKDOWN
    )
