import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from NekoRobot import tbot as bot
from NekoRobot import tbot as tgbot
from NekoRobot.events import register

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://te.legra.ph/file/ca84134db5b8a2a260555.mp4"
file2 = "https://te.legra.ph/file/457db382cef870dfa162e.mp4"
file3 = "https://te.legra.ph/file/d8d6c72ca47699d793f80.jpg"
file4 = "https://te.legra.ph/file/07e9c1367dcb8a299c98c.jpg"
file5 = "https://te.legra.ph/file/d8d6c72ca47699d793f80.jpg"
""" =======================CONSTANTS====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    betsy = event.sender.first_name
    button = [[custom.Button.inline("Click Here", data="information")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"♡ Hey {betsy}, I'm Neko\n♡ I'm Created By [Prince](tg://user?id=1732814103)\n♡ Click The Button Below To Get Your Info",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        NEKO = "YOUR DETAILS BY ITACHI UCHIHA\n\n"
        NEKO += f"FIRST NAME : {PRO.first_name} \n"
        NEKO += f"LAST NAME : {PRO.last_name}\n"
        NEKO += f"YOU BOT : {PRO.bot} \n"
        NEKO += f"RESTRICTED : {PRO.restricted} \n"
        NEKO += f"USER ID : {boy}\n"
        NEKO += f"USERNAME : {PRO.username}\n"
        await event.answer(NEKO, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__help__ = """
/myinfo: shows your info in inline button
"""

__mod_name__ = "myinfo"
__command_list__ = ["myinfo"]
