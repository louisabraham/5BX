import requests
from tqdm import tqdm

PATH = 'assets/img'

def download_file(url, destination):
    CHUNK_SIZE = 32768
    response = requests.get(url, stream=True)
    if 'content-length' in response.headers:
        total = int(response.headers['content-length'])
    else:
        total = None
    with open(destination, "wb") as f:
        with tqdm(total=total,
                  unit='B', unit_scale=True, unit_divisor=1024) as pbar:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    pbar.update(len(chunk))

URL = 'http://fit450.com/WEB_PAGES_AND_IMAGES/5BX%%20html%%20files/chart%s_files/image00%s.gif'
for chart in range(6):
    for ex in range(5):
        url = URL % (chart + 1, ex + 3)
        destination = PATH + '/chart%s_ex%s.png' % (chart, ex)
        download_file(url, destination)