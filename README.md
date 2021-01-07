# bilibili-crawler
bilibili弹幕爬虫+词云生成 自己写的简易版。

# bilibili.py

生成弹幕的txt文件。通过b站网页信息里的cid 来提取文件。 也可以直接输入视频的AV号，修改url。

# pic.py

生成词云。 调用jieba和wordcloud两个库

注意事项：如果要把词云轮廓设置成某个特别形状（比如某张图片中的形状），需要注意，图片的背景要要为白色。

我在实践中是事先ps指定图片，再进行词云生成。

# 我的实践效果

恰逢冰冰入驻B站，我便以冰冰的视频为例([BV1vy4y1i7bS](https://www.bilibili.com/video/BV1vy4y1i7bS))

并且随机选取了冰冰的一张照片，简略的p图过后，最后得到的冰冰版词云如下：

![image](https://github.com/Taossi/bilibili-crawler/blob/main/bilibili-danmu-crawler/pic2.png)

哈哈哈
