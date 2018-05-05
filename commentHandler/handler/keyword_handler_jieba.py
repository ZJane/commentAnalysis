#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 使用jieba的analyse模块进行关键词提取

import numpy
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import jieba
import matplotlib
import re
from nltk.corpus import stopwords
import nltk
import operator
from commentHandler.handler.get_comment_data import get_comment_list
import jieba.analyse as analyse

def get_keyword_IF(comments_list,keyword_number):
    content = " ".join(comments_list)
    print(content)
    # jieba.analyse.extract_tags(sentence,topK,withWeight,allowPOS,withFlag)
    # sentence 为待提取的文本
    # topK为返回的TF/IDF权重最大的关键词，默认值是20
    # withWeight 参数指定是否要返回关键词的权重，默认是False
    # allowPOS参数指定返回的值是否包含指定词性的词，默认是空，即不返回
    top_num = keyword_number
    result = " ".join(analyse.extract_tags(content, topK=top_num, withWeight=False, allowPOS=(), withFlag=False))
    return result

def get_keyword_TextRank(comments_list,keyword_number):
    content = " ".join(comments_list)
    print(content)
    # jieba.analyse.extract_tags(sentence,topK,withWeight,allowPOS,withFlag)
    # sentence 为待提取的文本
    # topK为返回的TF/IDF权重最大的关键词，默认值是20
    # withWeight 参数指定是否要返回关键词的权重，默认是False
    # allowPOS参数指定返回的值是否包含指定词性的词，默认是空，即不返回
    top_num = keyword_number
    result = " ".join(analyse.textrank(content, topK=top_num, withWeight=False, allowPOS=(), withFlag=False))
    return result



def plot_word_cloud(word_fre={}):
    font_path = "C:\\Users\\zhangminhua\\Desktop\\simhei.ttf"
    wc = WordCloud(
        width=1024,
        height=768,
        background_color='white',  # 设置背景颜色
        # mask=backgroud_Image,# 设置背景图片
        font_path=font_path,  # 设置中文字体，若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
        max_words=600,  # 设置最大现实的字数
        # stopwords=stopwords,# 设置停用词
        max_font_size=400,  # 设置字体最大值
        random_state=50,  # 设置有多少种随机生成状态，即有多少种配色方案
    )
    wc.fit_words(word_fre)
    plt.figure()
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    # 获取评论数据
    url = "https://item.jd.com/182424.html"
    comments_list = get_comment_list(url)
    print(comments_list)
    all_tokens = get_keyword_IF(comments_list)
    print(all_tokens)
    #text = ["我", "喜欢", "分词", "python", "旅行", "喜欢", "旅行", "喜欢", "旅行", "喜欢", "旅行", "喜欢"]
    word_fre_dict = count_word_freq(all_tokens)
    word_cloud = plot_word_cloud(word_fre_dict)
