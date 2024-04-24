import copy
import random

def Resolution(A, B):
    resolvent = {"p": set(), "n": set()}
    Ap, An = A["p"], A["n"]
    Bp, Bn = B["p"], B["n"]

    if not Ap.intersection(Bn) and not An.intersection(Bp):
        return False
    
    if Ap.intersection(Bn):
        a = random.choice(list(Ap.intersection(Bn)))
        Ap.remove(a)
        Bn.remove(a)
    else:
        a = random.choice(list(An.intersection(Bp)))
        An.remove(a)
        Bp.remove(a)
    
    resolvent["p"] = Ap.union(Bp)
    resolvent["n"] = An.union(Bn)

    if resolvent["p"].intersection(resolvent["n"]):
        return False
    
    return resolvent

def Solver(KB):
    KB = Incorporate(KB, [])
    KB_list = list(KB)

    while True:
        S = []
        KB_old = copy.deepcopy(KB_list)
        
        for A in KB_list:
            for B in KB_list:
                if A == B:
                    continue
                C = Resolution(A, B)
                if C:
                    S.append(C)
        
        if not S:
            return KB_list
        
        KB = Incorporate(S, KB)
        KB_list = list(KB)
        
        if KB_old == KB_list:
            return KB_list

def Incorporate(S, KB):
    for clause in S:
        KB = Incorporate_clause(clause, KB)
    return KB

def Incorporate_clause(A, KB):
    for B in KB:
        if all(x in B["p"] for x in A["p"]) and all(x in B["n"] for x in A["n"]):
            return KB
    for B in KB:
        if all(x in A["p"] for x in B["p"]) and all(x in A["n"] for x in B["n"]):
            KB.remove(B)
    KB.append(A)
    return KB

# Example usage:
initial_clauses = [
    {"p": {-1, -2, 3}, "n": set()},
    {"p": {-2, 3, 5}, "n": set()},
    {"p": {-5, 2}, "n": set()},
    {"p": {-5, -3}, "n": set()},
    {"p": {5}, "n": set()},
    {"p": {1, 5, 4}, "n": set()}
]
KB = initial_clauses
result = Solver(KB)
print("Final Knowledge Base:", result)