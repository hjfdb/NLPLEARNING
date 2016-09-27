# encoding=utf-8

import jieba

import nltk

# 精确模式，试图将句子最精确地切开，适合文本分析；
# 全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
#搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。

seg_list1 = jieba.cut(
    "从下单到手只用了3个多小时，真快啊，赞一下京东的配送速度，机子收到是原封的，深圳产，没有阴阳屏和跑马灯，还不错，三星的U，但不纠结，也 没有感觉有多费电，激活后买了c+，可以随意裸机体验了，整体来说很满意")

# 默认是精确模式
seg_list = jieba.cut(
    "使用了一周多来评价优化过后开机10秒左右运行不卡顿屏幕清晰无漏光巧克力键盘触感非常不错音质也很好外观漂亮质量轻巧尤其值得称赞的是其散热系统 我玩LOL三四个小时完全没有发烫暂时没有发现什么缺点如果有光驱就更好了值得入手值得入手值得入手～不枉费我浪费了12期免息券加首单减免*的优惠最后换了这台适合办公的 之前是买的惠普的暗夜精灵玩游戏超棒的")
# 默认是精确模式

str1 = " ".join(seg_list1)
str2 = " ".join(seg_list)
print str1
print str2
allText = str1 + str2

#allText = PlaintextCorpusReader(corpus_root, ['comment4.txt', 'comment5.txt'])

#print type(allText)

sinica_text = nltk.Text(allText)

mytexts = nltk.text.TextCollection(allText)

print len(mytexts._texts)

print len(mytexts)

the_set = set(sinica_text)
print
len(the_set)
for tmp in the_set:
    print
    tmp, "tf", mytexts.tf(tmp, str1), "idf", mytexts.idf(tmp), mytexts.tf_idf(tmp, str2)

# nltk的贝叶斯分类器函数使用总结
# 先定义一个特征提取函数,该函数返回一个dict,其中key为维度名称,value为维度值
def getFeature(sample):
    return {'d1': 5, 'd2': False}



