#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 2/26/2020 10:40 PM
@Author  : Alfred Lam
@FileName: run.py
@Software: PyCharm
"""
from scrapy import cmdline

cmdline.execute("scrapy crawl Konachan_spider".split(" "))
