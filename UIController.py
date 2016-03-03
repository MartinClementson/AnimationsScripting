

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
#pythonPath.insert(0,'//storage10.student.bth.se/students/20142/maik14/AnimationsScripting/')
pythonPath.insert(0,'C:/Users/Martin/Desktop/AnimationsScripting/')
import time

try:
    reload(transfer)

except Exception, e:
    print e  
    import transferFunctions as transfer   



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

        #Obj = QObject
        #Obj = QObject.thread(self)
        print Obj
        self.ui = ui


        #self.deleteLater()
        #self.ui.setWindowFlags(Qt.Window)

        #TransferButton
        #ui.transferButton.setEnabled(False)
        ui.transferButton.clicked.connect(self.transferButtonClicked)
        
        #warning message
        ui.warningLabel.setText(' ')

        #ui.warningLabel.setText('There is not an even number of joints')
        
        #Left Buttons
        ui.leftUpButton.clicked.connect(self.leftUpButtonClicked)
        ui.leftDownButton.clicked.connect(self.leftDownButtonClicked)
        ui.leftDeleteButton.clicked.connect(self.leftDeleteButtonClicked)
        ui.leftLoadButton.clicked.connect(self.loadSourceJoints)
        ui.SourceRootJoint.returnPressed.connect(self.loadSourceJointsFromString)
        
       

        #Right Buttons
        ui.rightUpButton.clicked.connect(self.rightUpButtonClicked)
        ui.rightDownButton.clicked.connect(self.rightDownButtonClicked)
        ui.rightDeleteButton.clicked.connect(self.rightDeleteButtonClicked)
        ui.rightLoadButton.clicked.connect(self.loadTargetJoints)
        ui.TargetRootJoint.returnPressed.connect(self.loadTargetJointsFromString)


        #Left list

        shapes = ['Square','Triangle','Arrow','Circle']
        ui.SourceList.clear()
        ui.SourceList.addItems(shapes)
        ui.SourceList.setCurrentRow(0)
        
        #ui.SourceRootJoint.keyPressEvent()
        
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

        self.windowActive = True
        self.ui.show() 


    #def __del__(self):
      #  del self.ui
      #  del self
      
    def showUI(self):
        self.ui.show()
        self.windowActive = True
        #start_new_thread(testThread,(self.windowActive))

    def hideUI(self):
        self.windowActive = False
        self.ui.close()
        del self

    def test(self):
        print "Threading!"



    def mousePressEvent(self, event):
                # Panning
        if event.event():
            print "mousePress ok!"
    
    def loadSourceJoints(self):
        self.loadJoints(self.ui.SourceList)
        self.ui.L_jointAmount.setText(str(self.ui.SourceList.count()))
        self.compareJointCount()
        self.ui.SourceList.setCurrentRow(0)
    
    def loadSourceJointsFromString(self):
        #print "LOAD FROM STRING"
        stringToLoad = self.ui.SourceRootJoint.text()
        self.loadJointsFromString(self.ui.SourceList,stringToLoad)
        self.ui.L_jointAmount.setText(str(self.ui.SourceList.count()))
        self.compareJointCount()
        self.ui.SourceList.setCurrentRow(0)        
        
    
    def loadTargetJointsFromString(self):
        stringToLoad = self.ui.TargetRootJoint.text()
        self.loadJointsFromString(self.ui.TargetList,stringToLoad)
        self.ui.R_jointAmount.setText(str(self.ui.TargetList.count()))
        self.compareJointCount()
        self.ui.TargetList.setCurrentRow(0)        
    
    def loadTargetJoints(self):
        self.loadJoints(self.ui.TargetList)
        self.ui.R_jointAmount.setText(str(self.ui.TargetList.count()))
        self.compareJointCount()
        self.ui.TargetList.setCurrentRow(0)
            
    def loadJoints(self, listWidget):
        print "LOAD JOINTS CAPN!"
        listWidget.clear()
        root = pm.ls(sl = True, type = 'joint')
        relatives = root[0].listRelatives(ad = True) #ad =all decendants
        relatives.reverse()
        
        listItems = [str(root[0])]
        for each_joint in relatives:
            listItems.append(str(each_joint))
        listWidget.addItems(listItems)
    
    
    def loadJointsFromString(self,listWidget,string):
        
        
        
        try:
            root = pm.PyNode(string)
            listWidget.clear()
            relatives = root.listRelatives(ad = True) #ad =all decendants
            relatives.reverse()
            
            listItems = [str(root)]
            for each_joint in relatives:
                listItems.append(str(each_joint))
            listWidget.addItems(listItems) 
        except:
            print "No match found"
        


    def leftUpButtonClicked(self):
        print "Left UP"
        self.moveListItemUp(self.ui.SourceList)
        
     

    def leftDownButtonClicked(self):
        print "Left DOWN"
        self.moveListItemDown(self.ui.SourceList)
        


    def leftDeleteButtonClicked(self):
        if self.ui.SourceList.count():
            
            toDelete = self.ui.SourceList.selectedItems()

            self.ui.SourceList.takeItem(self.ui.SourceList.row(toDelete[0]))	
            print "Left Delete"
            self.compareJointCount()
            self.ui.L_jointAmount.setText(str(self.ui.SourceList.count()))
        else:
            print "There is nothing to delete"




    def rightUpButtonClicked(self):
        self.moveListItemUp(self.ui.TargetList)
        print "right UP"
        

    def rightDownButtonClicked(self):
        self.moveListItemDown(self.ui.TargetList)

        print "right DOWN"


    def rightDeleteButtonClicked(self):
        if self.ui.TargetList.count():

            toDelete = self.ui.TargetList.selectedItems()

            self.ui.TargetList.takeItem(self.ui.TargetList.row(toDelete[0]))
            self.compareJointCount()
            self.ui.R_jointAmount.setText(str(self.ui.TargetList.count()))
            print "right Delete"
        else:
            print"NOTHING TO DELETE"




    def transferButtonClicked(self):
        
        loop = self.ui.SourceList.count()
        
        source = []
        dest = []
        
        for x in range(loop):
            source.append(str(self.ui.SourceList.item(x).text()))
            dest.append(str(self.ui.TargetList.item(x).text()))
            
            #print str(temp.text())
        
        transfer.transferAnimation(source, dest)


 


    def SourcelistItemChanged(self):
        print "source list item changed"

    def TargetlistItemChanged(self):
        print "Target list item changed"
        
        
        
    def moveListItemUp(self,listWidget):
        print "Left UP"
        if listWidget.currentRow() > 0:
            
            if listWidget.currentRow() == (listWidget.count() -1): #If it's the one furthest down, do this 
                
                itemToMove = listWidget.takeItem(listWidget.currentRow())
                                
                #self.ui.SourceList.setCurrentRow((self.ui.SourceList.currentRow() -1))
                listWidget.insertItem((listWidget.currentRow()),itemToMove)
                listWidget.setCurrentRow((listWidget.currentRow() -1))
                print "moving bottom up"
                
                
            else:
                itemToMove = listWidget.takeItem(listWidget.currentRow())
                
                #self.ui.SourceList.setCurrentRow((self.ui.SourceList.currentRow() -1))
                listWidget.insertItem((listWidget.currentRow()-1),itemToMove)
                listWidget.setCurrentRow((listWidget.currentRow() -2))
                #self.windowActive = False
                #self.ui.close()
        else:
            print"You're at the top!"        
    
    def moveListItemDown(self,listWidget):
        if listWidget.currentRow() < (listWidget.count() -1):
                   
                     
            itemToMove = listWidget.takeItem(listWidget.currentRow())
                   
            listWidget.insertItem((listWidget.currentRow()+1),itemToMove)
            listWidget.setCurrentRow((listWidget.currentRow() +1))
                
        else:
            print "AT THE BOTTOM"
    
    
    def compareJointCount(self):
        
        if self.ui.SourceList.count() != self.ui.TargetList.count():
            
            self.ui.warningLabel.setText('There is not an even number of joints')
            self.ui.transferButton.setEnabled(False)
        else:
            self.ui.warningLabel.setText(' ')
            self.ui.transferButton.setEnabled(True)
            






