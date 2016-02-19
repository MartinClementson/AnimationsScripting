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


def getRootNode(node):
    #This function finds the Joint that is highest in the hierarcy and returns that
    rootNode = node
    rootFound = False
    print type(rootNode)
    while not rootFound:
        
        if not rootNode.getParent(): #make sure there is a parent.
            rootFound = True
        
        else:
            if rootNode.getParent() == 'HIKCharacterNode1_Reference':
                rootFound = True
                
            elif rootNode.getParent().nodeType() == 'joint': #check if the parent is a joint node
                rootNode = rootNode.getParent()
        
            else:
                rootFound = True
        
        
    return rootNode
def transferRootJoint(src,dest):
    firstFrame = pm.findKeyframe(src, which ='first')
    lastFrame = 207 #pm.findKeyframe(src, which = 'last')
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
    
    
    #get the upper most parent node, If there is none it will return itself
    srcRootNode = getRootNode(src)
    print "The source node is : " + src
    print "The rootNODE of the source IS : " + srcRootNode 
    hej = False
    print "----------------------------------------"
    destRootNode = getRootNode(dest) 
    print "The destination node is : " + dest
    print "The rootNODE of the destination IS : " + destRootNode     
    
    if srcRootNode == src:
        #this checks if the root node is being processed
        #then we need to include the translation
        #we have another function only for the root node transformation
        transferRootJoint(src,dest)
        print "THIS IS THE ROOTNODE. IDIOT!"
    
    
    
    else:#lif hej: #do the normal transfer
        
        
        firstFrame = pm.findKeyframe(src, which ='first')
        lastFrame = 207 #pm.findKeyframe(src, which = 'last')
        current = firstFrame
        pm.setCurrentTime(current)
        frames = 0 
        
        #get the rotation of the root  (IT's the bind pose)      Needed when changing basis 
        srcRootRotation = srcRootNode.getRotation().asMatrix()   
    
        #Do the same for the destination joint    (get bind pose of root) Needed when applying rotation to destination
        # we need rotation of all the parenting joints, but not the destination joint
       
        destRootRotation = dest.getRotation().asMatrix()            



        
        
        
               
        
        
        
        
        
        
        srcHierarcyMatrix = gethierarchyMatrix(src) #This will be done on the first frame. A matrix of the hierarcys TPose will be constructed
        #hierarchyMatrix is used to isolate the rotation from the source joint
        
        changeofBasisMatrix = getChangeOfBasisMatrix(src) #This creates the matrix that is needed when we change the basis of the orientation
        #it is similar to the hierarchyMatrix, However, it is multiplicated in the reverse order, and it does not include the source joint orientation
        
        
        destHierarcyMatrix  = gethierarchyMatrix(dest) #This returns the hierarcy matrix of the destination, it is used when we are to apply the rotation to the destination
        
        #TEMPORARY
        #current = 185
        #pm.setCurrentTime(current) #temporary
        while current <= lastFrame:
    
            
            
            #print current
            
        
            pm.setCurrentTime(current)
             
            srcRotation = getRotationFromJoint(src,srcHierarcyMatrix) #Extract the Rotation from the source, using the hierarchy matrix
            
            # Rotation is extracted from the joint, 
        
            #Now it needs to be transformed into standard coordinate space.
            #this is achieved by doing a change of basis.     
            # inv(changeofBasisMatrix) * srcRotation * changeofBasisMatrix
            srcRotation = changeofBasisMatrix.inverse() * srcRotation * changeofBasisMatrix
            
            #print srcRotation
            print "Current frame:" + str(frames)
            
            setRotationToJoint(srcRotation,dest,destRootRotation)            
    
            dest.rotate.setKey()
            
            if current == lastFrame:
                break
        
            current = pm.findKeyframe(src , time = current, which='next')
            frames += 1
            
        #else:
            #print "TYSKLAND"
    
def getChangeOfBasisMatrix(node):
    #this is similar to the function "getHierarchyMatrix()"
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

def gethierarchyMatrix(node):
    #multiplies from the highest parent and down
    
    parents = node.getAllParents() #Get all the parents
    parents.reverse() #Reverse the order
    matrix = dt.Matrix()
    matrix = matrix.setToIdentity()
    for pNode in parents: # multiply all the parents tpose matrices
        if pNode.nodeType() == 'joint': #make sure we only multiply the joint nodes, no other transform nodes
        
            matrix = matrix * getTposeFromJoint(pNode)
    
    matrix = matrix * node.getRotation().asMatrix() # Multiply the parents matrix with the current joint matrix
    return node.getRotation().asMatrix()#matrix 
    
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
    #print joint.rotate.get();
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
    