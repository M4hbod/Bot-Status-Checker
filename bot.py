import os
import pytz
import asyncio
import datetime
from pyrogram import Client, filters
from pyrogram.errors import FloodWait


app = Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_name = os.environ["SESSION_NAME"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def status_checker():
    async with app:
            while True:
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                checker_bot = f"💡 **<u>وضعیت رباتون</u>** 💡\n\n💬 **{CHANNEL_OR_GROUP_NAME}**"
                for bot in BOT_LIST:
                    try:
                        checker_status = await app.send_message(bot, "/start")
                        aaa = checker_status.message_id
                        await asyncio.sleep(10)
                        checker_user = await app.get_history(bot, limit = 1)
                        for ccc in checker_user:
                            bbb = ccc.message_id
                        if aaa == bbb:
                            checker_bot += f"\n\n🤖 **ربات**: @{bot}\n🔴 **وضعیت**: بگا ❌"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **یالله** 🚨\n\n» ربات @{bot} بگا رفته** ❌")
                                except Exception:
                                    pass
                            await app.read_history(bot)
                        else:
                            checker_bot += f"\n\n🤖 **ربات**: @{bot}\n🟢 **وضعیت**: نابگا ✅"
                            await app.read_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                checker_bot += f"\n\n🛂 آخرین چک: {last_update} ({TIME_ZONE})\n\n🟡 **هر 60 دقیقه چک خواهد جود**\n\n⚡ __قدرت گرفته از آق مخبذ__"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, checker_bot)
                print(f"آخرین چک: {last_update}")                
                await asyncio.sleep(3600)
                        
app.run(status_checker())
