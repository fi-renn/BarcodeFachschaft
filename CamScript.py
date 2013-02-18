#!/usr/bin/python

import Item
import Gui
import Map
import zbar
import time

#Konstanten
PREVIEW_WINDOW = True


def procHandler(proc, image, closure):
	'handler um ergebnisse zu verarbeiten'
	for symbol in image.symbols:
		#debug
		print symbol.data
		#/debug
		KioskGui.instance.fillData(symbol.data)

#main
if __name__ =="__main__":
	#createHashMap
	map = Map.createHashMap()
	#createGui
	window = Gui.createGui(map)
	
	# init zbarCam
	#siehe beispiel in zbar
	proc = zbar.Processor()
	proc.parse_config('enable')
	device = '/dev/video1'
	proc.init(device)
	proc.set_data_handler(procHandler)
	
	#preview window
	proc.visible = False
	proc.active = True
	#if(PREVIEW_WINDOW):
	if(False):
		try:
			# keep scanning until user provides key/mouse input
			proc.user_wait()
		except zbar.WindowClosed, e:
			pass
		quit()
	else:
		#ich weiss sau haesllich aber mir faellt nichts besseres ein
		while(True):
			#print "bin in endlosSchleife"
			proc.process_one()
			#time.sleep(5)
	
	
	
	
	
	

