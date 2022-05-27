## Status Checker Userbot
check your bot status automatically using userbot, simply and easy.

## Mandatory Vars
1. `API_ID` : Telegram API_ID, get it from my.telegram.org/apps
2. `API_HASH` : Telegram API_ID, get it from my.telegram.org/apps
3. `SESSION_STRING` : A pyrogram session string
4. `BOT_LIST` : Your bot username list without "@" (Example: MakhusicBot OceanThiefBot)
5. `CHANNEL_OR_GROUP_ID` : Your channel's or group's Telegram id (Example: -1001246808642)
6. `MESSAGE_ID` : Telegram id of message from your channel or group (Example: 10)
7. `BOT_ADMIN_IDS` : Bot admin id (Example: 123456 127890) ~ optional
8. `TIME_ZONE`: Your time zone (Example: Asia/Kolkata)
9. `CHECK_DELAY`: Delay between each check in seconds (Example: 3600)

## Installation

### The Easy Way

##### Tap the Deploy To Heroku button below to deploy straight to Heroku!

[![Deploy](https://heroku.com/deploy?template=https://github.com/M4hbod/Bot-Status-Checker/tree/pyrogram-version-1)

### The Hard Way

```sh
git clone --single-branch --branch pyrogram-version-1 https://github.com/M4hbod/Bot-Status-Checker/
cd Bot-Status-Checker
pip install -r requirements.txt
cp example.env .env
--- EDIT .env values appropriately ---
python bot.py
```

### Credits
- [levina](https://github.com/levina-lab) for his [status-checker](https://github.com/levina-lab/status-checker)
