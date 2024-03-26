import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["مازن","المبرمج مازن","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/f666b1224efef14f06e3f.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪𝗩𝗶𝗽 𝗠 𝗮 𝗭 𝗲 𝗡❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @Ve_G4 ❫
◉ 𝙸𝙳      : ❪ `5951674553` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@Ve_G4) my world (@Source_Katya - @C1_F5) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗩𝗶𝗽 𝗠 𝗮 𝗭 𝗲 𝗡", url=f"https://t.me/Ve_G4"), 
                 ],[
                   InlineKeyboardButton(
                        "𝗦𝗼𝗨𝗿𝗖𝗲 𝗞𝗮𝗧𝘆𝗔", url=f"https://t.me/Source_Katya"),
                ],

            ]

        ),

    )
