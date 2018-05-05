#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 使用nltk库进行处理的结果
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

# 正则表达式，去除每条评论的标点符号
def get_clean_comment(comment_str):
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comment_str)
    cleaned_comments = ''.join(filterdata)
    # print(cleaned_comments)
    return cleaned_comments

# 对每条评论进行分词并删除停用词，这里用到的是nltk库，建议换成snownlp库
def get_clean_token(cleaned_comment):
    # 分词，
    tokens = jieba.cut(cleaned_comment)
    # 删除中文停用词
    stoplist = stopwords.words('chinese')
    clean_tokens = [token for token in tokens if token not in stoplist]
    #print(clean_tokens)
    #print(tokens)
    return clean_tokens

# 对所有评论进行去除标点符号，分词并删除停用词，返回所有tokens
def get_all_clean_tokens(comments=[]):
        comment_count = len(comments)
        # print(comment_count)
        all_tokens = []
        for i in range(0,comment_count):
            #print(self.comments[i])
            clean_comment = get_clean_comment(str(comments[i]))
            #print(clean_comment)
            clean_tokens = get_clean_token(clean_comment)
            print(clean_tokens)
            all_tokens.extend(clean_tokens)
        return all_tokens
# 统计词频，参数是分词、移除停用词的关键词列表
def count_word_freq(text = []):
    words_df = pd.DataFrame({'segment': text})
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
    words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
    for x in words_stat.values:
        print(x)
    word_fre = {x[0]: x[1] for x in words_stat.values}
    print(word_fre)
    print(type(word_fre))
    return word_fre

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
    all_tokens = get_all_clean_tokens(comments_list)
    print(all_tokens)
    #text = ["我", "喜欢", "分词", "python", "旅行", "喜欢", "旅行", "喜欢", "旅行", "喜欢", "旅行", "喜欢"]
    word_fre_dict = count_word_freq(all_tokens)
    word_cloud = plot_word_cloud(word_fre_dict)
