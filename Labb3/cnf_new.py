import copy
import random

def positive(A):
    temp = []
    for literal in A:
        if(literal > 0):
            temp.append(literal)
    
    temp2 = tuple(temp)
    return temp2

def makePos(A):
    newA = set()
    for every in A:
        newA.add(-every)
    return newA

def negative(A):
    temp = []
    for literal in A:
        if(literal < 0):
            temp.append(-literal)
    
    temp2 = tuple(temp)
    return temp2


def Resolution(A,B):
    C = set()
    A = set([A])
    B = set([B])
    print('A:  ',A)
    print('B:  ',B)

    Ap = set(positive(A))
    #print('Ap:  ',Ap)
    An = set(negative(A))
    #print('An:  ',An)
    Bp = set(positive(B))
    #print('Bp:  ',Bp)
    Bn = set(negative(B))
    #print('Bn:  ',Bn)

    Ap_i_Bn = Ap.intersection(Bn)
    An_i_Bp = An.intersection(Bp)

    if(len(Ap_i_Bn) == 0 and len(An_i_Bp) == 0):
        return False
    if(len(Ap_i_Bn) != 0):
        a = random.choice(tuple(Ap_i_Bn))
        Ap = Ap.difference(set([a]))
        Bn = Bn.difference(set([a]))
    else:
        a = random.choice(tuple(An_i_Bp))
        An = An.difference(set([a]))
        Bp = Bp.difference(set([a]))
    
    Cp = Ap.union(Bp)
    Cn = An.union(Bn)
    """ print('Cp:  ',Cp)
    print('Cn:  ', Cn) """
    if(len(Cp.intersection(Cn)) != 0):
        return False
    C.add(tuple(Cp))
    C.add(tuple(makePos(Cn)))
    return C




    

def Incorporate(S,KB):
    for clause in S:
        KB.add(tuple(Incorporate_Clause(clause,KB)))
    return KB

def Incorporate_Clause(A, KB):
    for clauseB in KB:
        if(clauseB == A or set([clauseB]).issubset(set([A]))):
            return KB
    for clauseB in KB:
        if(clauseB == A or set([A]).issubset(set([clauseB]))):
            KB = set([KB]).difference(set([clauseB]))
    
    KB = set(KB).union(set(A))
    return KB




def Solver(KB): #Main
    K = set()
    
    KB = Incorporate(KB,K)
    KB_list = list(KB)
    print('KB_list:    ', KB_list)

    while(True):
        S = set()
        KB_old = copy.copy(KB_list)
        for i in range(len(KB_list)):
            for j in range(i+1,len(KB_list)):
                C = Resolution(KB_list[i], KB_list[j])
                if (C != False):
                    absolute_C = {abs(element) for element in C}
                    #print('Here we have C: ', C)
                    S = S.union(absolute_C)
                    print('Here we have S: ', S)
        if(len(S) ==0):
            return KB_list
        
        KB = Incorporate(S,set([KB_list]))
        KB_list = list(KB)
        if(KB_old != KB_list):
            return KB_list

# sun = 1
# money = 2
# ice = 3
# cry = 4
# movie = 5


initial_clauses = set()
initial_clauses.add(tuple([-1,-2,3]))
initial_clauses.add(tuple([-2,3,5]))
initial_clauses.add(tuple([-5,2]))
initial_clauses.add(tuple([-5,-3]))
initial_clauses.add(tuple([5]))
initial_clauses.add(tuple([1,5,4]))
print(initial_clauses)

hej = Solver(initial_clauses)
print('nu leker vi' , hej)