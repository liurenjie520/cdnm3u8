# coding=utf-8
import urllib3
import os
import json
import base64
import time


# 未添加新浪微博的cookie和上传图片路径

# 上传图片
def UpImg(File):
    try:
        http = urllib3.PoolManager()
        # 设置UA和Cookie
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Cookie': 'usPkW1KyW',
        }
        # 上传接口
        url = "https://picupload.weibo.com/interface/pic_upload.php?ori=1&mime=image%2Fjpeg&data=base64&url=0&markpos=1&logo=&nick=0&marks=1&app=miniblog"

        f = open(File, 'rb')
        values = {
            'b64_data': base64.b64encode(f.read()),  # 将图片转换为base64
            'pic1': File
        }
        f.close()
        r = http.request('POST', url, fields=values, headers=headers)  # post方式调用API
        data = r.data.decode('utf-8')  # 解析返回内容
        data = data.replace('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />', '')
        data = data.replace('<script type="text/javascript">document.domain="sina.com.cn";</script>', '')
        jData = json.loads(data)  # 解析返回的json
        pid = jData['data']['pics']['pic_2']['pid']

        # 拼接图片地址
        imgUrl = 'http://ww1.sinaimg.cn/large/{pid}.jpg'.format(pid=pid)
        print("图片{file}上传成功，地址：{imgUrl}".format(file=File, imgUrl=imgUrl))
        return imgUrl
    except:
        print("图片{file}上传失败,3秒后将重试".format(file=File))
        time.sleep(3)
        UpImg(File)


if __name__ == '__main__':
    path = "./bmlastfile"
    urlList = []
    for file in os.listdir(path):
        url = UpImg(path + "\\" + file)
        # 写入图片地址到本地文件
        f = open('filelist.txt', 'a+')
        f.write(url + "\n")
        f.close()
