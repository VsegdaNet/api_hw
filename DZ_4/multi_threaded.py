import os
import time
import requests
import concurrent.futures
from urllib.parse import urlparse

def download_image(url):
    start_time = time.time()
    response = requests.get(url)
    filename = os.path.basename(urlparse(url).path)
    with open(filename, 'wb') as f:
        f.write(response.content)
    end_time = time.time()
    print(f"Downloaded {filename} in {end_time - start_time} seconds")

def main(urls):
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])