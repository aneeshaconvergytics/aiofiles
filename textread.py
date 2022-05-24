
import aiofiles
import asyncio
import json


async def main():
    async with aiofiles.open('file.txt', mode='r') as f:
        contents = await f.read()
        print(contents)

asyncio.run(main())