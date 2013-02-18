
import pygtk
pygtk.require('2.0')
import gtk
import pango
import fpformat
import time

from Item import KioskItem 

from thread import start_new_thread

#konstanten fuer gui
EURO_SYMBOL = u"\u20AC"
TIMESHOWN_INSECONDS=2

#konstanten fuer window
WINDOW_TITLE = "Ihr Produkt"
WINDOW_BORDER = 10
WINDOW_WITH = 300
WINDOW_HEIGHT = 200

#konstanten fuer nameLabel
NAMELABEL_SIZE = 20 * 1000

#konstanten fuer priceLabel
PRICELABEL_SIZE = 40 * 1000

#konstanten fuer kalcoLabel
CALORIESLABEL_SIZE = 15 * 1000

#konstanten fuer veggyLabel
VEGGYLABEL_SIZE = 15 * 1000

#konstanten fuer infoLabels
INFOLABEL_SIZE = 15 * 1000

class KisokGui:
	instance = 0
	#normales killen wenn fenster gekillt wird
	
	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		#close backend
		quit()

	def __init__(self,map):
		instance = self
		self.map = map
		#setze fehler anzeige
		self.map["err"] = KioskItem("Code unbekannt",13.37,9001,42,True,False)
		
		#common gui stuff
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title(WINDOW_TITLE)
		self.window.set_default_size(WINDOW_WITH,WINDOW_HEIGHT)
		self.window.connect("delete_event",self.delete_event)
		self.window.set_keep_below(True)
		#border
		self.window.set_border_width(10)
		#inhalt
		#nameLabel
		attrlist = pango.AttrList()
		attrlist.insert(pango.AttrSize(NAMELABEL_SIZE,0,-1))
		self.nameLabel = gtk.Label("name")
		self.nameLabel.set_attributes(attrlist)
		self.nameLabel.set_alignment(xalign=0.5, yalign=0.5)
		
		#priceLabel
		self.priceLabel = gtk.Label("0.00 "+EURO_SYMBOL)
		attrlist = pango.AttrList()
		attrlist.insert(pango.AttrSize(PRICELABEL_SIZE,0,-1))
		self.priceLabel.set_attributes(attrlist)
		self.priceLabel.set_alignment(xalign=0.5, yalign=0.5)
		
		#caloriesLabel
		self.caloriesLabel = gtk.Label("0 kcal/ 0 kJ")
		attrlist = pango.AttrList()
		attrlist.insert(pango.AttrSize(CALORIESLABEL_SIZE,0,-1))
		self.caloriesLabel.set_attributes(attrlist)
		self.caloriesLabel.set_alignment(xalign=1.0,yalign=0.5)
		
		#veggyLabel
		self.veggyLabel = gtk.Label("(ja/ja)")
		attrlist = pango.AttrList()
		attrlist.insert(pango.AttrSize(VEGGYLABEL_SIZE,0,-1))
		self.veggyLabel.set_attributes(attrlist)
		self.veggyLabel.set_alignment(xalign=1.0,yalign=0.5)
		
		#style
		table = gtk.Table(4,2)
		table.attach(self.nameLabel,0,2,0,1,)#nameLabel
		table.attach(self.priceLabel,0,2,1,2)#priceLabel
		table.attach(self.caloriesLabel,1,2,2,3)#caloriesLabel
		table.attach(self.veggyLabel,1,2,3,4)#veggyLabel
		
		
		attrlist = pango.AttrList()
		attrlist.insert(pango.AttrSize(INFOLABEL_SIZE,0,-1))
		calInfoLabel = gtk.Label("Energiegehalt:")
		calInfoLabel.set_attributes(attrlist)
		calInfoLabel.set_alignment(xalign=0.0,yalign=0.5)
		vegInfoLabel = gtk.Label("Vegan/Vegetarisch")
		vegInfoLabel.set_attributes(attrlist)
		vegInfoLabel.set_alignment(xalign=0.0, yalign=0.5)
		table.attach(calInfoLabel,0,1,2,3)
		table.attach(vegInfoLabel,0,1,3,4)
		
		self.window.add(table)
		
		#anzeige (show)
		self.nameLabel.show()
		self.priceLabel.show()
		self.caloriesLabel.show()
		self.veggyLabel.show()
		calInfoLabel.show()
		vegInfoLabel.show()
		
		table.show()
		
		self.window.show()
		
	def fillData(self,data):
		try:
			item = self.map[data]
		except KeyError:
			item = self.map["err"]
			
		self.nameLabel.set_label(item.name)
		self.priceLabel.set_label(fpformat.fix(item.price,2)+" "+EURO_SYMBOL)
		self.caloriesLabel.set_label("("+str(item.kcal)+" kcal / "+str(item.joul)+" kJ)")
		vegString = "("
		if(item.vegan):
			vegString+="ja/"
		else:
			vegString+="nein/"
			
		if(item.veggie):
			vegString+="ja)"
		else:
			vegString+="nein)"
		self.veggyLabel.set_label(vegString)
		
		#show window
		self.window.set_keep_below(False)
		self.window.set_keep_above(True)
		
		#sleep
		time.sleep(TIMESHOWN_INSECONDS)
		
		#hide window
		self.window.set_keep_above(False)
		self.window.set_keep_below(True)


def bumpThread():
	gtk.gdk.threads_init()
	gtk.main()

def createGui(map):
	window = KisokGui(map)
	start_new_thread(bumpThread,())
	
	return window
	

def killGui():
	gtk.quit()
	

if __name__ =="__main__":
	#test gui
	testMap = {}
	testCase = "test"
	testMap[testCase] = KioskItem("Frikadelle",2.50,100,200,False,False)
	window = createGui(testMap)
	time.sleep(2)
	window.fillData(testCase)
	fehler
	
	