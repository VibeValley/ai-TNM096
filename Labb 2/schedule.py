import random
import numpy as np

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

def getConflicts(courses):

    conflicts = np.array([])
    n = 0
    while n < len(courses):
        first = courses[n][2]
        second = courses[n+1][2]
        third = courses[n+2][2]

        if(first == second or first == third or second == third):
            conflicts = np.append(conflicts, n)

        n = n+3
    
    return conflicts

def randomizeOrder(courses):
    newArray = np.random.shuffle(courses)
    return newArray


def main():
    courses = loadCourses()
    randomizeOrder(courses)
    conflicts = getConflicts(courses)

    print(conflicts)

main()