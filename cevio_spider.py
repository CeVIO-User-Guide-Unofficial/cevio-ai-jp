# coding=utf-8
import os
import requests
import re
import bs4
from bs4 import BeautifulSoup

from markdownify import markdownify as md

sub_folder_regex = r'(https://cevio\.jp/guide/cevio_ai/)(.+?)(/.*)'

class CevioSpider:
    def __init__(self, local_doc_path, doc_url):
        self.doc_path = local_doc_path
        self.doc_url = doc_url
        self.home_soup = None
        self.nav_links = None
        
        if not os.path.exists(self.doc_path):
            os.mkdir(self.doc_path)

    @staticmethod
    def analysis_url(url):
        while True:
            try:
                response = requests.get(url)
            except Exception as e:
                print(e)
                continue
            break
        response.encoding = 'uft-8'
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    
    # 拿到根目录的内容
    def analysis_doc(self):
        self.home_soup = self.analysis_url(self.doc_url)
        self.nav_links = self.home_soup.select('body > main > nav > p > a')

    # 保存正文内容
    @staticmethod
    def save_content(soup, file_name):
        print(file_name)
        content = soup.select_one("[class~=window]")
        with open(file_name + '.md', 'w', encoding='utf-8') as fs:
            fs.write(md(content.prettify()))

    # 保存图片
    @staticmethod
    def save_image(path, link):
        img_folder = os.path.join(path, 'images')
        if not os.path.exists(img_folder):
            os.mkdir(img_folder)

        with open(os.path.join(img_folder, link.split('/')[-1]), 'wb') as f:
            for chunk in re.iter_content(chunk_size=1024):
                f.write(chunk)

    @staticmethod
    def get_sub_folder_name(link):
        sub_folder_name = re.match(sub_folder_regex, link).group(2)
        if sub_folder_name == 'tutorial_talk':
            sub_folder_name = 'talktrack'
        elif sub_folder_name == 'tutorial_song':
            sub_folder_name = 'songtrack'
        return sub_folder_name

    # 保存侧边栏的文档
    def save_sub_docs(self):
        for nav_link in self.nav_links:
            link = nav_link.get('href')
            print(link)
            
            sub_folder_name = self.get_sub_folder_name(link)
            sub_folder = os.path.join(self.doc_path, sub_folder_name)
            if not os.path.exists(sub_folder):
                os.mkdir(sub_folder)
            
            while True:
                try:
                    sub_soup = self.analysis_url(link)
                except requests.exceptions.SSLError:
                    continue
                break
            
            self.save_content(sub_soup, os.path.join(sub_folder, sub_soup.title.string))
            self.save_all_images(sub_soup, sub_folder)
            
    # 保存正文里的所有图片
    @staticmethod
    def save_all_images(soup, path):
        img_url = 'http://cevio.jp/guide/cevio_ai/'
        for img in soup.find_all('img'):
            try:
                link = img.get('src')
                
                # skip header image
                if link.endswith('header_image_title.png'):
                    continue
                    
                # build legal url
                if not link.startswith(img_url):
                    if link.startswith('../'):
                        link = link.strip('../')
                    link = img_url + link
                print(link)
                
                re = requests.get(link)

                img_folder = os.path.join(path, 'images')
                if not os.path.exists(img_folder):
                    os.mkdir(img_folder)

                with open(os.path.join(img_folder, link.split('/')[-1]), 'wb') as f:
                    for chunk in re.iter_content(chunk_size=1024):
                        f.write(chunk)
            except Exception as e:
                print(e)
                continue
                
    def run(self):
        self.analysis_doc()
        self.save_sub_docs()
        self.save_content(self.home_soup, os.path.join(self.doc_path, self.home_soup.title.string))
        self.save_all_images(self.home_soup, self.doc_path)

if __name__ == '__main__':
    doc_path = './docs'
    doc_url = 'https://cevio.jp/guide/cevio_ai/'

    spider = CevioSpider(doc_path, doc_url)
    spider.run()
