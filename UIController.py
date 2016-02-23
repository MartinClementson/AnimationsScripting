

from maya import OpenMayaUI as omui
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from shiboken import wrapInstance
from sys import path as pythonPath
import pymel.core.modeling as md
import pymel.core as pm
from thread import start_new_thread
from thread import exit
pythonPath.insert(0,'//storage10.student.bth.se/students/20142/maik14/AnimationsScripting/')

import time

try:
    reload(transfer)
    
except Exception, e:
    print e  
    import MocapScript as transfer   

	
    
def testThread(selection,currentJoint):
    on = True
    while on:
	
	checkJoint = pm.ls(sl = True, type = 'joint')
	
	if checkJoint:
	    
	    if checkJoint != currentJoint:
		
	        currentJoint = checkJoint[0]
	        on = False
	    
		
	
        print "hej"
	time.sleep(2)



class myUIController(QObject):
    
    def __init__(self, ui):
        
        Obj = QObject.__init__(self)
	
	Obj = QObject
	#Obj = QObject.thread(self)
	
        self.ui = ui
        
        self.ui.show()
	
	
	self.windowActive = True
	
	#TransferButton
	ui.transferButton.clicked.connect(self.transferButtonClicked)
        
	
        #Left Buttons
        ui.leftUpButton.clicked.connect(self.leftUpButtonClicked)
        ui.leftDownButton.clicked.connect(self.leftDownButtonClicked)
	ui.leftDeleteButton.clicked.connect(self.leftDeleteButtonClicked)
	
	#Right Buttons
	ui.rightUpButton.clicked.connect(self.rightUpButtonClicked)
	ui.rightDownButton.clicked.connect(self.rightDownButtonClicked)
	ui.rightDeleteButton.clicked.connect(self.rightDeleteButtonClicked)	
	
	
	#Left list
	
	shapes = ['Square','Triangle','Arrow','Circle']
	ui.SourceList.clear()
	ui.SourceList.addItems(shapes)
	ui.SourceList.setCurrentRow(0)
	#ui.selectedShape.setText('Square')
	#i.selectedShape.displayText()	
	
	ui.SourceList.itemSelectionChanged.connect(self.SourcelistItemChanged)
	
	
	#Right list
	
	ui.TargetList.clear()
	ui.TargetList.addItems(shapes)
	ui.TargetList.setCurrentRow(0)
	#ui.selectedShape.setText('Square')
	#i.selectedShape.displayText()	
	
	ui.TargetList.itemSelectionChanged.connect(self.TargetlistItemChanged)    
	
	
	
	
       
        self.jointSel = pm.ls(sl = True, type = 'joint')
	#self.thread = start_new_thread(testThread,(self.ui,self.jointSel[0]))
	
	#try:
          #  ui.jointLabel.setText(str(self.jointSel[0]))
	#except Exception, e:
	  #  ui.jointLabel.setText("None")
        
	
       # ui.image.setPixmap(self.ui.path + "\icons\Square.jpg")
        #ui.expMat.stateChanged.connect(self.expMatChanged)
	#print ui.QMouseEvent
	#self.mousePressEvent(obj)
	#self.obj.event()
	#mouseFilter = print("HEJ")
	#ui.installEventFilter(mouseFilter)
	
	
    def showUI(self):
        self.ui.show()
	self.windowActive = True
	start_new_thread(testThread,(self.windowActive))

    def hideUI(self):
	self.windowActive = False
        self.ui.close()
	
    def test(self):
	print "Threading!"

    
    
    def mousePressEvent(self, event):
		# Panning
	if event.event():
	    print "mousePress ok!"
	     
	
	
  	
	  
	
    def leftUpButtonClicked(self):
	print "Left UP"
	#self.windowActive = False
	#self.ui.close()
    
    def leftDownButtonClicked(self):
	print "Left DOWN"
	
	
    def leftDeleteButtonClicked(self):
	toDelete = self.ui.SourceList.selectedItems()
		
	self.ui.SourceList.takeItem(self.ui.SourceList.row(toDelete[0]))	
	print "Left Delete"
	



    def rightUpButtonClicked(self):
	print "right UP"
	#self.windowActive = False
	#self.ui.close()
    
    def rightDownButtonClicked(self):
	
	print "right DOWN"
	
	
    def rightDeleteButtonClicked(self):
	
	toDelete = self.ui.TargetList.selectedItems()
	
	self.ui.TargetList.takeItem(self.ui.TargetList.row(toDelete[0]))
	print "right Delete"
	
	
		
    def transferButtonClicked(self):
	print "Transferring"
	
		
	    
	    
	   
	
	#curvez.setRotation(joint._getRotation('transform'),'transform')
	print 'create button is clicked'
	
    def parentButtonClicked(self):
	print 'parent button is clicked'
	
		
    def SourcelistItemChanged(self):
	print "source list item changed"
	
    def TargetlistItemChanged(self):
	print "Target list item changed"
	
            




