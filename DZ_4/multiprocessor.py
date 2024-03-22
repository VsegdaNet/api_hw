import os
import multiprocessing
import requests
from urllib.parse import urlparse

# Вызвать python script.py https://example.com/image1.jpg https://example.com/image2.jpg


def download_image(url):
    response = requests.get(url)
    filename = os.path.basename(urlparse(url).path)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {filename}")

def main(urls):
    with multiprocessing.Pool() as pool:
        pool.map(download_image, urls)

if __name__ == "__main__":
    image_urls = [
        "https://demotivation.ru/wp-content/uploads/2020/11/a88ca4cdc69aa0d9bc8064f7d36871a4.jpg",
        
    ]
    main(image_urls)