# SSAccount_Spider
这是一个mac版shadowsocks账号爬虫工具，爬取 get.ishadowx.biz的免费ss账号并导入到shadowsocks客户端<br>

## Usage

1. Install ShadowsocksX client

Download：http://160.16.231.71/ssx-2.6.3.dmg

2. run `python Spider.js` to get proxies list

This script will generate ss_cfg.json, shadowsocks.xml and shadowsocks.plist.
Note: it has dependency on bs4, you should install bs4 at first: `pip install bs4`

3. run `./run.sh` to import proxies into ShadowsocksX client

## References

https://facaiy.com/misc/2017/06/24/shadowsocks_android_import_ss_links.html
https://github.com/jameslongyoung/SSAccount_Spider
https://github.com/zinbers/shadowsocks_profiles
http://zinbers.github.io/2016/09/28/shadowsocks/
