import os
import sys
import asyncio
import subprocess
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

from StringGen import Anony, LOGGER
from config import OWNER_ID, GITHUB_URL


def is_git_repo():
    """Check if the current directory is a git repository."""
    try:
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except Exception:
        return False


async def check_for_updates():
    """Check if there are any updates available."""
    try:
        # Fetch the latest changes
        subprocess.run(["git", "fetch", "origin"], check=True)
        
        # Get the number of commits behind
        result = subprocess.run(
            ["git", "rev-list", "HEAD..origin/main", "--count"],
            capture_output=True,
            text=True,
            check=True
        )
        
        commits_behind = int(result.stdout.strip())
        return commits_behind > 0
    except Exception as e:
        LOGGER.error(f"Failed to check for updates: {str(e)}")
        return False


async def update_bot():
    """Pull the latest changes and restart the bot."""
    try:
        # Pull the changes
        subprocess.run(["git", "pull", "origin", "main"], check=True)
        
        # Install any new requirements
        subprocess.run(["pip3", "install", "-r", "requirements.txt"], check=True)
        
        return True
    except Exception as e:
        LOGGER.error(f"Failed to update bot: {str(e)}")
        return False


@Anony.on_message(filters.command("update") & filters.private)
async def update_command(_, message: Message):
    user_id = message.from_user.id
    
    if user_id != OWNER_ID:
        await message.reply_text(
            "⌯ ʏσᴜ ᴀʀє ησᴛ ᴛʜє σᴡηєʀ σғ ᴛʜɪꜱ ʙσᴛ ⌯",
            parse_mode=ParseMode.MARKDOWN
        )
        return

    # Send initial message
    status_msg = await message.reply_text(
        "⌯ ᴘʟєᴀꜱє ᴡᴀɪᴛ, ᴄʜєᴄᴋɪηɢ ғσʀ ᴜᴘᴅᴀᴛєꜱ...",
        parse_mode=ParseMode.MARKDOWN
    )

    # Check if we're in a git repo
    if not is_git_repo():
        await status_msg.edit_text(
            "❌ ᴇʀʀᴏʀ: ɴᴏᴛ ᴀ ɢɪᴛ ʀᴇᴘᴏsɪᴛᴏʀʏ",
            parse_mode=ParseMode.MARKDOWN
        )
        return

    # Check for updates
    update_available = await check_for_updates()
    
    if not update_available:
        await status_msg.edit_text(
            "✅ ʙσᴛ ɪꜱ ᴀʟʀєᴀᴅʏ ᴜᴘ ᴛσ ᴅᴀᴛє!",
            parse_mode=ParseMode.MARKDOWN
        )
        return

    # Update found, edit message
    await status_msg.edit_text(
        "🔄 ᴜᴘᴅᴀᴛє ғσᴜηᴅ! ᴘʟєᴀꜱє ᴡᴀɪᴛ ᴡʜɪʟє ɪ ᴜᴘᴅᴀᴛє ᴛʜє ʙσᴛ...",
        parse_mode=ParseMode.MARKDOWN
    )

    # Perform the update
    update_success = await update_bot()
    
    if not update_success:
        await status_msg.edit_text(
            "❌ ᴜᴘᴅᴀᴛє ғᴀɪʟєᴅ! ᴘʟєᴀꜱє ᴄʜєᴄᴋ ʟσɢꜱ.",
            parse_mode=ParseMode.MARKDOWN
        )
        return

    # Update successful, restart bot
    await status_msg.edit_text(
        "✅ ʙσᴛ ᴜᴘᴅᴀᴛєᴅ ꜱᴜᴄᴄєꜱꜱғᴜʟʟʏ! ʀєꜱᴛᴀʀᴛɪηɢ...",
        parse_mode=ParseMode.MARKDOWN
    )
    
    # Wait a moment for the message to be sent
    await asyncio.sleep(2)
    
    # Restart the bot
    os.execl(sys.executable, sys.executable, "-m", "StringGen") 