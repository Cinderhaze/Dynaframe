#!/bin/bash
export DISPLAY=:0
#export DISPLAY=:0.0
while [ ! -e "/home/pi/Pictures/usb" ] ; 
do 
  echo "waiting on dir";
  sleep 1;
  
done;
echo "Waiting 5 sec to start"
sleep 5
#inotifywait -e create /home/pi/Pictures/usb/Pictures/
cd /home/pi/Pictures/usb/Pictures/
python3 /home/pi/git/Dynaframe/show.py
