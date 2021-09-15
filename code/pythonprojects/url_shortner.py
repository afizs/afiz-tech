import contextlib
from urllib.parse import urlencode
from urllib.request import urlopen
import sys

def get_tiny_url(url: str) -> str:
    request_url = 'http://tinyurl.com/api-create.php?'+urlencode({'url': url})
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

if __name__ == '__main__':
    print(get_tiny_url('https://afizs.github.io/afiz-tech/projects/rms/'))