#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala


import os

import telegram

#Configs for the bot
from config import Config

from telegram.ext import Updater
from telegram.ext import CommandHandler,MessageHandler, Filters

from plugins.start import start
from plugins.tg_attach import attach


updater = Updater(token=Config.TG_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)

attach_handler = MessageHandler(Filters.text, attach)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(attach_handler)

updater.start_polling()