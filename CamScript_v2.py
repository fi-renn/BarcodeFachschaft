#!/usr/bin/python

import Item
import Gui
import Map
import os
import time


#main
if __name__ =="__main__":
	#createHashMap
	map = Map.createHashMap()
	#createGui
	window = Gui.createGui(map)
	
	p=os.popen('/usr/bin/zbarcam /dev/video0','r')
	while True:
		code = p.readline()
		print code
		window.fillData(code)

