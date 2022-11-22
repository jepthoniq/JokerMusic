import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS, OWNER_NAME, CHANNEL

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("الأحد", 60 * 60 * 24 * 7),
    ("يوم", 60 * 60 * 24),
    ("الساعة", 60 * 60),
    ("الدقيقة", 60),
    ("الثانيه", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنك"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🏓 بـنـك/b> `{delta_ping * 1000:.3f} بالثانيه` \n<b>⏳ شغال</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["اعادة تشغيل"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    jepthon = await m.reply("1")
    await jepthon.edit("2")
    await jepthon.edit("3")
    await jepthon.edit("4")
    await jepthon.edit("5")
    await jepthon.edit("6")
    await jepthon.edit("7")
    await jepthon.edit("8")
    await jepthon.edit("9")
    await jepthon.edit("**تم اعادة تشغيل سورس ابن الدورة ميوزك بنجاح ✓**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["الاوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    JEPM = f"""
👋 اهلا {m.from_user.mention}!
𝘰𝘳𝘥𝘦𝘳𝘴 𝘮𝘶𝘴𝘪𝘤 [ {OWNER_NAME} ](t.me/{CHANNEL})
——————×—————
⧉ | لتشغيل صوتية في المكالمة أرسل ⇦ [ `{HNDLR}تشغيل  + اسم الاغنية` ]
⧉ | لتشغيل فيديو في المكالمة  ⇦ [ `{HNDLR}تشغيل_فيديو  + اسم الاغنية` ]
———————×———————
⧉ | لأيقاف الاغنية او الفيديو مؤقتآ  ⇦ [ `{HNDLR}استئناف` ] 
⧉ | لأعاده تشغيل الاغنية ⇦  [ `{HNDLR}ايقاف_الاستئناف` ]
⧉ | لأيقاف الاغنية  ⇦ [ `{HNDLR}ايقاف` ] 
⧉ | لتغطي الاغنية الحالية و تشغيل الاغنية التالية ⇦ [ `{HNDLR}تخطي` ]
⧉ | لتشغيل الاغنية عشوائية من قناة او مجموعة  ⇦ [ `{HNDLR}اغنيه عشوائية` ]
———————×———————
⧉ | لتحميل صوتية أرسل ⇦ [ `{HNDLR}تحميل + اسم الاغنية او الرابط` ]
⧉ | لتحميل فيديو  ⇦  [ `{HNDLR}تحميل_فيديو + اسم الاغنية او الرابط` ]
———————×———————
⧉ | لأعاده تشغيل التنصيب أرسل ⇦  [ `{HNDLR}ريستارت` ]
———————×———————
المطور 💻 : @lMl10l
القناة 🎈 : @jepthon
"""
    await m.reply(JEPM)


@Client.on_message(filters.command(["السورس"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    JEPM = f"""
<b>- مرحبا {m.from_user.mention}!

🎶 هذا هو سورس الجوكر ميوزك

🤖  اختصاص هذا البوت لتشغيل مقاطع صوتية او مقاطع الفيديو في المكالمات الصوتية

⚒️ لعرض اوامر السورس ارسل  {HNDLR}الاوامر

📚 • قناة السورس  : @jepthon</b>
"""
    await m.reply(JEPM, disable_web_page_preview=True)
