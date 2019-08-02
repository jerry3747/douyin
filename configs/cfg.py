import datetime

mysql_db = {'host': '127.0.0.1', 'user': 'root', 'password': 'cong452452', 'db': 'iyourcar_crawler', 'port': 3306

            }

qiniu_config = {'url': 'http://api.s.suv666.com/testapi/iyourcar_tools/qiniu/image_fetch',
                'editor_wrong_img': 'http://crawl-oss-qn.49auto.com/test/ycyh/external/content/20190110/20190110174347_Oo5tNRhD.png'}

date_time = datetime.date.today()
year = str(date_time.year)
month = str(date_time.month)
file_db = {"url": "http://res-upload-test01-gz.lc:8710/tools/upload/news", "path": "/html/crawl/BDC_autohome_news/" + year + month + '/',
           "host": "http://res.youcheyihou.com/test/static/news/"}

token_db = {'url': 'http://api-gw-internal-test.suv666.com/rpc/service/qiniu/config/get',
            'type': 'ycyh_crawl_content_video'}

video_db = {'domian': 'http://crawl-oss-qn.49auto.com/'}

local_file = {'html': 'Users/iyourcar/works/files/BDC_laosiji_news/'}

today = datetime.datetime.now()
log_file = {
    'level': 'DEBUG',
    'path':  None
}
# redis配置
crawl_redis_db = {
    'url': 'redis://@localhost:6379',
}

# 爬虫请求的url key
qq_group_redis_key = "/crawl/qq_group/start_urls"

cookie_key = '/BDC_qq_group_crawl/cookies'

proxies_api = 'http://192.168.6.29:5010'