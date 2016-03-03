import pymel.core as pm
import pymel.core.datatypes as dt


# pymel.core.datatypes.inv <--- for inverse matrix. inv(m) returns inverse of m

#print pm.datatypes.EulerRotation(hej) <---- from matrix to euler rotation
def printChildren(parent,level = 0):
    if level == 0:
        print parent 
    childs = 0
        
    level +=1
    
    for c in parent.getChildren():
        #print c
        #getRotationFromJoint(c)
      
        print level* " " + c 
        
        childs = childs + printChildren(c,level+1)
    
    
    return childs +1


def getRootNode(node):
    #This function finds the Joint that is highest in the hierarcy and returns that
    #This is used to check if we're transfering a root node. 
    # The root node will have a slightly different transfer, with it's translation included.
    rootNode = node
    rootFound = False
    print type(rootNode)
    while not rootFound:
        
        if not rootNode.getParent(): #make sure there is a parent.
            rootFound = True
        
        else:
            if rootNode.getParent() == 'HIKCharacterNode1_Reference': #ignore the refrence joint in the destination. The hip is the upper parent
                rootFound = True
                
            elif rootNode.getParent().nodeType() == 'joint': #check if the parent is a joint node
                rootNode = rootNode.getParent()
        
            else:
                rootFound = True
        
        
    return rootNode


def transferRootJoint(src,dest):
    
    #This function is used to transfer the root joint
    #We don't have to convert this into another space.
    #we just copy the rotation and translation over
    
    
    
    
    firstFrame = pm.findKeyframe(src, which ='first')
    lastFrame = pm.findKeyframe(src, which = 'last')
    current = firstFrame
    pm.setCurrentTime(current)
    
    while current <= lastFrame:
        
        pm.setCurrentTime(current)
        
        dest.setTranslation(src.getTranslation())
        dest.setRotation(src.getRotation())   
        dest.rotate.setKey()
        dest.translate.setKey()
                    
        if current == lastFrame:
            break
    
        current = pm.findKeyframe(src , time = current, which='next')
        
def transferOneJoint(src,dest):
    
    
    #get the upper most parent node of the source, If there is none it will return itself
    #This is done because we need the root node to to the change of basis
    srcRootNode = getRootNode(src)


    
 
    if srcRootNode == src:
        #this checks if the root node is being processed
        #then we need to include the translation
        #we have another function only for the root node transformation
        transferRootJoint(src,dest)
        print "THIS IS THE ROOTNODE"
    
    
    
    else: #do the normal transfer
        
        
        firstFrame = pm.findKeyframe(src, which ='first') #Find first key frame
        lastFrame = pm.findKeyframe(src, which = 'last')  #Find the lat key frame
        current = firstFrame 
        pm.setCurrentTime(current) #Set current key frame to the first one
        
        
        #get the rotation of the root in the first frame (IT's the bind pose)      Needed when changing basis 
        srcRootRotation = srcRootNode.getRotation().asMatrix()   
    
    
        #Get the bind pose of the destination joint. Needed when applying rotation to destination
        destRootRotation = dest.getRotation().asMatrix()            



        
        srcHierarcyMatrix = src.getRotation().asMatrix() 
        #This will be done on the first frame. 
        #A matrix of the hierarcys TPose will be returned
        #srcHierarchyMatrix is used to isolate the rotation from the source joint
        
        changeofBasisMatrix = getChangeOfBasisMatrix(src)
        #This creates the matrix that is needed when we change the basis of the orientation
        #it is similar to the hierarchyMatrix, However, it is multiplicated in the reverse order, and it does not include the source joint orientation
        
        
    
    
        # Loop through the frames
        while current <= lastFrame:
    
            
            
        
            pm.setCurrentTime(current)
             
            srcRotation = getRotationFromJoint(src,srcHierarcyMatrix) #Extract the Rotation from the source, using the hierarchy matrix
            
            # Rotation is extracted from the joint, 
        
            #Now it needs to be transformed into standard coordinate space.
            #this is achieved by doing a change of basis.     
            # inv(changeofBasisMatrix) * srcRotation * changeofBasisMatrix
            srcRotation = changeofBasisMatrix.inverse() * srcRotation * changeofBasisMatrix
            
            
            setRotationToJoint(srcRotation,dest,destRootRotation)            
    
            dest.rotate.setKey() #Set the keyframe!
            
            if current == lastFrame:
                break
        
            current = pm.findKeyframe(src , time = current, which='next') #Jump to next frame
            
            
       
def getChangeOfBasisMatrix(node):
    #this is similar to the function "getHierarchyMatrix()" <--- this was later removed
    #the difference is that we do not include the node's rotation in the end. we only want the parents rotations
    #also, we do the multiplication order the other way around, So we do not reverse the parents list
    #so it multiplies from the lowest children up
    
    parents = node.getAllParents()
    
    matrix = dt.Matrix()
    matrix = matrix.setToIdentity()
    
    for pNode in parents:
        if pNode.nodeType() == 'joint':
            
            matrix = matrix* getTposeFromJoint(pNode)
    return matrix


def transferAnimation(sourceRoot,destinationRoot):
    

    
    for Sc,Dc in zip(sourceRoot,destinationRoot):
        source = pm.PyNode(Sc)
        destination = pm.PyNode(Dc)
        
        transferOneJoint(source, destination)
        
    print "DONE"
        
     
        
       



def getTposeFromJoint(joint):
    
    rotation = joint.getRotation()
    rotation = rotation.asMatrix()
    
    return rotation
    
def getRotationFromJoint(joint, hierarchyMatrix):
    #to get the rotation from the joint.
    #we need to isolate the rotation
    #(thehierarchyMatrix)inversed * theHierarchyMatrix*rotation
    rotation = joint.getRotation()
    rotation = rotation.asMatrix()
    
    invMatrix  = hierarchyMatrix.inverse()
    rotation = invMatrix *  rotation
   
   #this rotation is now specified in the coordinates of the joint
   #later we will convert it into standard coordinate space
    
    return rotation
    
def setRotationToJoint(rotation,destination,matrix):
    
    finalRotation = matrix* rotation #matrix * rotation
    
    #convert it to euler rotation
    finalEuler = pm.datatypes.EulerRotation(finalRotation)
    
    destination.setRotation(finalEuler)
    