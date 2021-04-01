#!/bin/bash
apt install python3
pip3 install colorama
pip3 install requests
chmod 777 $PREFIX/bin/vk-stalker
cp ./stalker.py $PREFIX/bin/vk-stalker
