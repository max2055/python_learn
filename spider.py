# encoding:UTF-8
import urllib
import urllib.request
import re


def download_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    request = urllib.request.Request(url, headers=headers)
    data = response.read()
    return data


def get_image(html):
    regx = r'http://[\S]*\.jpg'
    pattern = re.compile(regx)
    get_img = re.findall(pattern, repr(html))
    num = 1
    for img in get_img:
        image = download_page(img)
        with open('%s.jpg' % num, 'wb') as fp:
            fp.write(image)
            num += 1
            print('%s' % num)

    return


url = 'http://pic.yesky.com/451/106166451.shtml'
html = download_page(url)
get_image(html)
