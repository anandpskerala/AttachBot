#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


#configs for the bot
from config import Config

def attach(update, context):
  if update.message.reply_to_message == None:
    update.message.reply_text("Reply to a media to get an attached Media")
  else:
    m = context.bot.forward_messages("@" + Config.CHANNEL_USERNAME, update.effective_chat.id, update.reply_to_message.message_id)
    m_id = m.message.message_id
    link = "https://t.me/{}/{}".format(Config.CHANNEL_USERNAME, m_id)
    print(link)
    context.bot.send_message(update.effective_chat.id, update.message.text + "<a href='{}'>{}</a>".format(link, " "), parse_mode=ParseMode.HTML)
