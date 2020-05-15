#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala

import os

class Config(object):
  TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
  #CHANNEL_USERNAME without '@'
  CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", "")
  #CHANNEL_ID = int(os.environ.get("CHANNEL_ID", 12345))
