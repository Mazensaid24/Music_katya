import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","كاتيا","السورس", "سورس مين"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/b895ea71e98d2dec07bd6.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [𝗦𝗢𝗨𝗥𝗖𝗘 𝗞𝗮𝗧𝗬𝗮](https://t.me/Source_katya)
么 [𝗔𝗦𝗞 𝗧𝗢 𝗠𝗘](https://t.me/ZzZzZl1l)
么 [νιρ ʍαzεπ](https://t.me/ZzZzZl1l)
么 [ʍαzεπ](https://t.me/ZzZzZl1l)
╰──── • ◈ • ────╯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ժᥱ᥎ Ⴆ᥆ƚ", url=f"https://t.me/Ve_G4"), 
                    
                
                    InlineKeyboardButton(
                        "‹ ᘜᖇ᥆υρ ›", url=f"https://t.me/miika3"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "‹ ᥉᥆υᖇᥴᥱ ›", url=f"https://t.me/Source_Katya"),
                
        ],

            ]

        ),

    )

