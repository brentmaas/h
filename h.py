from telethon import TelegramClient, events, errors
import random

with open("key", "r") as f:
    api_id = int(f.readline().rstrip())
    api_hash = f.readline().rstrip()
    bot_token = f.readline().rstrip()

client = TelegramClient("h", api_id, api_hash)

@client.on(events.NewMessage())
async def handler(event):
    if event.message.message.lower().replace("h", "").strip():
        try:
            await client.delete_messages(event.message.chat, [event.message.id])
        except errors.rpcerrorlist.MessageDeleteForbiddenError:
            pass
    elif random.randint(0, 100) == 0:
        await event.message.reply("h")

client.start(bot_token=bot_token)
client.run_until_disconnected()