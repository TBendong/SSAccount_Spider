# -*- coding: utf-8 -*-
import httplib;
from bs4 import BeautifulSoup;
import json;
import base64;
import os;
import xml.dom.minidom as xmlParser;
try:
    conn=httplib.HTTPSConnection('us.ishadowx.net',timeout=10);
    conn.request("GET","/");
except Exception as ex:
    print "please check if the internet is ok";
else:
    res=conn.getresponse().read();
    soup=BeautifulSoup(res,'html.parser');
    # print soup;
    country=["us","jp","sg","ssr"];
    item=soup.find_all(id='ipusa');

    AllSever=[];

    class Server:
        password="";
        server_port="";
        server="";
        method="";
        remarks="";
        def __init__(self,password,port,ip,method):
            self.password=password;
            self.server_port=port;
            self.server=ip;
            self.method=method;
            self.remarks="";

        def __repr__(self):
            return repr((self.server, self.password, self.server_port,self.method,self.remarks))

    for items in country:
        for i in range(97,122):
            if soup.find(id="ip"+items+chr(i))==None or soup.find(id="pw"+items+chr(i))==None:
                continue;
            else:
                # print soup
                ip=soup.find(id="ip"+items+chr(i)).string.strip();
                print "IP->"+ip;
                password=soup.find(id="pw"+items+chr(i)).string.strip();
                print "password->"+password;
                # port=int(soup.select('.hover-text h4')[1].string[5:]);
                port=soup.find(id="port"+items+chr(i)).string.strip();
                print "port->"+port;
                method=soup.select('.hover-text h4')[3].string[7:].strip();
                print "method->"+method;
                print "-------------";
                AllSever.append(Server(password,port,ip,method));


    data={"current":1,"profiles":AllSever};

    json_str=json.dumps(data,default=lambda o: o.__dict__, sort_keys=True, indent=4, separators=(',', ': '));
    print json_str;

    file = open('ss_cfg.json', 'w')
    file.write(json_str)
    file.close()
    base64Str=base64.b64encode(json_str);
    print base64Str;

    os.popen("plutil -convert xml1 RequiredFile/clowwindy.ShadowsocksX.plist -o shadowsocks.xml");

    DOMTree=xmlParser.parse("shadowsocks.xml");
    print DOMTree.getElementsByTagName("data")[0].childNodes[0];

    DOMTree.getElementsByTagName("data")[0].childNodes[0].data=base64Str;

    try:
        file_handle = open("shadowsocks.xml","wb");
        DOMTree.writexml(file_handle);
        # if os.path.exists("~/Library/Preferences/shadowsocks.plist")==False:
        #     os.popen("cp RequiredFile/shadowsocks.plist ~/Library/Preferences/");
        # os.popen("plutil -convert binary1 shadowsocks.xml -o shadowsocks.plist");
        # os.popen("defaults import clowwindy.ShadowsocksX shadowsocks.plist");
    except Exception as ex:
        print ex.message;
