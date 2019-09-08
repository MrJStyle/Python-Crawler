import os
import time
import logging
from selenium import webdriver
from lxml import etree

log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger('youtube')


class YoutubeDownload(object):
    def __init__(self, url):
        chrome_options = webdriver.ChromeOptions()
        # 使用headless无界面浏览器模式
        chrome_options.add_argument('--headless')  # 增加无界面选项
        chrome_options.add_argument('--disable-gpu')  # 如果不加这个选项，有时定位会出现问题

        self.url = url
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)

    def get_xpath_elements(self):
        page_source = self.browser.page_source
        html = etree.HTML(page_source)
        return html


    def get_label_list(self, xpath, html):
        return html.xpath(xpath)

    def download_m4a(self, path, url, index=140):
        return os.system('youtube-dl --proxy {} -f {} {} -o {}'.format('localhost:1087', index, url, path))


if __name__ == '__main__':
    youtube = YoutubeDownload('https://www.youtube.com/user/JFlaMusic/videos?view=0&sort=dd&shelf_id=11')
    logger.info('finish init')
    html = youtube.get_xpath_elements()
    xpath = "//a[@class='yt-simple-endpoint style-scope ytd-grid-video-renderer']"
    a_label_list = youtube.get_label_list(xpath, html)
    video_url_list = ["http://www.youtube.com"+i.xpath('@href')[0] for i in a_label_list]
    title_list = [i.xpath('@title')[0].replace('(', '').replace(')', '').replace(' ', '_') for i in a_label_list]
    bind_list = dict(zip(title_list, video_url_list))
    for index, title in enumerate(bind_list):
        path = '/Volumes/Samsung_T5/Files/Music/JFla/{}'.format(title+'.m4a')
        logger.info('start download {}'.format(title))
        youtube.download_m4a(path=path, url=bind_list.get(title))
        logger.info('finish download {} finish rate: {} / {}'.format(title, index+1, len(bind_list)))
    logger.info('finish download all')