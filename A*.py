import numpy as np
from copy import copy,deepcopy
depthVariable = 0
visited = []
costVariable = 0
allNodes = []


class Node:
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost

def create_node(state, parent, operator, depth, cost):
    return Node(state, parent, operator, depth, cost)

def move_left(state,row,column):
    global costVariable
    costVariable = costVariable + 1
    
    AnswerRow = 0
    AnswerColumn = 0
    #Checking position of 0
    countX = 0
    countY = 0
    for x in state:
        countX =countX + 1
        countY = 0
        for y in x:
            countY = countY + 1
            if y == 8.0:
                
                AnswerRow = countX
                AnswerColumn = countY
                break

    
    #Boundary conditions
    if AnswerColumn == 1 :
        return None

    
    #Switching places
    AnswerRow = AnswerRow - 1
    AnswerColumn = AnswerColumn - 1
    state[AnswerRow][AnswerColumn-1] = 8
    state[AnswerRow][AnswerColumn]= 1  

    

    return state    

def move_right(state,row,column):
    global costVariable
    costVariable = costVariable + 1
    
    AnswerRow = 0
    AnswerColumn = 0
    #Checking position of 0
    countX = 0
    countY = 0
    for x in state:
        countX =countX + 1
        countY = 0
        for y in x:
            countY = countY + 1
            if y == 8.0:
                
                AnswerRow = countX
                AnswerColumn = countY
                break

    #Boundary conditions
    if AnswerColumn == column :
        return None

    
    #Switching places
    AnswerRow = AnswerRow - 1
    AnswerColumn = AnswerColumn - 1
    state[AnswerRow][AnswerColumn+1] = 8
    state[AnswerRow][AnswerColumn]= 1  

    

    return state    

def move_up(state,row,column):
    global costVariable
    costVariable = costVariable + 1
    
    AnswerRow = 0
    AnswerColumn = 0
    #Checking position of 0
    countX = 0
    countY = 0
    for x in state:
        countX =countX + 1
        countY = 0
        for y in x:
            countY = countY + 1
            if y == 8.0:
                
                AnswerRow = countX
                AnswerColumn = countY
                break

    #Boundary conditions
    if AnswerRow == 1 :
        return None

    
    #Switching places
    AnswerRow = AnswerRow - 1
    AnswerColumn = AnswerColumn - 1
    state[AnswerRow-1][AnswerColumn] = 8
    state[AnswerRow][AnswerColumn]= 1  

    

    return state    

def move_down(state,row,column):
    global costVariable
    costVariable = costVariable + 1
    
    AnswerRow = 0
    AnswerColumn = 0
    #Checking position of 0
    countX = 0
    countY = 0
    for x in state:
        countX =countX + 1
        countY = 0
        for y in x:
            countY = countY + 1
            if y == 8.0:
                
                AnswerRow = countX
                AnswerColumn = countY
                break

    #Boundary conditions
    if AnswerRow == row :
        return None

    
    #Switching places
    AnswerRow = AnswerRow - 1
    AnswerColumn = AnswerColumn - 1
    state[AnswerRow+1][AnswerColumn] = 8
    state[AnswerRow][AnswerColumn]= 1  

    

    return state   

def arrayChecker(s1 , s2,r,c):
    for x in range(0,r):
        for y in range(0,c):

            if s1[x][y] != s2[x][y]:
                return False
    
    return True

def checkVisited(a1,rows,columns):
    found = False
    for x in visited:
        if arrayChecker(a1,x.state,rows,columns) == True:
            found = True
    return found   

def expand_node(node,rows,columns):

    global depthVariable
    depthVariable = depthVariable + 1
    expanded_nodes = []
    # ----- code here
   
    #Checking position of 8
    AnswerRow = 0
    AnswerColumn = 0
    #Checking position of 8
    countX = 0
    countY = 0
    for x in node.state:
        countX =countX + 1
        countY = 0
        for y in x:
            countY = countY + 1
            if y == 8.0:
                
                AnswerRow = countX
                AnswerColumn = countY
                break
    
    AnswerRow = AnswerRow - 1
    AnswerColumn = AnswerColumn - 1
    
    #Check for move up 
    a1 = deepcopy(node.state)
    if AnswerRow != 0 and node.state[AnswerRow-1][AnswerColumn] == 1:
        a1 = move_up(a1,rows,columns)
        #check if its in visited
        if checkVisited(a1,rows,columns) == False:
            sub = create_node(a1,node.state,"up",depthVariable,depthVariable)
            expanded_nodes.append(sub)
            
    #Check for move left
    a4 = deepcopy(node.state)
    if AnswerColumn != 0 and node.state[AnswerRow][AnswerColumn-1] == 1:
        a4 = move_left(a4,rows,columns)
        #check if its in visited
        if checkVisited(a4,rows,columns) == False:
            sub = create_node(a4,node.state,"left",depthVariable,depthVariable)
            expanded_nodes.append(sub)

     #Check for move right
    a3 = deepcopy(node.state)
    if AnswerColumn != 19 and node.state[AnswerRow][AnswerColumn+1] == 1:
        a3 = move_right(a3,rows,columns)
        #check if its in visited
        if checkVisited(a3,rows,columns) == False:
            sub = create_node(a3,node.state,"right",depthVariable,depthVariable)
            expanded_nodes.append(sub)
            
    #Check for move down
    a2 = deepcopy(node.state)
    if AnswerRow != 19 and node.state[AnswerRow+1][AnswerColumn] == 1:
        a2 = move_down(a2,rows,columns)
        #check if its in visited
        if checkVisited(a2,rows,columns) == False:
            sub = create_node(a2,node.state,"down",depthVariable,depthVariable)
            expanded_nodes.append(sub)        

    
    return expanded_nodes


