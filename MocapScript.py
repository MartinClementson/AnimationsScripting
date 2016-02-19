import pymel.core as pm
import time

import sys

sys.path.insert(0,'//storage10.student.bth.se/students/20142/maik14/AnimationsScripting/')


try:
    reload(tf)
except:
    import transferFunctions as tf

    

#src = pm.PyNode('iPi:Hip')
#src = pm.PyNode('iPi:RThigh')
src = pm.PyNode('iPi:RShin')
#src = pm.PyNode('iPi:RFoot')

#destRoot = pm.PyNode('HIKCharacterNode1_Hips')
#destRoot = pm.PyNode('HIKCharacterNode1_RightUpLeg')
destRoot = pm.PyNode('HIKCharacterNode1_RightLeg')
#destRoot = pm.PyNode('HIKCharacterNode1_RightFoot')

tf.transferOneJoint(src, destRoot)
#tf.transferAnimation(root,destRoot)


#printChildren(root, 0)




    
    
    