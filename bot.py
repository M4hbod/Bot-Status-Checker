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
                checker_bot = f"💡 **<u>LIVE BOT STATUS</u>** 💡\n\n💬 **{CHANNEL_OR_GROUP_NAME}**"
                for bot in BOT_LIST:
                    try:
                        checker_status = await app.send_message(bot, "/start")
                        aaa = checker_status.message_id
                        await asyncio.sleep(10)
                        checker_user = await app.get_history(bot, limit = 1)
                        for ccc in checker_user:
                            bbb = ccc.message_id
                        if aaa == bbb:
                            checker_bot += f"\n\n🤖 **BOT**: @{bot}\n🔴 **STATUS**: down ❌"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **announcement** 🚨\n\n» @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await app.read_history(bot)
                        else:
                            checker_bot += f"\n\n🤖 **BOT**: @{bot}\n🟢 **STATUS**: alive ✅"
                            await app.read_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                checker_bot += f"\n\n🛂 Last Check: {last_update} ({TIME_ZONE})\n\n🟡 **updates every 60 min(s)**\n\n⚡ __Powered by M4 Checker AI__"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, checker_bot)
                print(f"Last Check At: {last_update}")                
                await asyncio.sleep(3600)
                        
app.run(status_checker())
