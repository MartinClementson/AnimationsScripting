from maya import OpenMayaUI as omui
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from shiboken import wrapInstance
from sys import path as pythonPath

def getMayaWin():
    #obtain a reference to the maya window
    mayaWinPtr = omui.MQtUtil.mainWindow()
    mayaWin    = wrapInstance(long(mayaWinPtr), QWidget)

def loadUI(uiName):
    """Returns QWidget with the UI"""
    # object to load ui files
    loader = QUiLoader()
    # file name of the ui created in Qt Designer
    # directory name (we will update this until we find the file)
    dirIconShapes = ""
    # buffer to hold the XML we are going to load
    buff = None
    # search in each path of the interpreter
    for p in pythonPath:
        fname = p + '/' + uiName
        uiFile = QFile(fname)
        # if we find the "ui" file
        if uiFile.exists():
            # the directory where the UI file is
            dirIconShapes = p
            uiFile.open(QFile.ReadOnly)
            # create a temporary array so we can tweak the XML file
            buff = QByteArray( uiFile.readAll() )
            uiFile.close()
            # the filepath where the ui file is: p + uiname
            break
    else:
        print 'UI file not found'
    # fix XML
    fixXML(buff, p)
    qbuff = QBuffer()
    qbuff.open(QBuffer.ReadOnly|QBuffer.WriteOnly)
    qbuff.write(buff)
    qbuff.seek(0)
    ui = loader.load(qbuff, parentWidget = getMayaWin())
    ui.path = p
    return ui


def fixXML(qbyteArray, path):
    # first replace forward slashes for backslashes
    if path[-1] != '/':
        path = path + '/'
    path = path.replace("/","\\")
    
    # construct whole new path with <pixmap> at the begining
   # tempArr = QByteArray( "<pixmap>" + path + "\\")
    
    # search for the word <pixmap>
    #lastPos = qbyteArray.indexOf("<pixmap>", 0)
    #while ( lastPos != -1 ):
        #qbyteArray.replace(lastPos,len("<pixmap>"), tempArr)
        #lastPos = qbyteArray.indexOf("<pixmap>", lastPos+1)
    return 

            
    

# usage example from Maya window
##reload(loadXMLUI)
##from loadXMLUI import *
##UIController is loadXMLUI.UIController
##cont = UIController(loadUI('iconshapes.ui'))