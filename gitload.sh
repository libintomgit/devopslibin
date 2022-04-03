#!/usr/bin/env bash
#
#
#
#commi_detail=$1
#com_mesg= read "Enter commit meessage"

echo "Enter commit message"
read mesg

sudo git status
sudo git add .
sudo git commit -m "$mesg"
sudo git push origin


