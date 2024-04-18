import random
import numpy as np
import math
import copy


def loadCourses():
    courses = np.array([
      "MT101", "MT102", "MT103",
      "MT104", "MT105", "MT106",
      "MT107", "MT201", "MT202",
      "MT203", "MT204", "MT205",
      "MT206", "MT301", "MT302",
      "MT303", "MT304", "MT401",
      "MT402", "MT403", "MT501",
      "MT502", "     ", "     "
    ])
    return courses

def printSchedule(solution):
    print("     TP51      SP34      K3")
    print("     ----      ----      ----")
    print("9   ", solution[0],"   ", solution[1], "   ", solution[2])
    print("10  ", solution[3],"   ", solution[4], "   ", solution[5])
    print("11  ", solution[6],"   ", solution[7], "   ", solution[8])
    print("12  ", solution[9],"   ", solution[10], "   ", solution[11])
    print("1   ", solution[12],"   ", solution[13], "   ", solution[14])
    print("2   ", solution[15],"   ", solution[16], "   ", solution[17])
    print("3   ", solution[18],"   ", solution[19], "   ", solution[20])
    print("4   ", solution[21],"   ", solution[22], "   ", solution[23])
    
def getConflicts(courses):

    conflicts = np.array([])
    n = 0
    while n < len(courses):
        first = courses[n][2]
        second = courses[n+1][2]
        third = courses[n+2][2]

        if(first == second or first == third or second == third):
            if((first == "5" and second == "5") or (second == "5" and third == "5") or (first == "5" and third == "5")):
                n = n
                #print("hej")
            else:
                conflicts = np.append(conflicts, n)

        n = n+3
    conflicts2 = conflicts.astype(int)
    #print(conflicts2)
    return conflicts2

def randomizeOrder(courses):
    newArray = np.random.shuffle(courses)
    return newArray


def min_conflicts(courses,randIndex, conflicts):
    startOfRowCourse = courses[randIndex]
    courseNumber = startOfRowCourse[2]

    minIndex = np.array([[10000,10000]])
    minIndexConflict = 1000
    
    for i in range(len(courses)):
        courseNumberOther = courses[i][2]
        #Prevent same row and same number
        if(courseNumber != courseNumberOther):
            neighbours = ["", ""]
            col = i % 3
            nConflicts = 0

            if(courseNumber == "5"):
                nConflicts = 0
            else:
                if(col == 0):
                    neighbours[0] = courses[i+1]
                    neighbours[1] = courses[i+2]
                if(col == 1):
                    neighbours[0] = courses[i-1]
                    neighbours[1] = courses[i+1]
                if(col == 2):
                    neighbours[0] = courses[i-2]
                    neighbours[1] = courses[i-1]

                if(courseNumber == neighbours[0][2]):
                    nConflicts = nConflicts+1
                if(courseNumber == neighbours[1][2]):
                    nConflicts = nConflicts+1

            if(nConflicts <= minIndexConflict):
                minIndexConflict = nConflicts
                if(minIndex[0][1] > nConflicts):
                    minIndex = np.array([], dtype=int).reshape(0, 2)
                newRow = np.array([i,nConflicts])
                minIndex = np.vstack([minIndex,newRow])
    random_row = np.random.choice(minIndex.shape[0])
    randomLowestConflict = minIndex[random_row] 
    return randomLowestConflict[0]

                #courses[startConflict+i]







def main():
    courses = loadCourses()
    print("          Initial state: ")
    printSchedule(courses)
    print("\n")
    conflicts = getConflicts(courses)
    randomizeOrder(courses)
    print("       Randomized state: ")
    printSchedule(courses)
    print("\n")
    #print(conflicts)
    n = 0
    while(len(conflicts) > 0 and n < 1000):
        n = n + 1

        randConflict = np.random.choice(conflicts)
        
        minConflictIndex = min_conflicts(courses, randConflict, conflicts)

        placeholder = copy.copy(courses[randConflict])
        courses[randConflict] = copy.copy(courses[minConflictIndex])
        courses[minConflictIndex] = placeholder

        #--------PRINT EVERY STEP------------
        """ printSchedule(courses)
        print("\n") """
        
        conflicts = getConflicts(courses)
        np.random.shuffle(conflicts) # So it wont choose the same again

    #print(conflicts)
    print("          Final state: ")
    printSchedule(courses)
    print("\n")
    print("Number of swaps: ", n)
    print("Conflict array: ",conflicts)



main()