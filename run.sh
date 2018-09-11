#!/bin/bash

version=1.0.1
function killShadowsocksX(){
    ss_process=`ps aux | grep "ShadowsocksX$" | grep -v "grep"`
    if [ "$ss_process" ]; then
        pid=`echo "$ss_process" | awk '{print $2}'`
        if [ -z "$pid" ]; then
            echo "kill shadowsocks process failed, please restart ShadowsocksX manually!"
        else
            kill -9 "$pid"
        fi
    fi
}

function restartShadowsocksX(){
    ss_app_path="/Applications/ShadowsocksX.app"
    if [ -d "$ss_app_path" ]; then
        open "$ss_app_path"
        echo "restart ShadowSocksX success."
    fi
}

plutil -convert binary1 shadowsocks.xml -o shadowsocks.plist
defaults import clowwindy.ShadowsocksX shadowsocks.plist

killShadowsocksX
restartShadowsocksX
