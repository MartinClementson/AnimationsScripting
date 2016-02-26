import pymel.core as pm
import time

import sys

sys.path.insert(0,'//storage10.student.bth.se/students/20142/maik14/AnimationsScripting/')
#sys.path.insert(0,'C:/Users/Martin/Desktop/AnimationsScripting/')


try:
    reload(tf)
except:
    import transferFunctions as tf

    
#src = ['iPi:Hip', 'iPi:LThigh', 'iPi:LShin', 'iPi:LFoot', 'iPi:LToe', 'iPi:LToeEnd', 'iPi:RThigh', 'iPi:RShin', 'iPi:RFoot', 'iPi:RToe', 'iPi:RToeEnd', 'iPi:LowerSpine', 'iPi:MiddleSpine', 'iPi:Chest', 'iPi:LClavicle', 'iPi:LShoulder', 'iPi:LForearm', 'iPi:LHand', 'iPi:LHandEnd', 'iPi:RClavicle', 'iPi:RShoulder', 'iPi:RForearm', 'iPi:RHand', 'iPi:RHandEnd', 'iPi:Neck', 'iPi:Head', 'iPi:HeadEnd']
#src = pm.PyNode('iPi:Hip')
#src = pm.PyNode('iPi:RThigh')
#src = pm.PyNode('iPi:RShin')
#src = pm.PyNode('iPi:RFoot')


#src = pm.PyNode('iPi:LThigh')
#src = pm.PyNode('iPi:LShin')
#dest = ['HIKCharacterNode1_Hips', 'HIKCharacterNode1_LeftUpLeg', 'HIKCharacterNode1_LeftLeg', 'HIKCharacterNode1_LeftFoot', 'HIKCharacterNode1_LeftFootMiddle1', 'HIKCharacterNode1_LeftFootMiddle2', 'HIKCharacterNode1_RightUpLeg', 'HIKCharacterNode1_RightLeg', 'HIKCharacterNode1_RightFoot', 'HIKCharacterNode1_RightFootMiddle1', 'HIKCharacterNode1_RightFootMiddle2', 'HIKCharacterNode1_Spine', 'HIKCharacterNode1_Spine1', 'HIKCharacterNode1_Spine2', 'HIKCharacterNode1_LeftShoulder', 'HIKCharacterNode1_LeftArm', 'HIKCharacterNode1_LeftForeArm', 'HIKCharacterNode1_LeftHand', 'HIKCharacterNode1_LeftFingerBase', 'HIKCharacterNode1_RightShoulder', 'HIKCharacterNode1_RightArm', 'HIKCharacterNode1_RightForeArm', 'HIKCharacterNode1_RightHand', 'HIKCharacterNode1_RightFingerBase', 'HIKCharacterNode1_Neck', 'HIKCharacterNode1_Neck1', 'HIKCharacterNode1_Head']

#destRoot = pm.PyNode('HIKCharacterNode1_Hips')
#destRoot = pm.PyNode('HIKCharacterNode1_RightUpLeg')
#destRoot = pm.PyNode('HIKCharacterNode1_RightLeg')
#destRoot = pm.PyNode('HIKCharacterNode1_RightFoot')

#destRoot = pm.PyNode('HIKCharacterNode1_LeftUpLeg')
#destRoot = pm.PyNode('HIKCharacterNode1_LeftLeg')
print "MOCAP SCRIPT LOADED!!"
#hej = tf.printChildren(src, 0)
#tf.transferAnimation(src, dest)
#print "TOTAL AMOUNT OF Joints : " + str(hej)
#tf.transferOneJoint(src, destRoot)
#tf.transferAnimation(root,destRoot)


#printChildren(root, 0)




    
    
    