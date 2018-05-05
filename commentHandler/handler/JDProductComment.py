#!/usr/bin/python 
# -*- coding:utf-8 -*-
import urllib.request
import urllib
import jieba
import json
import re
from nltk.corpus import stopwords
import nltk
from bs4 import BeautifulSoup
import pymysql
import django
import os
import datetime
os.environ['DJANGO_SETTINGS_MODULE'] = 'guideForBeauty.settings'
django.setup()
from commentHandler.models import Product,ProductComment

class JDProductComment:
    def __init__(self):
        self.productListUrls = []
        self.productUrls = set() # 所有商品的url地址
        self.headers = {"Host": "ss.3.cn",
                   "Origin": "http://www.jd.com/",
                   "Referer": "http://www.jd.com/",
                   "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                   "Accept": "*/*",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
                   }
        self.product_table = Product
        self.product_comment_table = ProductComment


    # 根据url下载html
    def get_html(self,url):
        get_time = 3 # 重复发送http请求的最大次数
        if(url != None):
            req = urllib.request.Request(url)
            req.add_header("Referer", "http://www.jd.com/")
            req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")

            while(get_time > 0):
                try:
                    response = urllib.request.urlopen(req)
                    html = response.read()
                    return html
                    break # 成功获取html，跳出循环
                except urllib.error.HTTPError as e:
                    print("Download error: ", e.reason)
                    if 500 <= e.code and e.code < 600:  # 5XX:当错误发生在服务端时,重新发送2次
                        get_time = get_time-1
                    else:
                        break

    # 根据商品详情的url获取商品id
    def get_id_from_url(self,url):
        id = url.split("com/")[1].split(".html")[0]
        return id

    # 根据商品id和页数构造获取评论的url,pagesize为默认的10
    def get_comment_url(self,id,page):
        comment_url = "https://club.jd.com/comment/productPageComments.action?productId="\
                      +str(id)+"&score=0&sortType=5&page="+str(page)+"&pageSize=10&isShadowSku=0&fold=1"
        #print(comment_url)
        return comment_url

    # 判断是否是最后一页评论
    def is_last_page(self,htmlcontent):
        if len(htmlcontent)> 2364:
            return True
        else:
            return False

    #
    # 获取商品评论数据
    def get_comment_data(self):
        product = Product.objects.get(product_id=17)
        # products = Product.objects.filter(product_id > 15)
        product_url = product.detail_url
        print(product_url)
        product_id = self.get_id_from_url(product_url)
        print(product_id)
        for page in range(0,100):
            print("page = " + str(page))
            comment_page_url = self.get_comment_url(product_id,page)
            html_content = self.get_html(comment_page_url)
            # print(html_content)
            comment_json = json.loads(html_content.decode("gbk"))
            product_comments = comment_json['comments']
            for i in range(0,10):
                product_comment = product_comments[i]['content']
                print("第"+str(i)+"条评论"+product_comment)
                comment_id = product_comments[i]['id']
                creation_time = product_comments[i]['creationTime']
                comment_uid = product_comments[i]['nickname']
                product_name = product_comments[i]['referenceName']

                print(type(product_comments[i]))
                if 'afterUserComment' in product_comments[i]:
                    after_comment_content = product_comments[i]['afterUserComment']['hAfterUserComment']['content']
                else:
                    after_comment_content = ""
                print(after_comment_content)
                get_time = datetime.datetime.now()
                print(get_time)
                # 存进数据库
                product_comment_obj = self.product_comment_table(comment_id=comment_id,
                                                             product_id=product_id,
                                                             comment_content=product_comment,

                                                             creation_time=creation_time,
                                                             comment_uid=comment_uid,
                                                             get_time=get_time,
                                                             product_name=product_name,
                                                             after_comment_content=after_comment_content)
                print(product_comment_obj)
                product_comment_obj.save()


    # 根据商品的url获取商品评论
    def get_comment_from_url(self,url):
        product_id = self.get_id_from_url(url)
        comments = []
        # 通过product_id判断该商品评论是否已经爬过，若是，直接从数据库获取
        product_objects = ProductComment.objects.filter(product_id=product_id)
        records = product_objects.count()
        if  records > 0:
            # print("数据已经爬取")
            for i in range(0,records):
            #for i in range(0, 100):
                comments.append(product_objects[i].comment_content)
                print("第" + str(comments.__len__()) + "条评论: " + comments[i])

        else:
            print("数据未爬取")
            for page in range(0,100):
                comment_page_url = self.get_comment_url(product_id,page)
                html_content = self.get_html(comment_page_url)
                # 文本内容转换成json格式
                try:
                    comment_json = json.loads(html_content.decode("gbk"))
                except:
                    pass
                product_comments = comment_json['comments']
                for i in range(0,10):
                    product_comment = product_comments[i]['content']
                    comments.append(product_comments)
                    print("第"+str(comments.__len__())+"条评论: "+product_comment)

                    comment_id = product_comments[i]['id']
                    creation_time = product_comments[i]['creationTime']
                    comment_uid = product_comments[i]['nickname']
                    product_name = product_comments[i]['referenceName']
                    if 'afterUserComment' in product_comments[i]:
                        after_comment_content = product_comments[i]['afterUserComment']['hAfterUserComment']['content']
                    else:
                        after_comment_content = ""
                    get_time = datetime.datetime.now()

                    # 存进数据库
                    product_comment_obj = self.product_comment_table(comment_id=comment_id,
                                                                 product_id=product_id,
                                                                 comment_content=product_comment,

                                                                 creation_time=creation_time,
                                                                 comment_uid=comment_uid,
                                                                 get_time=get_time,
                                                                 product_name=product_name,
                                                                 after_comment_content=after_comment_content)
                    product_comment_obj.save()
        # print(comments)
        print("数据已经爬取")
        return comments

    def test(self):
        url = "https://item.jd.com/1955298.html"
        comments = self.get_comment_from_url(url)
        # product_objects = ProductComment.objects.filter(product_id=305551)
        # print(product_objects.count())
        # a = product_objects[0].comment_content
        # print(a)

        allComment = ''
        for k in range(len(comments)):
            allComment = allComment + (str(comments)).strip()

        pattern = re.compile(r'[\u4e00-\u9fa5]+')
        filterdata = re.findall(pattern, allComment)
        cleaned_comments = ''.join(filterdata)
        # 分词 分词结果返回的是一个生成器（这对大数据量数据的分词尤为重要）。
        tokens = jieba.cut(cleaned_comments)
        # print(','.join(tokens))
        token_str = ','.join(tokens)
        type(token_str)
        f = open('token.txt','w+')
        f.write(token_str)
        f.close()
        return token_str

if __name__ == '__main__':
    test = JDProductComment()
    test.__init__()
    # test.get_product_list_urls()
    # print("请输入  你要查询的商品链接")
    # # 1955298\
    url = "https://item.jd.com/1955298.html"
    comments = test.get_comment_from_url(url)

    # 词频统计
    freq_dis = {}
    for k in range(0,3):
        comment_str = comments[k]
        # 正则表达式，去除每条评论的标点符号
        pattern = re.compile(r'[\u4e00-\u9fa5]+')
        filterdata = re.findall(pattern, comment_str)
        cleaned_comments = ''.join(filterdata)
        print(cleaned_comments)

        # 分词，
        tokens = jieba.cut(cleaned_comments)
        # 删除停用词
        # nltk.download('stopwords')
        stoplist = stopwords.words('chinese')
        cleantokens = [token for token in tokens if token not in stoplist]
        print(cleantokens)
        print(tokens)
        # 统计频率
        for token in cleantokens:
            if token in freq_dis:
                freq_dis[token] += 1
            else:
                freq_dis[token] = 1

    for key in freq_dis.keys():
        print(key + ":" + str(freq_dis[key]))

    # 按照频率次数排序
    # sorted_freq_dis = sorted(freq_dis.keys(),)
    # print(sorted_freq_dis)

    # 去除停用词

        #
    # allComment = ''
    # for k in range(len(comments)):
    #     allComment = allComment + (str(comments)).strip()
    #
    # pattern = re.compile(r'[\u4e00-\u9fa5]+')
    # filterdata = re.findall(pattern, allComment)
    # cleaned_comments = ''.join(filterdata)
    # # 分词 分词结果返回的是一个生成器（这对大数据量数据的分词尤为重要）。
    # tokens = jieba.cut(cleaned_comments)
    # print(','.join(tokens))
    #
    #
    #
