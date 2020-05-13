#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala

import os

class Config(object):
  TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
  APP_ID = int(os.environ.get("API_ID", 12345))
  API_HASH = os.environ.get("API_HASH")
  DOWNLOAD_LOCATION = "./DOWNLOADS"
