from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from TanuMusic import app
from config import BOT_USERNAME

start_txt = """
❖ ʜᴇʏ , ᴛʜᴇʀᴇ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ  ♥︎\n\n● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ˹ ᴛᴀɴᴜ ꭙ ᴍᴜsɪᴄ™ ♡゙゙, ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏʟʟᴇᴄᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ˹ ᴛᴀɴᴜ ꭙ ᴍᴜsɪᴄ™ ♡゙"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/krishSupport"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://graph.org/file/5922a83b355489ba0853a.mp4")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://i.ibb.co/2FSqhSr/photo-2024-09-19-18-33-46-7416425646991081500.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
