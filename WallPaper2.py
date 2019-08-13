import os
import requests
import tqdm
from lxml import etree

home_url = 'http://wallpaperswide.com'
definition = '1920x1080'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}
download_path = '/Volumes/Samsung_T5/Files/Photo/WallPapers/'


def get_xpath(html):
    return etree.HTML(html)


def get_current_page_list(page):
    req = requests.get(os.path.join(home_url, 'page', str(page)))
    if req.status_code != 200:
        raise ConnectionError
    s = get_xpath(req.text)
    current_page_list = s.xpath("//ul[@class='wallpapers']//a/@href")
    for index, page in enumerate(current_page_list):
        current_page_list[index] = page.replace('/', '')
    return current_page_list


def download_current_page_pic(url):
    req_2 = requests.get(url)
    s = get_xpath(req_2.text)
    file_path = s.xpath("//a[@target='_self' and text()='1920x1080']/@href")
    file_name = file_path[0].rsplit('/')[-1]
    download_url = os.path.join(home_url+file_path[0])
    print('Begin download_pic:{}'.format(file_name))
    req_pic = requests.get(download_url)
    if req_pic.status_code != 200:
        raise ConnectionError
    with open(download_path+'{}.jpg'.format(file_name), 'wb') as f:
        f.write(req_pic.content)
        f.close()
    print('Finish download:{}'.format(file_name))


def download_pic(start_page, end_page):
    if start_page >= end_page:
        raise ValueError('start_page should lower than end_page')
    for page_num in tqdm.trange(start_page, end_page+1):
        current_page_list = get_current_page_list(page_num)
        for next_path in current_page_list:
            url = os.path.join(home_url, next_path)
            download_current_page_pic(url)


if __name__ == '__main__':
    download_pic(1, 2)