def backTrackerVisited(answerNode , startNode,rows,columns):
    cost = 0
    final = answerNode.state
    toPrint = []
    for x in reversed (visited):
        if(arrayChecker(answerNode.parent,x.state,rows,columns)):
             cost = cost + 1   
             #print(answerNode.operator)
             toPrint.append(answerNode.operator)
             answerNode = x
             final = answerNode.state
    print("\nCost of Reaching solution : " + str(cost - 1)+"\n")
    toPrint.pop(0)
    print("Path to Solution : \n ")
    for x in reversed (toPrint):
        print(x)

def manhattanDistance(current,goal):

    #Takes arrays as parameters

    #Find position of piece currently
    row = 0
    column = 0

    for x in current:
        toBreak = False
        column = 0
        for y in x:
            if current[row][column] == 8 : 
                toBreak = True
                break
            column = column + 1
        if toBreak == True:
            break
        
        row = row + 1
    
    CurrentRow = row
    CurrentColumn = column

    #Find position of piece in Final State
    row = 0
    column = 0

    for x in goal:
        toBreak = False
        column = 0
        for y in x:
            if goal[row][column] == 8 : 
                toBreak = True
                break
            column = column + 1
        if toBreak == True:
            break
        
        row = row + 1
    
    FinalRow = abs(CurrentRow - row)
    FinalColumn = abs(CurrentColumn - column)
    MD = FinalRow + FinalColumn
    return MD



def gbfs(start, goal,rows,columns):
     #---- code here -----
   
   # Create lists for open nodes and closed nodes
    open = []

    # Add the start node
    open.append(start)
    answerFound = False
    # Loop until the open list is empty
    while len(open)>0:

        # Sort the open list to get the node with the lowest cost first
        min = open[0].cost + open[0].depth
        counter = 0
        minimumIndex= 0
        for a in open:
            
            if((a.cost + a.depth) < min):
                min = a.cost + a.depth
                minimumIndex = counter

            counter = counter + 1

        #Node with lowest cost
        current = open.pop(minimumIndex)
        

        # Add the current node to the closed list
        visited.append(current)

        # Check if we have reached the goal, return the path (From Current Node to Start Node By Node.parent)
        if (arrayChecker(current.state,goal.state,rows,columns)) == True:
            answerFound = True
            break

        # Get neighbours
        neighbors = expand_node(current,rows,columns)

        # Loop neighbors
        for i in neighbors:
    
            # Check if the neighbor is in the closed list
            if(i in visited):
                continue

            # Calculate cost to goal
            i.cost = manhattanDistance(i.state,goal.state)
            for a in visited:
                if(arrayChecker(i.parent,a.state,rows,columns) == True):
                    i.depth = a.depth + 1
            
            # Check if neighbor is in open list and if it has lower cost
            if(In_Open(open, i,rows,columns) == True):
                open.append(i)
           
    if(answerFound == False):
        print("NO POSSIBLE SOLUTION !")
        return None


    print("Cost of calculation : ")
    counter = 0
    for i in visited:
        counter = counter + 1
    print(counter)

    #print("\nPath of Calculation : \n")
    #for i in visited:
    #    print(i.state)
    #    print("\n")
    #print("\n")
    backTrackerVisited(goal,start,rows,columns)

def In_Open(open, neighbor,r,c):
    
    for node in open:
        if (arrayChecker(neighbor.state,node.state,r,c) and neighbor.cost >= node.cost):
            return False
    return True


def main():
    #Program takes input of maze size from user , as well as initial and final state of maze from files

    dim =input("Rows in Maze : ")
    dim2 =input("Columns in Maze : ")
    #Node with initial position
    data = np.genfromtxt("/home/saad/Downloads/Semester6/AI/Assignment02/input.txt")
    #Node with final position
    data2 = np.genfromtxt("/home/saad/Downloads/Semester6/AI/Assignment02/input2.txt")
    testNode = create_node(data, data , "None",0,0)
    testNode2 = create_node(data2, data2 , "None",0,0)
    print("\n")
    #print(arrayChecker(data,data,12,12))
    print("\n******************************\n")
    temp = expand_node(testNode,12,12)
    #bfs(testNode , testNode2 , int(dim) , int(dim2))
    gbfs(testNode , testNode2 , int(dim) , int(dim2))
    
if __name__ == "__main__":
    main()