# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from commentHandler.demo.CustomerReviews import Reviews

data=pd.read_csv('./data/vivo_x20.csv')
data=pd.read_csv('G:/毕设/DataScience/nlp/ReviewsAnalysis/reviews/AppleiPhone 8.csv')
color=list(data['productColor'].dropna().unique())

comments=Reviews(data['content'],data['score'],data['creationTime'])
comments.describe()

# 解决一词多义问题以及统一产品特征名词。比如触摸屏-->触屏等
# comments.replace('synonyms.txt')
# 分词。此处用的是结巴分词工具，添加了手机领域的专有词、以及产品特点词语，比如磨砂黑、玫瑰金
comments.segment(product_dict='G:/毕设/DataScience/nlp/ReviewsAnalysis/mobile_dict.txt',stopwords='G:/毕设/DataScience/nlp/ReviewsAnalysis/stopwords/chinese.txt',add_words=color)
# 去除无效评论
initial_words=['经济','杂交','今生今世','红红火火','彰显','荣华富贵','仰慕','滔滔不绝','永不变心','海枯石烂','天崩地裂']
comments.drop_invalid(initial_words=initial_words,max_rate=0.6)
comments.describe()

'''
from sklearn import metrics
ss=comments.sentiments(method='snownlp')
ss1=pd.cut(ss,[-0.1,0.0139,0.0315,1],labels=['差评','中评','好评'])
metrics.accuracy_score()
metrics.roc_auc_score()
'''


for k in ['好评','中评','差评']:
    keywords=comments.get_keywords(comments.scores==k)
    print('{} 的关键词为：'.format(k)+'|'.join(keywords))
    sentiments_result = comments.genwordcloud(comments.scores==k,filename='wordcloud of {}'.format(k));
    labels = "好评","中评","差评"
    sizes = [94.67,1.93,3.40]
    colors = ['yellowgreen','gold','lightcoral']
    explode = (0,0,0.1)
    plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',colors=colors)
    plt.axis('equal')
    plt.show()







