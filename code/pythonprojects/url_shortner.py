import contextlib
from urllib.parse import urlencode
from urllib.request import urlopen
import sys

def get_tiny_url(url):
    request_url = 'http://tinyurl.com/api-create.php?'+urlencode({'url': url})

    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

if __name__ == '__main__':
    url = input('Enter the URL: ')
    print('Short URL: ', get_tiny_url(url))