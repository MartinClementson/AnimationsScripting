import pymel.core as pm
import pymel.core.datatypes as dt


# pymel.core.datatypes.inv <--- for inverse matrix. inv(m) returns inverse of m

#print pm.datatypes.EulerRotation(hej) <---- from matrix to euler rotation
def printChildren(parent,level):
    
    for c in parent.getChildren():
        print c
        getRotationFromJoint(c)
        #print level* " " + c
        #printChildren(c,level+1)
        
def transferOneJoint(src,dest):
    firstFrame = pm.findKeyframe(src, which ='first')
    lastFrame = 20 #pm.findKeyframe(src, which = 'last')
    current = firstFrame
    pm.setCurrentTime(current)
    frames = 0
    if hasParent(src):
        srcRootNode = src.getParent(-1)
    else:
        srcRootNode = src
    
    srcRootRotation = srcRootNode.getRotation().asMatrix()
        
    if hasParent(dest):
        destRootNode = dest.getParent(-1) 
    else:
        destRootNode = dest
        
        
    destRootRotation = destRootNode.getRotation().asMatrix()        
    
    hierarcyMatrix = gethierarchyMatrix(src)
    
    while current <= lastFrame:

        frames += 1
        
        print current
        
    
        pm.setCurrentTime(current)
         
        srcRotation = getRotationFromJoint(src,hierarcyMatrix) 
        
        # Rotation is extracted from the joint
    
        #Now it needs to be transformed into standard coordinate space.
        #this is achieved by doing a change of basis.     
        # inv(srcRoot) * srcRotation * destination root
        srcRotation = srcRootRotation.inverse() * srcRotation * destRootRotation
        
        print srcRotation
        setRotationToJoint(srcRotation,dest)            

        #dest.rotate.setKey()
        
        if current == lastFrame:
            break
    
        current = pm.findKeyframe(src , time = current, which='next')
    
    
    
def gethierarchyMatrix(node):
    
    parents = node.getAllParents()
    parents.reverse()
    matrix = dt.Matrix()
    matrix = matrix.setToIdentity()
    for pNode in parents:
        matrix = matrix * getTposeFromJoint(pNode)
    
    matrix = matrix * node.getRotation().asMatrix()
    return matrix 
    
def transferAnimation(sourceRoot,destinationRoot):
    
    print "HEJHEJHEJ"
    #print test.__len__()
   
    print sourceRoot.getAllParents().__len__()
    
    for Sc,Dc in zip(sourceRoot.getChildren(),destinationRoot.getChildren()):
        
        print Sc
        firstFrame = pm.findKeyframe(Sc, which ='first')
        lastFrame = pm.findKeyframe(Sc, which = 'last')
        current = firstFrame
        pm.setCurrentTime(current)
        frames = 0
        #hierarcyMatrix = 
        while current <= lastFrame:
            frames += 1
            print current
            
            
            current = pm.findKeyframe(Sc , time = current, which='next')
            pm.setCurrentTime(current)
            
            srcRotation = getRotationFromJoint(Sc) 
            setRotationToJoint(srcRotation,Dc)            
            Dc.rotate.setKey()
            if current == lastFrame:
                break
        print "NUMBER OF ANIMATIONFRAMES:" + str(frames)
            #print Sc
            #print Dc
            
        #transferAnimation(Sc, Dc)
        
        #srcRotation = getRotationFromJoint(sc)
        
        #sourceRot = getRotationFromJoint(Sc)
        #destinationRot.setRotation(sourceRot)
        
    



def getTposeFromJoint(joint):
    
    rotation = joint.getRotation()
    rotation = rotation.asMatrix()
    print joint.rotate.get();
    return rotation
    
def getRotationFromJoint(joint, hierarchyMatrix):
    
    rotation = joint.getRotation()
    rotation = rotation.asMatrix()
    
    invMatrix  = hierarchyMatrix.inverse()
    rotation = invMatrix * (hierarchyMatrix * rotation)
   
    
    
    return rotation
    
def setRotationToJoint(rotation,destination):
    pass