import copy
import random

class Clauses:
    def __init__(self, p=None, n=None):
        self.p = p if p else set()
        self.n = n if n else set()

    def __eq__(self, other):
        return self.p == other.p and self.n == other.n

    def __lt__(self, other):
        return len(self.p) + len(self.n) < len(other.p) + len(other.n)

    def __hash__(self):
        p_hashable = frozenset(self.p) if isinstance(self.p, (set, list, tuple)) else self.p
        n_hashable = frozenset(self.n) if isinstance(self.n, (set, list, tuple)) else self.n
        return hash((p_hashable, n_hashable))

    def __str__(self):
        return f"[{self.p}, {self.n}]"

    def __repr__(self):
        listed = []
        for item in self.p:
            listed.append(item)
        for item in self.n:
            listed.append(item)

        return f"{listed}"

    def __contains__(self, item):
        return item in self.p or item in self.n

    def __len__(self):
        return len(self.p) + len(self.n)

    def __iter__(self):
        yield from self.p
        yield from self.n

    def __sub__(self, other):
        return Clauses(self.p - other.p, self.n - other.n)

    def __or__(self, other):
        return Clauses(self.p | other.p, self.n | other.n)

    def __and__(self, other):
        return Clauses(self.p & other.p, self.n & other.n)

    def add_positive(self, item):
        self.p.add(item)

    def add_negative(self, item):
        self.n.add(item)

    def remove_positive(self, item):
        self.p.remove(item)

    def remove_negative(self, item):
        self.n.remove(item)

def positive(A):
    temp = []
    for literal in A:
        if(literal > 0):
            temp.append(literal)
    
    temp2 = tuple(temp)
    return temp2

def makeNegative(A):
    temp = []
    for tuple1 in A:
        for i in tuple1:
            temp.append(-i)
    
    temp2 = tuple(temp)
    return temp2

def negative(A):
    temp = []
    for literal in A:
        if(literal < 0):
            temp.append(-literal)
    
    temp2 = tuple(temp)
    return temp2

                    


def Resolution(A, B):
    C = set()
    A = set(A)
    B = set(B)
    

    Ap = set()
    An = set()
    Bp = set()
    Bn = set()
    Ap.add(positive(A))
    An.add(negative(A))
    Bp.add(positive(B))
    Bn.add(negative(B))
    """ print('Ap:', Ap)
    print('An:', An)
    print('Bp:', Bp)
    print('Bn:', Bn) """

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
    
    Cp = Bp.union(Ap)
    Cn = An.union(Bn)
    """ print(Cn)
    print(Cp)
    print(Cp.intersection(Cn)) """
    if Cp.intersection(Cn):
        return False
    Cn2 = set()
    Cn2.add(makeNegative(Cn))
 
    C = Cp.union(Cn2)
    return C

def Incorporate(S, KB):
    for clause in S:
        KB = Incorporate_Clause(clause, KB)
        #KB.add(tuple(clause))
    return KB

def Incorporate_Clause(A, KB):
    a_set = set()
    a_set.add(A)
    
    
    for clauseB in KB:
        b_set = set()
        b_set.add(clauseB)
        if b_set == a_set or b_set.issubset(a_set):
            print('in 1st if')
            return KB
    for clauseB in KB:
        b_set = set()
        b_set.add(clauseB)
        if b_set == a_set or a_set.issubset(b_set):
            print('in 2st if')
            KB = KB - b_set

    
    KB = KB.union(a_set)
    return KB

def Solver(KB):
    K = set()
    print('heres first incorporate')
    KB = Incorporate(KB, K)
    KB_list = list(KB)
    print('KB_list:', KB_list)
    k = 0
    while k < 1:
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
        print('heres second incorporate')
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

#result = Solver(initial_clauses)
#print('Final Knowledge Base:', result)

hejsan = set()
p_set = set((1,2))
p_set2 = set((1,2,3))
n_set = set((3,-4))
hejsan.add(Clauses(p_set,n_set))
hejsan.add(Clauses(p_set2,n_set))

print(hejsan)

