import os
import asyncio
import aiohttp
from urllib.parse import urlparse

async def download_image(session, url):
    async with session.get(url) as response:
        filename = os.path.basename(urlparse(url).path)
        with open(filename, 'wb') as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f.write(chunk)
        print(f"Downloaded {filename}")

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Пример списка URL-адресов
    image_urls = [
        "https://demotivation.ru/wp-content/uploads/2020/11/a88ca4cdc69aa0d9bc8064f7d36871a4.jpg",
    ]
    asyncio.run(main(image_urls))