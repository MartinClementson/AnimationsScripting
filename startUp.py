import sys

import pymel.core as pm
import time

sys.path.insert(0,'//storage10.student.bth.se/students/20142/maik14/AnimationsScripting/')



try:
    
    reload (tf)
except:
    
    import transferFunctions as tf


try:
    moCap = reload(moCap)
except:
	import MocapScript as moCap