import datetime

mysql_db = {'host': 'mysql.repos.suv163.com', 'user': 'u_xiongrencong', 'password': 'q3T8Yz6YYKL!qZB',
            'db': 'iyourcar_crawler', 'port': 32372}

qiniu_config = {'url': 'http://api-gw-internal.suv666.com/rpc/tools/qiniu/image_fetch',
                'editor_wrong_img': 'http://crawl-oss-qn.49auto.com/test/ycyh/external/content/20190110/20190110174347_Oo5tNRhD.png'}

date_time = datetime.date.today()
year = str(date_time.year)
month = str(date_time.month)
file_db = {"url": "http://res-upload-gz.tc:8710/tools/upload/news", "path": "/html/crawl/BDC_autohome_news/" + year + month + '/',
           "host": "http://res.youcheyihou.com/static/news", }

token_db = {'url': 'http://api-gw-internal.suv666.com/rpc/service/qiniu/config/get', 'type': 'ycyh_crawl_content_video'}

video_db = {'domian': 'http://crawl-oss-qn.49auto.com/'}

local_file = {'html': '/data/autohome_article_html/' + year + month + '/'}

today = datetime.datetime.now()
log_file = {'level': 'WARNING',
    'path': '/data/iyourcar/BDC_crawlers/log/BDC_autohome_news/{}_{}_{}.log'.format(today.year, today.month, today.day)}

# redis配置
crawl_redis_db = {
    'url': 'redis://:9kXp0!2EfVCKpi@s0.crawler.redis.tc:6379',
}

# 爬虫请求的url key
qq_group_redis_key = "/crawl/qq_group/start_urls"

cookie_key = '/BDC_qq_group_crawl/cookies'
