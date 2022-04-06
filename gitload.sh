#!/usr/bin/env bash
#this script is run the git command quick
#
#
#commi_detail=$1
#com_mesg= read "Enter commit meessage"
echo "Pulling the latest changes from the remote repository"
sudo git pull
echo "Enter commit message"

read mesg
#CHANGES=`git status | grep "Changes not staged for commit"`
#echo $CHANGES
#if [[CHANGES -eq "Changes not staged for commit" ]]; then	
#	sudo git add .
#	echo "added the changes to commit"
#	echo "Enter commit message"
#	read mesg
#	sudo git commit -m "$mesg :by libin"
#	echo "commited the changes with the message: "$mesg""
#	sudo git push origin
#	echo "pushed the changes to the remote server"
#	echo "re-checking the status"
#	git status
#else
#	echo "Nothing to commit - Aborting the script"
#fi


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
