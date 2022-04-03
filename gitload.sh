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
echo "added the changes to commit"
sudo git commit -m "$mesg :by libin"
echo "commited the changes with the message: "$mesg""
sudo git push origin
echo "pushed the changes to the remote server"
\n
echo "re-checking the status"
git status
