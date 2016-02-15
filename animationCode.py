# Animation code
import pymel.core as pm
import time

root = pm.PyNode('iPi:Hip')

first = pm.findKeyframe(root, which='first')
last = pm.findKeyframe(root, which='last')

print first, last

curr = first

while curr <= last:
    curr = pm.findKeyframe(root, time=curr, which='next')
    pm.setCurrentTime(curr)
    # apply key values
    if curr==last:
        break