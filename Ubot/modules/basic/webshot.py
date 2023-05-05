# COPYRIGHT https://github.com/TeamKillerX/DarkWeb
# CREATE CODING BY https://t.me/xtsea

import asyncio
from pyrogram.types import *
from pyrogram import *

from . import *
from Ubot.helper import edit_or_reply

@Ubot(["webshot", "ss"], cmds)
async def webshot(client: Client, message: Message):
    ren = await edit_or_reply(message, "`Processing...`")
    try:
        user_link = message.command[1]
        try:
            full_link = f"https://webshot.deam.io/{user_link}/?width=1920&height=1080?delay=2000?type=png"
            await client.send_photo(
                message.chat.id,
                full_link,
                caption=f"**Tangkapan layar halaman** {user_link}",
            )
        except Exception as dontload:
            await message.edit(f"Error! {dontload}\nMencoba lagi membuat tangkapan layar...")
            full_link = f"https://mini.s-shot.ru/1920x1080/JPEG/1024/Z100/?{user_link}"
            await client.send_photo(
                message.chat.id,
                full_link,
                caption=f"**Tangkapan layar halaman** {user_link}",
            )
        await ren.delete()
    except Exception as error:
        await ren.delete()
        await client.send_message(
            message.chat.id, f"**Ada yang salah\nLog:{error}...**"
        )

add_command_help(
    "webshot",
    [
        [f"ss <link>", "Untuk screenshot halaman web yang diberikan",],
    ],
)
