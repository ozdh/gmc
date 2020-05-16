#!/bin/bash
echo "STARTING SCRIPT"
while :
do
	if ps aux | grep "/c/Program Files/Python37/python"
	then
		date
	else
		echo "Not Running, Starting"
		date
		python pythonbot.py &
	fi
	sleep 180
done
