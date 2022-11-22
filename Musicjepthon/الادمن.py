from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, call_py
from Musicjepthon.helpers.decorators import authorized_users_only
from Musicjepthon.helpers.handlers import skip_current_song, skip_item
from Musicjepthon.helpers.queues import QUEUE, clear_queue


@Client.on_message(filters.command(["تخطي"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**- لا يوجد شيء في قائمة الانتظار لتخطيه**")
        elif op == 1:
            await m.reply("**")
        else:
            await m.reply(
                f"**⏭ تخطي التشغيل** \n**🎧 المشغل الحالي ** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ تمت إزالة الأغاني التالية من قائمة الانتظار : **"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(filters.command(["انهاء", "توقف"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**✅ تم إنهاء التشغيل بنجاح **")
        except Exception as e:
            await m.reply(f"**هناك خطأ ** \n`{e}`")
    else:
        await m.reply("**❌ لايوجد هناك اغنيه شغاله !**")


@Client.on_message(filters.command(["ايقاف"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**⏸ تم ايقاف التشغيل مؤقتًا.**\n\n•لاستئناف التشغيل ، استخدم الأمر  » {HNDLR}استئناف"
            )
        except Exception as e:
            await m.reply(f"**خطأ** \n`{e}`")
    else:
        await m.reply("**- لم يتم تشغيل اي شيء اصلا!**")


@Client.on_message(filters.command(["استئناف"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶ تم استئناف التشغيل للاغنيه المتوقفة **\n\n•  لإيقاف التشغيل مؤقتًا ، استخدم الأمر » {HNDLR}ايقاف**"
            )
        except Exception as e:
            await m.reply(f"**خطأ** \n`{e}`")
    else:
        await m.reply("** لم يتم إيقاف أي شيء مؤقتًا ❌**")
