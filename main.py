import asyncio
from pytgcalls import idle
from config import call_py
from Musicjepthon.التشغيل import arq
from Musicjepthon.helpers import web_server

        
async def main():
    await call_py.start()
    print(
        """
    ------------------
   | تم تشغيل ميوزك الجوكر |
    ------------------
"""
    )
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    redaport = Config.PORT
    await web.TCPSite(app, bind_address, redaport).start()
    await idle()
    await arq.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
