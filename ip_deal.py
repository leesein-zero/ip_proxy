# author_li
# create time :2018/3/14

from random import choice
import re
from threading import Thread
from requests import get

import config


d = {}
ip_list = []


#获取网页源码
def GetPageContent(tar_url):
    url_content = ""
    try:
        url_content = get(tar_url,
                          headers={
                              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                              'Accept-Encoding': 'gzip, deflate, compress',
                              'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ru;q=0.4',
                              'Cache-Control': 'no-cache',
                              'Connection': 'keep-alive',
                              'Upgrade-Insecure-Requests': "1",
                              'User-Agent': choice(config.UserAgents)
                          }).text
    except BaseException as e:
        pass
    finally:
        return url_content


def GetIP():
    global d
    global ip_list
    thread_list = []
    ips = []

    #这个for 循环里，把目标网站的ip 添加到ip_list
    for tar_url in config.Url_Regular.keys():
        url_content = GetPageContent(tar_url)
        regular = config.Url_Regular.get(tar_url, "")
        tmp_ip_list = re.findall(regular, url_content)
        for item in tmp_ip_list:
            ip_list.append("{}:{}".format(item[0], item[1]))

    #设置线程池，，对 VerifyIp
    for index in range(0, config.MaxThreads):
        thread_list.append(Thread(target=VerifyIp))
    for item in thread_list:
        item.start()
    for item in thread_list:
        item.join()

    for item in d.keys():
        ips.append(item)
    return ips




def VerifyIp():
    global d
    while ip_list:
        tmp_ip_port = ip_list.pop(0)
        ip,duankou=tmp_ip_port.split(':')
        # print("verify ip: {}".format(tmp_ip_port))
        proxies = {"http": "http://{}".format(tmp_ip_port), "https": "https://{}".format(tmp_ip_port)}
        try:
            req= get(config.TestUrl,
                              proxies=proxies,
                              timeout=config.TestTimeOut,
                              headers={
                                  'User-Agent': choice(config.UserAgents)
                              })

            if req.status_code == 200:
                result=re.compile("<code>(.*?)</code>").findall(req.text)[0]

                if result == ip:
                    print('jia')
                    d.update({"{}".format(tmp_ip_port): 0})

        except :
            continue
