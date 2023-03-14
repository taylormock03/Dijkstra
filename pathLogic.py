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

def addPath(paths, newPath):
    startPoint = newPath[0]
    endPoint = newPath[1]
    cost = int(newPath[2])

    # this adds the path from A to B
    try:
        paths[startPoint][endPoint]=cost
    except:
        paths[startPoint] = {endPoint:cost}

    # This adds the corresponding path from B to A
    try:
        paths[endPoint][startPoint]=cost
    except:
        paths[endPoint] = {startPoint:cost}

    return 

def calculatePaths(paths, startPoint, visitedNodes = [], costs = {}):
    # printTableHead(paths, startPoint)
    
    if len(visitedNodes) ==0:
        visitedNodes = [startPoint]

    # Initialisation of costs
    for node in paths:
        if node == startPoint:
            costs[node]=0
        elif node in paths[startPoint]:
            costs[node] = paths[startPoint][node]
        else:
            costs[node] = "inf"
    
    print (costs)
    
    closestNeighbour,closestCost = getClosestNeighbour(costs, visitedNodes)
    visitedNodes.append(closestNeighbour)
    print(visitedNodes)

    print (costs)

    while closestNeighbour!=-1:
        for x in paths[closestNeighbour]:
            if costs[x] == 'inf':
                costs[x] = paths[closestNeighbour][x]+closestCost

            if paths[closestNeighbour][x]+closestCost <= costs[x]:
                costs[x]= paths[closestNeighbour][x]+closestCost

        closestNeighbour,closestCost = getClosestNeighbour(costs, visitedNodes)
        visitedNodes.append(closestNeighbour)

    print (costs)
    # printTableLine(shortestPath)
    

def getClosestNeighbour(neighbours, visitedNodes):
    closestNeighbour=False
    minCost = 999
    for x in neighbours:
        if neighbours[x]=="inf" or x in visitedNodes:continue

        elif neighbours[x]< minCost: 
            minCost=neighbours[x]
            closestNeighbour=x
    if closestNeighbour ==False: return -1,-1 
    else: return closestNeighbour,minCost

calculatePaths(paths={'A': {'B': 1, 'C': 5}, 'B': {'A': 1, 'C': 3, 'D': 13}, 'C': {'A': 2, 'B': 3, 'D': 95}, 'D': {'C': 95}}, startPoint="A")