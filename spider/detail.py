#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import re
import json
import requests
from lxml import etree
from fontTools.ttLib import TTFont
from frozen_path import app_path
from BDC_module_proxy import ProxyGetter


class DouYin(object):

    ttfond = TTFont(app_path() + "/data/iconfont_9eb9a50.woff")
    ttfond.saveXML(app_path() + "/data/iconfont_9eb9a50.xml")

    def __int__(self):
        pass

    def get_cmap_dict(self):
        """
        :return: 关系映射表
        """
        # 从本地读取关系映射表【从网站下载的woff字体文件】
        best_cmap = self.ttfond["cmap"].getBestCmap()
        # 循环关系映射表将数字替换成16进制
        best_cmap_dict = {}
        for key,value in best_cmap.items():
            best_cmap_dict[hex(key)] = value
        return best_cmap_dict   # 'num_1', '0xe604': 'num_2', '0xe605': 'num_3'

    def get_num_cmap(self):
        """
        :return: 返回num和真正的数字映射关系
        """
        num_map = {
            "x":"", "num_":1, "num_1":0,
            "num_2":3, "num_3":2, "num_4":4,
            "num_5":5, "num_6":6, "num_7":9,
            "num_8":7, "num_9":8,
        }
        return num_map


    def map_cmap_num(self,get_cmap_dict,get_num_cmap):
        new_cmap = {}
        for key,value in get_cmap_dict().items():
            key = re.sub("0","&#",key,count=1) + ";"    # 源代码中的格式 &#xe606;
            new_cmap[key] = get_num_cmap()[value]
            # 替换后的格式
            # '&#xe602;': 1, '&#xe603;': 0, '&#xe604;': 3, '&#xe605;': 2,
        return new_cmap


    # 获取网页源码
    def get_html(self,url):
        ip = ProxyGetter(project_name = 'douyin').getter_server_proxy()
        proxy = {'https':'https://' + ip}
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        response = requests.get(url,headers=headers, proxies=proxy).text
        return response

    def replace_num_and_cmap(self,result,response):
        """
        将网页源代码中的&#xe603;替换成数字
        :param result:
        :param response:
        :return:
        """
        for key,value in result.items():
            if key in response:
                # print(777)
                response = re.sub(key, str(value), response)
        return response

    def manage(self,response):
        res = etree.HTML(response)
        douyin_name = res.xpath('//p[@class="nickname"]//text()')[0]
        douyin_id = 'ID:'+''.join(res.xpath('//p[@class="shortid"]/i//text()')).replace(' ','')
        guanzhu_num = ''.join(res.xpath('//span[@class="focus block"]//text()')).replace(' ','')
        fensi_num = ''.join(res.xpath('//span[@class="follower block"]//text()')).replace(' ','')
        dianzan = ''.join(res.xpath('//span[@class="liked-num block"]//text()')).replace(' ','')
        print(douyin_name,douyin_id,guanzhu_num,fensi_num,dianzan)
        line = douyin_name + " " + douyin_id + " " + guanzhu_num + ' ' + fensi_num + ' ' + dianzan
        with open(app_path() + '/data/author.txt', 'a+', encoding = 'utf-8') as f:
            f.write(line + '\n')

    def read_author_id(self):
        with open(app_path() + '/data/body.txt', 'r') as f:
            lines = f.readlines()
            return lines

    def main(self):
        lines = self.read_author_id()
        for line in lines:
            line = re.sub('\'', '"', line)
            data = json.loads(line)
            author_id = data['id']
            url = 'https://www.iesdouyin.com/share/user/' + str(author_id)
            response = self.get_html(url)
            new_cmap = self.map_cmap_num(self.get_cmap_dict, self.get_num_cmap)
            res = self.replace_num_and_cmap(new_cmap, response)
            self.manage(res)


if __name__ == '__main__':
    dy = DouYin()
    dy.main()