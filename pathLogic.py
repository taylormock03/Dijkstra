def validatePath(path:str):
    path = path.split(",")

    if path == ["done"]:
        return "done"
    
    elif len(path) ==3:
        if not path[0].isupper() or not path[1].isupper():
            raise Exception("Please Use Capital Letters For Paths")
        
        elif not path[2].isnumeric():
            raise Exception("Path Cost Must Be A Number")
        
        elif int(path[2])<=0:
            raise Exception("Cost Cannot Be <=0")
        return path 
    
    else:
        raise Exception("Invalid Path")
    
def addPath(path):
    print(path)
    