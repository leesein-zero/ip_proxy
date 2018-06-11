# author_li
# create time :2018/6/10
from random import choice
import ip_deal
import config
import requests
import tools
ip_list=tools.get_ip()
url='https://blog.csdn.net/qq_38505990/article/details/80603007'

i=0
while ip_list:
    tmp_ip_port = ip_list.pop(0)
    proxies = {"http": "http://{}".format(tmp_ip_port), "https": "https://{}".format(tmp_ip_port)}
    headers = {'User-Agent': choice(config.UserAgents)}
    try:
        req = requests.get(url, proxies=proxies, headers=headers,timeout=config.TestTimeOut).text
    except:
        continue
    i+=1
print(i)