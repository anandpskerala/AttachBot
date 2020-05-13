#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala

import pyrogram

from pyrogram import Client, Filters

#configs for the bot
from config import Config

@Client.on_message(Filters.text)
async def attach(bot, msg):
  if msg.reply_to_message == None:
    await msg.reply("Reply to a media to get an attached Media")
  else:
    m = await bot.forward_messages(Config.CHANNEL_USERNAME, msg.chat.id, msg.reply_to_message.message_id)
    m_id = m.message_id
    link = "https://t.me/{}/{}".format(Config.CHANNEL_USERNAME, m_id)
    await bot.send_message(msg.chat.id, msg.text + "<a href='{}'.format(link)></a>", parse_mode="html", disable_web_page_preview=False)
