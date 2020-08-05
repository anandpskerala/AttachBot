#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala


#Secret configs
from config import Config


def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi [{update.message.from_user.first_name}](tg://user?id={update.message.from_user.id}) I am Attach Bot. I can attach medias to your long text.", parse_mode="Markdown")
