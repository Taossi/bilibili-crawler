import requests
import json
import chardet
import re
from pprint import pprint
# 1.根据bvid请求得到cid
def get_cid():
    url = 'https://api.bilibili.com/x/player/pagelist?bvid=BV1vy4y1i7bS&jsonp=jsonp'
    res = requests.get(url).text     # 返回json ?
    json_dict = json.loads(res)      #转化为dict
    #print(res)
    #print(json_dict)
    return json_dict["data"][0]["cid"]     # return cid (in json)
    #print(json_dict["data"][0]["cid"])

# 2.根据cid请求弹幕，解析弹幕得到最终的数据
"""
注意：哔哩哔哩的网页现在已经换了，那个list.so接口已经找不到，但是我们现在记住这个接口就行了。
"""
def get_data(cid):
    final_url = "https://api.bilibili.com/x/v1/dm/list.so?oid=" + str(cid)
    final_res = requests.get(final_url)
    final_res.encoding = chardet.detect(final_res.content)['encoding']    # detect返回字典，检查编码
    final_res = final_res.text
    #print(final_res)
    pattern = re.compile('<d.*?>(.*?)</d>')
    data = pattern.findall(final_res)
    #pprint(final_res)
    return data

# 3.保存弹幕列表
def save_to_file(data):
    with open("danmu.txt", mode="w", encoding="utf-8") as f:
        for i in data:
            f.write(i)
            f.write("\n")

cid = get_cid()
data = get_data(cid)
save_to_file(data)


if __name__ == '__main__':
    save_to_file(data)