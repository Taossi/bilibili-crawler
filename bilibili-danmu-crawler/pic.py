# 1 导入相关库
import pandas as pd
import jieba   #结巴分词模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy
import PIL.Image as Image
from imageio import imread
import bilibili as bili

import warnings
warnings.filterwarnings("ignore")

stop_words = open("cn_stopwords.txt",encoding="utf8").read().split("\n")

#1.将字符串切分
def chinese_jieba(text):
    wordlist_jieba=jieba.cut(text)
    space_wordlist=" ".join(wordlist_jieba)
    return space_wordlist

def cloudPicture1(file):
    # "danmu.txt"
    with open(file ,encoding="utf-8")as file:
        #1.读取文本内容
        text=file.read()
        #text=chinese_jieba(text)
        #2.设置词云的背景颜色、宽高、字数
        wordcloud=WordCloud(scale=4,font_path='/Library/Fonts/Songti.ttc',background_color="black",width=800,height=400,max_words=50,min_font_size=8).generate(text)
        #3.生成图片
        image=wordcloud.to_image()
        #4.显示图片
        image.show()
        wordcloud.to_file('pic1.png')

def cloudPicture2(file):
    with open(file ,encoding="utf-8")as file:
        text=file.read()
        #text=chinese_jieba(text)
        #2.图片遮罩层
        #mask_pic=numpy.array(Image.open("bingbing.jpg"))
        mask_pic= imread(r"bingbing.jpg")
        #3.将参数mask设值为：mask_pic
        wordcloud = WordCloud(scale=4,font_path="/Library/Fonts/Songti.ttc",mask=mask_pic).generate(text)
        image=wordcloud.to_image()
        image.show()
        wordcloud.to_file('pic2.png')

if __name__ == '__main__':
    file="danmu.txt"
    #cloudPicture1(file)
    cloudPicture2(file)
