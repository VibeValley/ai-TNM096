import copy
import random

def positive(A):
    return {literal for literal in A if literal > 0}

def makePos(A):
    return {-every for every in A}

def negative(A):
    return {-literal for literal in A if literal < 0}

def Resolution(A, B):
    C = set()
    A = set(A)
    B = set(B)
    

    Ap = positive(A)
    An = negative(A)
    Bp = positive(B)
    Bn = negative(B)
    print('Ap:', Ap)
    print('An:', An)
    print('Bp:', Bp)
    print('Bn:', Bn)

    Ap_i_Bn = Ap.intersection(Bn)
    An_i_Bp = An.intersection(Bp)

    if not Ap_i_Bn and not An_i_Bp:
        return False
    
    if Ap_i_Bn:
        a = random.choice(tuple(Ap_i_Bn))
        Ap.remove(a)
        Bn.remove(a)
    else:
        a = random.choice(tuple(An_i_Bp))
        An.remove(a)
        Bp.remove(a)
    
    Cp = Ap.union(Bp)
    Cn = An.union(Bn)

    if Cp.intersection(Cn):
        return False
    
    C.add(tuple(Cp))
    C.add(tuple(makePos(Cn)))
    return C

def Incorporate(S, KB):
    for clause in S:
        KB.add(tuple(clause))
    return KB

def Incorporate_Clause(A, KB):
    for clauseB in KB:
        if clauseB == A or set(clauseB).issubset(A):
            return KB
    for clauseB in KB:
        if clauseB == A or set(A).issubset(clauseB):
            KB = KB - {clauseB}
    KB = KB.union({tuple(A)})
    return KB

def Solver(KB):
    KB = Incorporate(KB, set())
    KB_list = list(KB)
    print('KB_list:', KB_list)
    k = 0
    while True:
        k +=1
        S = set()
        KB_old = copy.copy(KB_list)
        for i in range(len(KB_list)):
            for j in range(i + 1, len(KB_list)):
                C = Resolution(KB_list[i], KB_list[j])
                if C:
                    print('Here we have C:', C)
                    S = S.union(C) #Måste vi inte kolla ifall ensamma objekt redan finns inlagda oavsett minus och plus. Det kan ju inte vara -sun och sun liksom
                    print('Here we have S:', S)
        if not S:
            return KB_list
        KB = Incorporate(S, KB)
        KB_list = list(KB)
        if KB_old == KB_list:
            return KB_list

initial_clauses = set()
initial_clauses.add(tuple([-1,-2,3]))
initial_clauses.add(tuple([-2,3,5]))
initial_clauses.add(tuple([-5,2]))
initial_clauses.add(tuple([-5,-3]))
initial_clauses.add(tuple([5]))
initial_clauses.add(tuple([1,5,4]))

print(initial_clauses)

result = Solver(initial_clauses)
print('Final Knowledge Base:', result)