#izzy
import asyncio
from pyrogram import Client, filters, raw
from pyrogram.types import Message
from . import *
from Ubot.helper import edit_or_reply
from Ubot.database.accesdb import *


@Ubot("limit", cmds)
async def spamban(client: Client, m: Message):
    await client.unblock_user("SpamBot")
    response = await client.send(
        raw.functions.messages.StartBot(
            bot=await client.resolve_peer("SpamBot"),
            peer=await client.resolve_peer("SpamBot"),
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    await m.edit_text("`Processing...`")
    await asyncio.sleep(1)
    spambot_msg = response.updates[1].message.id + 1
    status = await client.get_messages(chat_id="SpamBot", message_ids=spambot_msg)
    await m.edit_text(f"~ {status.text}")

add_command_help(
    "limit",
    [
        [f"limit", "Cek limit/batasan akun."],
    ],
)