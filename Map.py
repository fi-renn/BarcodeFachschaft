
from Item import KioskItem

def createHashMap():
	'baut die Preiliste auf und so, trag das Zeug hier ein'
	# hashmap von Barcode auf Object
	result = {}
	#suss
	result["EAN-13:4021700800000\n"] = KioskItem("Mr.Tom",0.30,210,879,True,True)
	result["EAN-8:40114606\n"] = KioskItem("KitKat",0.40,234,980,False,True)
	result["EAN-8:40144955\n"] = KioskItem("Mamba",0.20,103,430,True,True)
	result["EAN-8:40004617\n"] = KioskItem("Bifi Roll",0.80,230,950,False,False)
	result["EAN-13:4001242000601\n"] = KioskItem("Chip Chips Paprika",0.80,268,1120,True,True)
	result["EAN-8:40468709\n"] = KioskItem("Dextro Energy",0.90,170,722,True,True)
	result["EAN-8:40468273\n"] = KioskItem("Dextro Energy Vitamin C",0.90,170,722,True,True)
	result["EAN-13:5000159407236\n"] = KioskItem("Mars",0.50,228,912,False,True)
	result["EAN-13:4001686372234\n"] = KioskItem("Haribo Roulette",0.20,86,359,False,False)
	result["EAN-8:40358802\n"] = KioskItem("Knoppers",0.30,137,572,False,True)
	result["EAN-8:40111315\n"] = KioskItem("Twix",0.50,144,601,False,True)
	result["EAN-13:7613032625474\n"] = KioskItem("Lion",0.40,207,867,False,True)
	result["EAN-13:5000159020312\n"] = KioskItem("Malteser",0.50,184,772,False,True)
	result["EAN-13:7300400127387\n"] = KioskItem("Wasa Tomate 3er Pack",2.10,588,2454,False,True)
	result["EAN-13:7300400127448\n"] = KioskItem("Wasa Creme Cheese 3er Pack",2.10,450,1800,False,True)
	result["EAN-13:7300400122702\n"] = KioskItem("Wasa Chives 3er Pack",2.10,510,2160,False,True)
	result["EAN-8:40084077\n"] = KioskItem("Kinderriegel",0.30,118,493,False,True)
	result["EAN-13:5000159407397\n"] = KioskItem("Snickers",0.50,287,1148,False,True)
	
	
	#getraenke
	result["EAN-13:4029764001814\n"] = KioskItem("Club-Mate IceT",1.0,140,585,True,True)
	result["EAN-13:4029764001883\n"] = KioskItem("Club-Mate Cola",1.0,99,416,True,True)
	result["EAN-13:0061000005853\n"] = KioskItem("Club-Mate", 0.9, 100, 420, True, True)
	result["EAN-13:4029764001869\n"] = KioskItem("Club-Mate Winteredition",0.9,100,420,True,True)
	result["EAN-13:1094922076211\n"] = KioskItem("Hermann Brause Zitrone",0.90,122,515,True,True)
	result["EAN-13:1094922076228\n"] = KioskItem("Hermann Brause Orange",0.90,149,624,True,True)
	result["EAN-13:1094922076235\n"] = KioskItem("Hermann Brause Limette",0.90,139,584,True,True)
	result["EAN-13:4022652390397\n"] = KioskItem("Tausend Wasser naturelle",0.90,-1,-1,True,True)
	result["EAN-13:4022652530168\n"] = KioskItem("Aqua Siron classic",0.90,-1,-1,True,True)
	result["EAN-13:4018905327784\n"] = KioskItem("Eistee Pfirsich",0.60,155,650,True,True)
	result["EAN-13:4018905327807\n"] = KioskItem("Eistee Zitrone",0.60,155,660,True,True)
	result["EAN-13:4001513006905\n"] = KioskItem("Gerolsteiner Apfelschorle",1.20,188,795,True,True)
	result["EAN-13:4018905652343\n"] = KioskItem("Multivitamin 12 Frucht",0.70,45,185,True,True)
	result["EAN-13:4018905342329\n"] = KioskItem("Ace Vitamindrink",0.70,240,1015,True,True)
	result["EAN-13:4102430013684\n"] = KioskItem("Bitburger Radler",1.0,116,485,True,True)
	result["EAN-13:4102430015206\n"] = KioskItem("Bitburger Premium Pils",1.0,136,568,True,True)
	result["EAN-13:4000555100909\n"] = KioskItem("Kandi Malz",0.70,142,597,True,True)
	result["EAN-13:4060800160003\n"] = KioskItem("Rockstar Energy Drink",1.80,295,1255,True,True)
	result["EAN-8:90162565\n"] = KioskItem("Redbull Mist",1.30,113,480,True,True)
	result["EAN-13:109422076266\n"] = KioskItem("Hermann Kola",0.80,139,591,True,True)
	
	return result