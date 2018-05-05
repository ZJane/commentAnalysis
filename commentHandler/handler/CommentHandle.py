#!/usr/bin/python 
# -*- coding:utf-8 -*-

from comment_datascrape.JDProductComment import JDProductComment
import jieba
import matplotlib
import re
from nltk.corpus import stopwords
import nltk
import operator
from bs4 import BeautifulSoup
import pymysql
import django
import os
import datetime
os.environ['DJANGO_SETTINGS_MODULE'] = 'guideForBeauty.settings'
django.setup()
from commentHandler.models import Product,ProductComment

class CommentHandle:
    def __init__(self):
        self.comments = []
        self.product_table = Product
        self.product_comment_table = ProductComment
        self.freq_dist = {}
        self.clean_tokens = []
    def get_comment(self,url):
        url = "https://item.jd.com/1955298.html"
        test = JDProductComment()
        self.comments = test.get_comment_from_url(url)
        # return self.comments

    # 正则表达式，去除每条评论的标点符号
    def get_clean_comment(self,comment_str):
        pattern = re.compile(r'[\u4e00-\u9fa5]+')
        filterdata = re.findall(pattern, comment_str)
        cleaned_comments = ''.join(filterdata)
        #print(cleaned_comments)
        return cleaned_comments

    # 对每条评论进行分词并删除停用词
    def get_clean_token(self,cleaned_comment):
        # 分词，
        tokens = jieba.cut(cleaned_comment)
        # 删除中文停用词
        stoplist = stopwords.words('chinese')
        clean_tokens = [token for token in tokens if token not in stoplist]
        #print(clean_tokens)
        #print(tokens)
        return clean_tokens

    # 对所有评论进行去除标点符号，分词并删除停用词，返回所有tokens
    def get_all_clean_tokens(self):
        comment_count = len(self.comments)
        # print(comment_count)
        for i in range(0,comment_count):
            #print(self.comments[i])
            clean_comment = self.get_clean_comment(str(self.comments[i]))
            #print(clean_comment)
            clean_tokens = self.get_clean_token(clean_comment)
            print(clean_tokens)
            self.clean_tokens.extend(clean_tokens)
    # 词频统计
    def get_comment_freq(self,clean_tokens):
        for token in clean_tokens:
            if token in self.freq_dist:
                self.freq_dist[token] += 1
            else:
                self.freq_dist[token] = 1
        # sort_freq_dist = sorted(self.freq_dist.values(), key=operator.itemgetter(1),reverse = True)
        # print(sort_freq_dist[:25])
        for key in self.freq_dist.keys():
            print(key + ":" + str(self.freq_dist[key]))
        return self.freq_dist
    def get_nltk_comment_freq(self,clean_tokens):
        Freq_dist_nltk = nltk.FreqDist(clean_tokens)
        # print(Freq_dist_nltk)
        for k,v in Freq_dist_nltk.items():
            print(str(k)+":"+str(v))
        Freq_dist_nltk.plot(50,cumulative=False)

# 运行脚本
if __name__ == '__main__':
    # from comment_datascrape.JDProductComment import JDProductComment
    # from comment_datascrape.CommentHandle import CommentHandle
    url = "https://item.jd.com/1955298.html"
    comment_test = CommentHandle()
    comment_test.get_comment(url)

    comment_test.get_all_clean_tokens()
    comment_test.get_comment_freq(comment_test.clean_tokens)
