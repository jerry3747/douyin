#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import json
from mitmproxy import ctx, http
from urllib.parse import unquote, quote
from frozen_path import app_path

heads_file = app_path() + '/data/header.txt'

body_file = app_path() + '/data/body.txt'


def bytes_to_str(s, encoding='utf-8'):
    """Returns a str if a bytes object is given."""
    if isinstance(s, bytes):
        return s.decode(encoding)
    return s


class Spider(object):
    def __init__(self):
        print('-------------------------------------------------------------')

    def request(self, flow: http.HTTPFlow):
        url = flow.request.url
        with open(heads_file, 'a+') as f:
            f.write(url + '\n')

    def response(self, flow: http.HTTPFlow):
        url = unquote(flow.request.url)
        ctx.log.info(url)
        host = 'https://aweme-hl.snssdk.com/aweme/v1/general/search/single/'
        if url.startswith(host):
            response = flow.response.get_text()
            self.parse_response(response)
        else:
            return

    def parse_response(self, response):
        response = json.loads(response)
        items = response.get('data')
        if items:
            for item in items:
                result = {}
                unique_id = item.get('aweme_info').get('author').get('uid')
                if unique_id:
                    result['author_id'] = unique_id  # 抖音号
                else:
                    result['author_id'] = item.get('aweme_info').get('author').get('short_id')
                result['nickname'] = item.get('aweme_info').get('author').get('nickname')  # 用户名
                result['url'] = item.get('aweme_info').get('share_url')  # 小视频链接
                result['like_num'] = item.get('aweme_info').get('statistics').get('digg_count')  # 点赞数
                result['comment_count'] = item.get('aweme_info').get('statistics').get('comment_count')  # 评论次数
                result['share_count'] = item.get('aweme_info').get('statistics').get('share_count')  # 分享次数
                result['info'] = item.get('aweme_info').get('desc')  # 视频说明
                ctx.log.info(result)
                with open(body_file, 'a+') as f:
                    f.write(str(result) + '\n')
