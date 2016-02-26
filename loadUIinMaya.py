import sys

import pymel.core as pm
import time

sys.path.insert(0,'//storage10.student.bth.se/students/20142/maik14/AnimationsScripting/')
#sys.path.insert(0,'C:/Users/Martin/Desktop/AnimationsScripting/')


import loadXMLUI


gui = loadXMLUI.loadUI("transferUI.ui")
#iPi:Hip

try:
    muic = reload(muic)
except:
		
	import UIController as muic

controllerz = muic.myUIController(gui)


controllerz.ui.show()
controllerz.__del__()
gui.
print controllerz
del controllerz
controllerz.ui.show()
controllerz.hideUI()