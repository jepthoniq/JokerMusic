import asyncio
from pytgcalls import idle
from config import call_py
from Musicjepthon.التشغيل import arq

        
async def main():
    await call_py.start()
    print(
        """
    ------------------
   | تم تشغيل ميوزك الجوكر |
    ------------------
"""
    )
    await idle()
    await arq.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
