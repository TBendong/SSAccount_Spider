# SSAccount_Spider

shadowsocks 免费代理爬虫工具，自动化一键翻墙。

## 原理

众所周知，shadowsocks 是个很好的翻墙工具，但是仅仅有这个软件本身还不够，还需要自己搭建shadowsocks服务器来提供代理服务，即所谓搭建梯子。这样的服务器通常应该位于海外，才能达到翻墙的目的。同时，购买以及搭建shadowsocks也是一件耗时耗力的事情。因此网上出现了一些提供免费shadowsocks账号的网站，这些代理账号可以直接在shadowsocks软件里使用，通常有不是特别稳定以及定期更换密码的特点。但是也能满足一般的翻墙需求。

本工具就是使用脚本爬取免费shadowsocks账号网站的信息，自动导入到shadowsocks客户端中，实现翻墙上网的目的，

### 用到的网站

- get.ishadowx.biz
- 2020-01-22 亲测可用


## 使用方法

```html
以下提供的方式，可能只是很多可行方案中的一种，比如你可以选择不用ShadowsocksX 客户端，而用SSX-NG等。原理上都是一样，但是因这些未能一一测试，所以不保证一定可用正常工作。

本文在 macOS上测试，关于Windows上的使用，请自行搜索相应版本。
```

1. 安装 ShadowsocksX 客户端

