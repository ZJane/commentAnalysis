#!/usr/bin/python 
# -*- coding:utf-8 -*-
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'commentAnalysis.settings'
django.setup()
from commentHandler.models import ProductComment

# 根据url从数据库获取商品评论，并转换成商品评论列表
def get_comment_list(url = ""):
    product_id = url.split("com/")[1].split(".html")[0]
    product_comments = ProductComment.objects.filter(product_id=product_id)
    product_comment_list = list(product_comments)

    comments_list = []
    for pc in product_comment_list:
        comments_list.append(pc.comment_content)
    return comments_list

if __name__ == '__main__':
    url = "https://item.jd.com/182424.html"
    comments_list = get_comment_list(url)
    print(comments_list)

