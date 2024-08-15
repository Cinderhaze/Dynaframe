# Dynaframe
 A Dynamic Photo and Video Picture Frame script written in Python. It was created to provide a simple way to do not only slideshows on a raspberry pi connected to a monitor, but to also do videos for effects such as cinemagraphs or plotagraphs.  The initial version includes control via MQTT or HTTP, so that it can easily be controlled via home autoamtion or tablets/phones/computers remotely. 
 
 I've created a video of the project at: https://www.youtube.com/watch?v=2f92ypMnDEs&feature=youtu.be
 
 This is my first Python project, so feedback is much appreciated! 


--- Notes:

Create the mouse.sh script to move the mouse 'out of the way'
- be sure to sudo apt-get install xdotools to allow cli movement of the mouse
Use the launcher script to run dynaframe
use the autorestart configuration to call the above and use it instead of the typical Xsession
