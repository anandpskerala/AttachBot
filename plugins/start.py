#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala

#Logger
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#Secret configs
from config import Config

from telegram import ParseMode

def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi <a href='tg://user?id={update.message.from_user.id}'>{update.message.from_user.first_name}</a>. I am Attach Bot. I can attach medias to your long text.", parse_mode=ParseMode.HTML)
