# author_li
# create time :2018/3/14
from random import choice
import ip_deal


import config

def UserAgents():
    return choice(config.UserAgents)

def get_ip():
    return ip_deal.GetIP()







if __name__ == '__main__':
    get_ip()