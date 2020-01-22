# _*_ coding: utf-8 _*_
#
# Step 1:
# sudo pip install requests
# Step 2:
# sudo pip install shadowsocks
# Step 3:
# In "VPN.S HTTP Proxy" or other tools, set proxy to 127.0.0.1:1080
# Step 4:
# Run "python ishadow_ss.py"
#

import requests
import re
import os


def get_free_ss_info():
    # url = 'http://xyz.ishadow.online/'
    # url = 'http://free.ishadow.online/'
    # url = 'http://ss.ishadowx.com/'
    url = 'https://a.ishadowx.net/'
    # url = 'https://mysterious-anchorage-19898.herokuapp.com/'

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    }

    try:
        html = requests.get(url, headers=headers)

    except:
        os.system('echo ' + url + '访问失败')
        return None
    os.system('echo get free ss from ' + url)

    # IP_Address
    pattern = re.compile("<h4>.*?IP Address.*?<span id=.*?>(.*?)</span>")
    ip_address = pattern.findall(html.text)
    print(ip_address)
    # os.system('echo result ' + str(html.text))

    # port
    pattern = re.compile("<h4>.*?Port.*?<span id=.*?>(.*?)\n</span>")  # 2017-12-30 修复
    port = pattern.findall(html.text)
    print(port)

    # for index, item in enumerate(port):
    #     port[index] = re.findall("\d+", item)[0]  # 清理'：'乱码

    # local_port
    local_port = "1080"

    # Password
    # 不是每个都有密码，貌似没有提供密码的不能用
    pattern = re.compile("<h4>.*?Password.*?<span id=.*?>(.*?)\n</span>")  # 2017-12-30 修复
    password = pattern.findall(html.text)
    print(password)

    # Method
    pattern = re.compile("<h4>Method:(.*?)</h4>")
    method = pattern.findall(html.text)
    print(method)


    ss_infos = []
    for i in range(len(ip_address)):
        ss_infos.append({'IP_Address': ip_address[i], 'port': port[i], 'local_port': local_port,
                         'Password': password[i], 'Method': method[i]})
    return ss_infos


def main():
    ss_infos = get_free_ss_info()

    str = '''
1-3: 美国
4-6: 日本
7-9: 新加坡
10-12: SSR
    '''
    print (str)
    i = input('请输入要使用的ss序号：')
    i = int(i)
    ss = ss_infos[i-1]

    command = "sslocal -s %s -p %s -l %s -k %s -m %s -v" % (ss.get('IP_Address'), ss.get('port'), ss.get('local_port'),
                                                         ss.get('Password'), ss.get('Method'))

    os.system('echo ' + command)
    os.system(command)

if __name__ == '__main__':
    main()