[下载地址 1](http://160.16.231.71/ssx-2.6.3.dmg)

[下载地址 2](https://github.com/shadowsocks/shadowsocks-iOS/releases/download/2.6.3/ShadowsocksX-2.6.3.dmg)

2. 打开终端，clone或者下载本repo的代码。

```shell
git clone https://github.com/jiji262/SSAccount_Spider.git
```

3. 终端内运行爬虫

```shell
cd SSAccount_Spider
python Spider.js
```

`python Spider.js` 即是用于爬取免费的代理列表的命令。运行之后会生成几个文件:

```
ss_cfg.json
shadowsocks.xml
shadowsocks.plist
```
这些都是为了之后使用ShadowsocksX 客户端准备的，目前不用关心这几个文件的用途。

需要注意的是，爬虫脚本需要依赖`bs4`,因此在运行之前需要先安装`bs4`：
```
pip install bs4
```

4. 启动 ShadowsocksX 客户端

同样在`SSAccount_Spider`目录下运行`./run.sh`即可启动ShadowsocksX 客户端，如果弹出系统安全提示，请选「允许」。
启动之后会在系统状态栏上看到一个Shadowsocks的图标，点击"Turn Shadowsocks On"即可激活PAC，就是设置了全局代理。
启动之后点击Shadowsocks这个图标，如果看到处于`Shadowsocks Off`的状态（如下图），这个并不是说明Shadowsocks没有打开，只是说明PAC关闭状态。

![](images/1.png =250x)

推荐的使用的方式是，

- 保持ShadowsocksX 客户端的`Shadowsocks: Off`状态
- 保持`Auto Proxy Mode`
- Chrome浏览器使用扩展程序 SwitchySharp或者 VPN.S HTTP Proxy设置代理127.0.0.1:1080 上，代理类型为 SOCKS v5。如下图：

![](images/2.png =500x)

## 问题答疑

### 如何高效的使用ShadowsocksX 客户端

#### 基本使用

点击"Turn Shadowsocks On", Shadowsocks 会自动设置为全局 PAC 代理，Chrome、Safari、Twitter 都可以正常使用了。
如果你开启了其它翻墙工具，请先将它们关闭。如果你使用了 Chrome 扩展程序 SwitchySharp或者 VPN.S HTTP Proxy，请把它的模式设置为「使用系统代理设置」。

#### 高级使用

如果你不想用全局 PAC 代理，想配合 SwitchySharp 等插件使用，可在菜单栏图标里点`Shadowsocks: Off`。
关闭后代理仍会运行在 127.0.0.1:1080 上，代理类型为 SOCKS v5。
之所以不叫关闭 PAC，因为很多人不懂什么是 PAC。写关闭 Shadowsocks 更容易理解。

可以在菜单栏图标里配置和选择自定义服务器，之前的步骤就是把免费的服务器导入到这个列表中以便选择。

切换服务器后，因为 Chrome 保持长连接，可能需要重启浏览器才能生效。也可以重启 ShadowsocksX 来强制 Chrome 重新连接。

### 如何选择快速的免费代理

本项目中提供了一个脚本，可以在选择代理服务器之前，对爬取到的免费代理的速度做一个测试。

在运行`python Spider.js`成功之后，再去运行一下如下脚本：
```shell
./speed.sh
```
即可看到各个代理的速度情况，结果如下：
```
➜  SSAccount_Spider git:(master) ✗ ./speed.sh
total_server
->process 1/8
server:a.isxb.top avg_time:155.927

->process 2/8
server:b.isxb.top avg_time:169.606
......
```

### 如何看`python Spider.js`是否执行成功？

执行成功时，会在终端看到类似如下的结果：
```
➜  SSAccount_Spider git:(master) ✗ python Spider.py
IP->a.isxb.top
password->isx.yt-77741472
port->17931
method->aes-256-cfb
-------------
IP->b.isxb.top
password->isx.yt-72120068
port->10417
method->aes-256-cfb
-------------
IP->c.isxb.top
password->isx.yt-92387749
port->12610
method->aes-256-cfb
-------------
IP->a.isxc.top
password->isx.yt-91180431
port->11483
method->aes-256-cfb
-------------
IP->b.isxc.top
password->isx.yt-02598956
port->16474
method->aes-256-cfb
-------------
IP->c.isxc.top
password->isx.yt-01314631
port->14997
method->aes-256-cfb
-------------
IP->a.isxc.top
password->isx.yt-91180431
port->11483
method->aes-256-cfb
-------------
IP->c.isxb.top
password->isx.yt-92387749
port->12610
method->aes-256-cfb
-------------
{
    "current": 1,
    "profiles": [
        {
            "method": "aes-256-cfb",
            "password": "isx.yt-77741472",
            "remarks": "",
            "server": "a.isxb.top",
            "server_port": "17931"
        },
        {
            "method": "aes-256-cfb",
            "password": "isx.yt-72120068",
            "remarks": "",
            "server": "b.isxb.top",
            "server_port": "10417"
        },
        {
            "method": "aes-256-cfb",
            "password": "isx.yt-92387749",
            "remarks": "",
            "server": "c.isxb.top",
            "server_port": "12610"
        },
        {
            "method": "aes-256-cfb",
            "password": "isx.yt-91180431",
            "remarks": "",
            "server": "a.isxc.top",
            "server_port": "11483"
        },
        {
            "method": "aes-256-cfb",
            "password": "isx.yt-02598956",
            "remarks": "",
            "server": "b.isxc.top",
            "server_port": "16474"
        },
        {
            "method": "aes-256-cfb",
            "password": "isx.yt-01314631",
            "remarks": "",
            "server": "c.isxc.top",
            "server_port": "14997"
        },
        {
            "method": "aes-256-cfb",
            "password": "isx.yt-91180431",
            "remarks": "",
            "server": "a.isxc.top",
            "server_port": "11483"
        },
        {
            "method": "aes-256-cfb",
            "password": "isx.yt-92387749",
            "remarks": "",
            "server": "c.isxb.top",
            "server_port": "12610"
        }
    ]
}
ewogICAgImN1cnJlbnQiOiAxLAogICAgInByb2ZpbGVzIjogWwogICAgICAgIHsKICAgICAgICAgICAgIm1ldGhvZCI6ICJhZXMtMjU2LWNmYiIsCiAgICAgICAgICAgICJwYXNzd29yZCI6ICJpc3gueXQtNzc3NDE0NzIiLAogICAgICAgICAgICAicmVtYXJrcyI6ICIiLAogICAgICAgICAgICAic2VydmVyIjogImEuaXN4Yi50b3AiLAogICAgICAgICAgICAic2VydmVyX3BvcnQiOiAiMTc5MzEiCiAgICAgICAgfSwKICAgICAgICB7CiAgICAgICAgICAgICJtZXRob2QiOiAiYWVzLTI1Ni1jZmIiLAogICAgICAgICAgICAicGFzc3dvcmQiOiAiaXN4Lnl0LTcyMTIwMDY4IiwKICAgICAgICAgICAgInJlbWFya3MiOiAiIiwKICAgICAgICAgICAgInNlcnZlciI6ICJiLmlzeGIudG9wIiwKICAgICAgICAgICAgInNlcnZlcl9wb3J0IjogIjEwNDE3IgogICAgICAgIH0sCiAgICAgICAgewogICAgICAgICAgICAibWV0aG9kIjogImFlcy0yNTYtY2ZiIiwKICAgICAgICAgICAgInBhc3N3b3JkIjogImlzeC55dC05MjM4Nzc0OSIsCiAgICAgICAgICAgICJyZW1hcmtzIjogIiIsCiAgICAgICAgICAgICJzZXJ2ZXIiOiAiYy5pc3hiLnRvcCIsCiAgICAgICAgICAgICJzZXJ2ZXJfcG9ydCI6ICIxMjYxMCIKICAgICAgICB9LAogICAgICAgIHsKICAgICAgICAgICAgIm1ldGhvZCI6ICJhZXMtMjU2LWNmYiIsCiAgICAgICAgICAgICJwYXNzd29yZCI6ICJpc3gueXQtOTExODA0MzEiLAogICAgICAgICAgICAicmVtYXJrcyI6ICIiLAogICAgICAgICAgICAic2VydmVyIjogImEuaXN4Yy50b3AiLAogICAgICAgICAgICAic2VydmVyX3BvcnQiOiAiMTE0ODMiCiAgICAgICAgfSwKICAgICAgICB7CiAgICAgICAgICAgICJtZXRob2QiOiAiYWVzLTI1Ni1jZmIiLAogICAgICAgICAgICAicGFzc3dvcmQiOiAiaXN4Lnl0LTAyNTk4OTU2IiwKICAgICAgICAgICAgInJlbWFya3MiOiAiIiwKICAgICAgICAgICAgInNlcnZlciI6ICJiLmlzeGMudG9wIiwKICAgICAgICAgICAgInNlcnZlcl9wb3J0IjogIjE2NDc0IgogICAgICAgIH0sCiAgICAgICAgewogICAgICAgICAgICAibWV0aG9kIjogImFlcy0yNTYtY2ZiIiwKICAgICAgICAgICAgInBhc3N3b3JkIjogImlzeC55dC0wMTMxNDYzMSIsCiAgICAgICAgICAgICJyZW1hcmtzIjogIiIsCiAgICAgICAgICAgICJzZXJ2ZXIiOiAiYy5pc3hjLnRvcCIsCiAgICAgICAgICAgICJzZXJ2ZXJfcG9ydCI6ICIxNDk5NyIKICAgICAgICB9LAogICAgICAgIHsKICAgICAgICAgICAgIm1ldGhvZCI6ICJhZXMtMjU2LWNmYiIsCiAgICAgICAgICAgICJwYXNzd29yZCI6ICJpc3gueXQtOTExODA0MzEiLAogICAgICAgICAgICAicmVtYXJrcyI6ICIiLAogICAgICAgICAgICAic2VydmVyIjogImEuaXN4Yy50b3AiLAogICAgICAgICAgICAic2VydmVyX3BvcnQiOiAiMTE0ODMiCiAgICAgICAgfSwKICAgICAgICB7CiAgICAgICAgICAgICJtZXRob2QiOiAiYWVzLTI1Ni1jZmIiLAogICAgICAgICAgICAicGFzc3dvcmQiOiAiaXN4Lnl0LTkyMzg3NzQ5IiwKICAgICAgICAgICAgInJlbWFya3MiOiAiIiwKICAgICAgICAgICAgInNlcnZlciI6ICJjLmlzeGIudG9wIiwKICAgICAgICAgICAgInNlcnZlcl9wb3J0IjogIjEyNjEwIgogICAgICAgIH0KICAgIF0KfQ==
<DOM Text node "u'\n\teyJjdXJy'...">
➜  SSAccount_Spider git:(master) ✗
```

并生成新的`ss_cfg.json`文件。


## References

https://facaiy.com/misc/2017/06/24/shadowsocks_android_import_ss_links.html
https://github.com/jameslongyoung/SSAccount_Spider
https://github.com/zinbers/shadowsocks_profiles
http://zinbers.github.io/2016/09/28/shadowsocks/
