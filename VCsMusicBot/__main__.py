import requests
from pyrogram import Client as Bot

from VCsMusicBot.config import 8b2c2204694f06a9ca85047ec4f531a8
from VCsMusicBot.config import 21434130
from VCsMusicBot.config import BG_IMAGE
from VCsMusicBot.config import 5542726899:AAHOAOHZzqXtzqScNdyEh-t7v5sAwF1J84Q
from VCsMusicBot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    21434130,
    8b2c2204694f06a9ca85047ec4f531a8,
    AAHOAOHZzqXtzqScNdyEh-t7v5sAwF1J84Q,
    plugins=dict(root="VCsMusicBot.modules"),
)

bot.start()
run()
