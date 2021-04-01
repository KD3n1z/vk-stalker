#!/bin/bash
apt install python3
pip3 install colorama
pip3 install requests
chmod +x $PREFIX/bin/vk-stalker
cp ./stalker.py $PREFIX/bin/vk-stalker