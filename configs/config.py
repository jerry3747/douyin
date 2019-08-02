#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jerry'
from configs.cfg_test import crawl_redis_db, proxies_api

bdc_module_project_name = 'BDC_qq_group_crawl'
bdc_module_log_path = './'
bdc_module_redis_url = crawl_redis_db['url']
bdc_module_proxies_api = proxies_api