#!/bin/bash
# Installation Script - tested on an ubuntu/trusty64 vagrant box

# Show all commands being run
#set -x

# Error out if one fails
set -e
BASE_DIR=$(dirname ${BASH_SOURCE[0]})
apt-get update
apt-get install --fix-missing
apt-get install -y swig swig3.0 libssl-dev python-dev libjpeg-dev xvfb

# Install pip and install pytnon requirements through it
apt-get install -y python-pip
pip install -r $BASE_DIR/requirements.txt

wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
tar xzvf geckodriver-v0.23.0-linux64.tar.gz
mv geckodriver /usr/bin/geckodriver

mkdir -p $BASE_DIR/logs/inbound/
cp -f $BASE_DIR/httpscreenshot.service /lib/systemd/system/

while getopts ":enable_service" opt; do
    case $opt in
        a)
            echo "enabling service was triggered!" >&2
            systemctl daemon-reload
            systemctl enable httpscreenshot.service
            systemctl restart httpscreenshot.service
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            ;;
    esac
done
