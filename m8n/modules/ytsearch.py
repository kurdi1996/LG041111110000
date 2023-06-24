import logging

from search_engine_parser import GoogleSearch
from youtube_search import YoutubeSearch

import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message

from m8n import app
from m8n.utils.filters import command


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)


@app.on_message(command(["لينك", "ستران", "link"]))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("‹ نافي بنفيسه يان لينكي فريكه ›")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("‹ جافه ري به لێت ڪه ريت ›")
        results = YoutubeSearch(query, max_results=7).to_dict()
        text = ""
        for i in range(4):
            text += f" **‹ ناف ›** - [{results[i]['title']}](https://youtube.com{results[i]['url_suffix']})\n"
            text += f" **‹ وه صف ›** - {results[i]['duration']}\n"
            text += f" **‹ ژمارا مشاهدا ›** - {results[i]['views']}\n"
            text += f" **‹ كه نالي يوتيوب  ›** - {results[i]['channel']}\n\n"
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
