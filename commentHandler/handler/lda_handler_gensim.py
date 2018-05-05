#!/usr/bin/python 
# -*- coding:utf-8 -*-

# gensim lda 主题模型 + nltk 删除停用词
from gensim import corpora,models,similarities
import gensim
import pandas as pd
import jieba

# 从文件中读取中文评论,转换成DataFrame格式，注意要指定encoding为utf-8
# 参数index_col指定为false，header=None:使得pandas不用第一列作为行的名称
def get_commets_from_file():
    comments = pd.read_csv("G:/毕设/commentAnalysis/commentHandler/temp_data/all_comments.txt",index_col = False, sep="/n", encoding="utf-8")
    comments = comments.dropna()
    comments_list = comments['comment'].values.tolist()
    return comments_list

# 对所有评论进行去除标点符号，分词并删除停用词，返回所有tokens
def get_all_clean_tokens(comments=[]):
        # 载入停用词表
        stopwords = pd.read_csv("G:/毕设/commentAnalysis/commentHandler/temp_data/stop_words.txt", index_col=False, sep="/n", encoding="utf-8")
        stopwords = stopwords['stopword'].values

        comment_count = len(comments)
        all_tokens = []
        for i in range(0,comment_count):
            try:
                segs = jieba.lcut(comments[i])
                segs = filter(lambda x:len(x)>1,segs) # 过滤掉空的评论
                segs = list(filter(lambda x:x not in stopwords,segs)) # 过滤掉停用词
                print(segs)
                all_tokens.append(segs)
            except Exception as e:
                print(e)
                print(comments[i])
                continue
        return all_tokens

if __name__ == '__main__':
    # 获取评论数据
    # url = "https://item.jd.com/182424.html"
    # comments_list = get_comment_list(url)
    comments_list = get_commets_from_file()
    print(comments_list)
    all_tokens = get_all_clean_tokens(comments_list)
    print(all_tokens)
    dictionary = corpora.Dictionary(all_tokens)
    corpus = [dictionary.doc2bow(tokens) for tokens in all_tokens]
    print(corpus[5])
    lda = gensim.models.LdaModel(corpus = corpus,id2word=dictionary, num_topics=10)
    for topic in lda.print_topics(num_topics = 10,num_words=5):
        print(topic[1])

