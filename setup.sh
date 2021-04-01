#!/bin/bash

apt install dos2unix
apt install python
pip3 install colorama
pip3 install requests
cp ./stalker.py $PREFIX/bin/vk-stalker
dos2unix $PREFIX/bin/vk-stalker
chmod 777 $PREFIX/bin/vk-stalker
