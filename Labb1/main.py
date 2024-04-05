from queue import PriorityQueue
import copy
import random
import time


movesQ = PriorityQueue()
expandedNodes ={

}

def printBoard(board):
    skip = 0
    print("-------------")
    for n in range(3):
        print("|", board[n+skip], "|", board[(n+1)+skip] , "|" , board[(n+2)+skip], "|" )
        print("-------------")
        skip = skip+2

def moveLeft(board):
    indexOfBlank = board.index(0)
    copyOfLeftNumber = board[indexOfBlank-1]
    board[indexOfBlank-1] = 0
    board[indexOfBlank] = copyOfLeftNumber
    return board

def moveUp(board):
    indexOfBlank = board.index(0)
    copyOfUpperNumber = board[indexOfBlank-3]
    board[indexOfBlank-3] = 0
    board[indexOfBlank] = copyOfUpperNumber
    return board

def moveDown(board):
    indexOfBlank = board.index(0)
    copyOfBottomNumber = board[indexOfBlank+3]
    board[indexOfBlank+3] = 0
    board[indexOfBlank] = copyOfBottomNumber
    return board

def moveRight(board):
    indexOfBlank = board.index(0)
    copyOfRightNumber = board[indexOfBlank+1]
    board[indexOfBlank+1] = 0
    board[indexOfBlank] = copyOfRightNumber
    return board


def allMoves(board, lastVisitedNode):
    
    
    # 0 - höger | 1 - ner | 2 - vänster | 3 - upp
    allowedMoves = [[0,1],[0,1,2],[1,2],[0,1,3],[0,1,2,3],[1,2,3],[0,3],[0,2,3],[2,3]]
    indexOfBlank = board[0].index(0)
    currentMoves = allowedMoves[indexOfBlank]
    
    for n in currentMoves:
        set = True
        state = copy.copy(board[0])
        if(n == 0):
            state = moveRight(state)
            h = evaluateH(state)
        if(n == 1):
            state = moveDown(state)
            h = evaluateH(state)
        if(n == 2):
            state = moveLeft(state)
            h = evaluateH(state)
        if(n == 3):
            state = moveUp(state)
            h = evaluateH(state)
        #print(h)
        s = ''.join(str(x) for x in state)
        if s in expandedNodes:
            set = False
            """ node = expandedNodes[s]
            if(node > board[1]+1):
                expandedNodes.update({s:board[1]+1}) """

        
        """ for move in lastVisitedNode:
            if(move == state):
                set = False
                break """
        if(set):
            movesQ.put((h + board[1]+1, [state, board[1]+1,h], board[0]))

def calculateManhattan(board):
    positions = [[1,1], [2,1], [3,1], [1,2], [2,2], [3,2], [1,3], [2,3], [3,3]]
    h = 0
    for n in board:
        indexOfCurrent = board.index(n)
        statePos = positions[indexOfCurrent]
        if(n == 0):
            goalPos = positions[8]
        else:
            goalPos = positions[n-1]
        
        y_dist = abs(statePos[1] - goalPos[1])
        x_dist = abs(statePos[0] - goalPos[0])
        h = h+y_dist+x_dist
    return h

def evaluateH(board):
    h1 = 0; 
    for n in range(len(board)):
        if(n == 8 and board[8] != 0):
            #print("pkus")
            h1 = h1+1
        elif(board[n] != n+1 and n != 8):
            h1 = h1+1
    
    h2 = calculateManhattan(board)
    return h2


    

def main():   

    board = [8,6,7,2,5,4,3,0,1]
    #random.shuffle(board)
    print(board)
    # Upp = -3 index
    # Vänster = -1 index
    # Höger = +1 index
    # Ner = +3 index
    print("Welcome to the 8-bit puzzle solver!\n")
    printBoard(board)
    allMoves([board,0], expandedNodes)
    
    numberOfIterations = 0
    levelInTree = 0; 
    start_time = time.time()
    while(True):
        numberOfIterations = numberOfIterations+1
        node = movesQ.get()
        if(node[1][2] == 0):
            break
        allMoves(node[1], expandedNodes)
        s = ''.join(str(x) for x in node[1][0])
        expandedNodes.update({s:[node[1][0],node[2]]})
        #lastVisitedNodes.append(node[1])
        #printBoard(node[1])
    #print(expandedNodes)
    #printBoard(node[1][0])

    printVector = []
    firstNode = node[1][0]
    printVector.append(firstNode)
    firstNode = node[2]
    printVector.append(firstNode)
    for n in range(node[0]):
        s1 = ''.join(str(x) for x in firstNode)
        parentNode = expandedNodes[s1][1]
        printVector.append(parentNode)
        firstNode = parentNode

    printVector2 = printVector[::-1]
    for n in printVector2:
        print("----------------------\n")
        printBoard(n,)
        print("\n")

    print("Depth: ", node[0])
    #print("Number of iterations: ",numberOfIterations)
    end_time = time.time()
    elapsedTime = end_time-start_time
    elapsedTime= round(elapsedTime,4)
    print("Elapsed time: ",elapsedTime,"s")
    

main()