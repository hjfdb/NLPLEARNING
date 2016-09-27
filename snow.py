# -*- coding: UTF-8 -*-

__author__ = 'ChAngIng'
#from snownlp import SnowNLP
import jieba
import jieba.analyse
import time

from snownlp import sentiment

# sentiment.train('neg.txt', 'pos.txt')
# sentiment.save('sentiment.marshal')

file_object = open('./titles1.txt')
try:
    all_the_text = file_object.read()
# print all_the_text
finally:
    file_object.close()

#seg_list = jieba.cut("SMG进军VR！广电系的VR打法与爱奇艺优土有何不同？专访王建军", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# TF-IDF 算法的关键词抽取
tags = jieba.analyse.extract_tags(all_the_text, topK=30, withWeight=False, allowPOS=())
# sentence 为待提取的文本
# topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
# withWeight 为是否一并返回关键词权重值，默认值为 False
# allowPOS 仅包括指定词性的词，默认值为空，即不筛选
print(",".join(tags))

# TextRank
tags = jieba.analyse.textrank(all_the_text, topK=30, withWeight=False, allowPOS=('ns', 'n', 'vn'))
print(",".join(tags))

# ls = []
# for w in all_the_text.split('\n'):
#    ls.append(w.decode('utf-8'))

# s = SnowNLP(u'SMG进军VR！广电系的VR打法与爱奇艺优土有何不同？专访王建军')
# print("Default Mode: " + "/ ".join(s.words))  # 精确模式


# s.words(分词)
# s.tags（关键词）
# s.sentiments（情感度）
# s.pinyin（拼音）
# s.keywords(3)（关键词）
# s.summary(3)（关键句子）
# s.sentences（语序）
# s.tf（tf值）
# s.idf（idf值）

#ls = s.tf

#file_object = open('./tf.txt', 'w')
#file_object.write(','.join(str(i.keys()[0]).decode('gb2312') + ':' + str(i.values()[0]) for i in ls))
#file_object.close()

# print s.words
#  [u'这个', u'东西', u'真心',  u'很', u'赞']

# print s.tags
#  [(u'这个', u'r'), (u'东西', u'n'),
#  (u'真心', u'd'), (u'很', u'd'),
#  (u'赞', u'Vg')]
#print time.time()

#try:
#    print s.sentiments    # 0.9769663402895832 positive的概率
#except Exception as e:
#    print e
#print time.time()

# print s.pinyin
#  [u'zhe', u'ge', u'dong', u'xi',
#   u'zhen', u'xin', u'hen', u'zan']

# s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')

# print s.han
#  u'「繁体字」「繁体中文」的叫法
#  在台湾亦很常见。'