#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala

import asyncio

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

#Configs for the bot
from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

async def client():
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "AttachBot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        workers=10, 
        plugins=plugins
    )
    return app
    
async def run_bot():
    bot = await client()
    await bot.start()
     
    await bot.idle()
     
    await bot.stop()
     
     
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_bot())
