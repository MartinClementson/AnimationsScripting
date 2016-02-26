import sys

import pymel.core as pm
import time

#sys.path.insert(0,'//storage10.student.bth.se/students/20142/maik14/AnimationsScripting/')
sys.path.insert(0,'C:/Users/Martin/Desktop/AnimationsScripting/')


import loadXMLUI
try:
    muic = reload(muic)
except:
		
	import UIController as muic



gui = loadXMLUI.loadUI("transferUI.ui")




controllerz = muic.myUIController(gui)
controllerz.ui.show()
controllerz.__del__()
    
print controllerz
del controllerz
controllerz.ui.show()
controllerz.hideUI()