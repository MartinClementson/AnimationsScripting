import pymel.core as pm
import time

import sys

sys.path.insert(0,'//storage10.student.bth.se/students/20142/maik14/AnimationsScripting/')


try:
    reload(tf)
except:
    import transferFunctions as tf

    

root = pm.PyNode('iPi:Hip')
destRoot = pm.PyNode('HIKCharacterNode1_Hips')

print "HEJ1"
tf.transferOneJoint(root, destRoot)
#tf.transferAnimation(root,destRoot)


#printChildren(root, 0)




    
    
    