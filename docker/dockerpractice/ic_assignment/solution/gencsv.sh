#!/bin/bash
#This script will create a list of random number with index number prefix and creates a file named "inputFile" with the file permisson 644.
#by default it generates 10 enteries and with argument it can generate n number of entries.

#remove any file with the name inputFile first
rm -rf inputFile

#generate random number to ran_num variable
ran_num=$$

#generate random numbers with index 10 or n enties to inputFile
num=0
arg1=${1:-10}
while [[ ${num} -le ${arg1} ]]
do
	echo $num, $ran_num >> inputFile
(( num = num + 1 ))
done

#change the file permission to 644
chmod 644 inputFile

#print the file content on the terminal upon the completion
cat inputFile

