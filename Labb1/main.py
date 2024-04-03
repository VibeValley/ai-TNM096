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
    indexOfBlank = board.index(0)

    currentMoves = allowedMoves[indexOfBlank]
    
    for n in currentMoves:
        set = True
        state = copy.copy(board)
        if(n == 0):
            state = moveRight(state)
            h1 = evaluateH(state)
        if(n == 1):
            state = moveDown(state)
            h1 = evaluateH(state)
        if(n == 2):
            state = moveLeft(state)
            h1 = evaluateH(state)
        if(n == 3):
            state = moveUp(state)
            h1 = evaluateH(state)
        s = ''.join(str(x) for x in state)
        if s in expandedNodes:
            set = False

        
        """ for move in lastVisitedNode:
            if(move == state):
                set = False
                break """
        if(set):
            movesQ.put((h1, state))

def evaluateH(board):
    h1 = 0; 
    for n in range(len(board)):
        if(board[n] != n):
            h1 = h1+1
    return h1
    

def main():   

    board = [5,8,6,3,4,7,0,1,2]
    random.shuffle(board)
    print(board)
    # Upp = -3 index
    # Vänster = -1 index
    # Höger = +1 index
    # Ner = +3 index
    print("Welcome to the 8-bit puzzle solver!\n")
    printBoard(board)
    allMoves(board, expandedNodes)
    
    numberOfIterations = 0
    start_time = time.time()
    while(True):
        numberOfIterations = numberOfIterations+1
        node = movesQ.get()
        
        if(node[0] == 0):
            
            break
        allMoves(node[1], expandedNodes)
        s = ''.join(str(x) for x in node[1])
        expandedNodes.update({s:node[1]}) 
        #lastVisitedNodes.append(node[1])
        #printBoard(node[1])
        
    #print(expandedNodes)
    printBoard(node[1])
    print("Number of iterations: ",numberOfIterations)
    end_time = time.time()
    elapsedTime = end_time-start_time
    elapsedTime= round(elapsedTime,4)
    print("Elapsed time: ",elapsedTime,"s")
    

    

main()