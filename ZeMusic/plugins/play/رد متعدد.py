import asyncio
from ZeMusic import app 
from strings.filters import command
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


italy = ["نعم يا قلب البوت ؟!", "يسطا ابوس ايدك ناديني بي اسمي", "بسلك رقم وجيلك🤤", "عايز اي ياعم", "انت متعرفنيش بجد اخص علي الصحب؟!"]

@app.on_message(filters.text & filters.regex(r"(^|\W)بوت(\W|$)"))
async def Italymusic(client, message):
    if "بوت" in message.text:
        response = random.choice(italy)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس", url="https://t.me/Source_Katya")]])
        await message.reply(response, reply_markup=keyboard)

