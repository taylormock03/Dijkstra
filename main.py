import pyinputplus
from pathLogic import *

done = ""

while done != "done":
    # Add paths to the network
    done = pyinputplus.inputCustom(validatePath, prompt="Create a path (e.g. A,B,15 means the cost of going from A to B is 15) > ", postValidateApplyFunc=addPath)
    
