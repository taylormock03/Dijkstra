import pyinputplus
from pathLogic import *

newPath = ""

paths = {}

print("Path logic = A,B,15 means the cost of going (directly) from A to B is 15")
while newPath != "done":
    # Add paths to the network
    newPath = pyinputplus.inputCustom(validatePath, 
                                      prompt="Create a path > ", 
                                    )
    if newPath != "done":
        addPath(paths,newPath)


node = "0"
choices = getNodes(paths)
choices.append("quit")
while node!="quit":
    node = pyinputplus.inputMenu(choices, prompt="Which Node would you like to calculate for? > \n", )
    
    if node!="quit":
        calculatePaths(paths,node)
        print()