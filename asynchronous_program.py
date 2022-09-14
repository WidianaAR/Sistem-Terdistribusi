import asyncio
import time

waktu = time.time()

async def fungsi1():
    task = asyncio.create_task(fungsi2())
    for i in range(3):
        print(f"{i+1} = {time.time() - waktu} detik")
        await asyncio.sleep(2)
    hasil = await task
    print(hasil)

async def fungsi2():
    print(f"A = {time.time() - waktu} detik")
    await asyncio.sleep(1)
    print(f"B = {time.time() - waktu} detik")
    await asyncio.sleep(3)
    print(f"C = {time.time() - waktu} detik")
    return "Selesai"

asyncio.run(fungsi1())
