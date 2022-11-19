import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("PYROGRAM V2 STRING SESSION", "
BQFHDxIAGg2H9a1W8ct4wNyul8qN0iP2WeBVcaB24K6UAfrOkk8z8-eBbzT4HHHwsBC4ed9qVsR4BISvppeF727aPQqh7FaKuNLNrMS90kn9Oe8k5H9Igb5GWIoOX-2KMdgbT1usF9bTwspkh5hRdnFuWspUi4ESwOviOBur_Qso2JaGnqz3MvN398PP2NK7WFKmNEyJDkvKwC8Z9Dq8uD933MnzUtGhSJldHwfb7EcDfdWH0dMAZzTFfmZG8JSsSveK9DChI85MYNX60gNSu8yml0IzAo-CxhCkOZP7pBjHGiJLaFu2hz9leubpJgTPicMk_nvo7SGYvrcP1H1_DMzI5lbx8wAAAAFWcdzoAA")
BOT_TOKEN = getenv("5542726899:AAHOAOHZzqXtzqScNdyEh-t7v5sAwF1J84Q")
BOT_NAME = getenv("geetha")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tgbotproject")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("21434130", "21434130"))
API_HASH = getenv("8b2c2204694f06a9ca85047ec4f531a8")
BOT_USERNAME = getenv("geethu_1398bot")
ASSISTANT_NAME = getenv("ıllı 🎀 🇰𝕚𝕟𝕘 🇴𝕗 🇧𝕦𝕕𝕕𝕚𝕖𝕤 🎀 ıllı", "VCsMusicPlayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "zauteschat")
PROJECT_NAME = getenv("King_of_Aisha", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ZauteKm/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "160"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("5745269992").split()))
