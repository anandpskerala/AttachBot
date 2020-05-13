from pyrogram import Client, Filters

#Secret configs
from config import Config

@Client.on_message(Filters.command(["start"]))
async def start(bot, msg):
  await bot.send_message(msg.chat.id, f"Hi {msg.from_user.id}. I am Attach Bot. I can attach medias to your long text.", reply_to_message_id=msg.message_id)