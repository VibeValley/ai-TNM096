def resolve(clause1, clause2):
    """
    Perform resolution between two clauses.
    """
    resolvent = []
    for literal in clause1:
        if literal not in clause2 and -literal not in clause2:
            resolvent.append(literal)
            #print(literal)
    for literal in clause2:
        if literal not in clause1 and -literal not in clause1:
            resolvent.append(literal)
    print(resolvent)
    return resolvent


def resolution_algorithm(clauses):
    """
    Apply the resolution mechanism to a set of clauses.
    """
    new_clauses = list(clauses)
    while True:
        new_resolvents = set()
        for i in range(len(new_clauses)):
            for j in range(i + 1, len(new_clauses)):
                resolvent = resolve(new_clauses[i], new_clauses[j])
                if not resolvent:  # Empty resolvent means contradiction found
                    return True
                new_resolvents.add(tuple(resolvent))
        if not new_resolvents.issubset(set(map(tuple, new_clauses))):
            new_clauses.extend(list(new_resolvents))
        else:
            return False


# Example usage:
clauses = [
        [1, 2, 3],   # (A OR B OR C)
        [-1, -2],    # (-A OR -B)
        [-1, -3],    # (-A OR -C)
        [-2, -3],    # (-B OR -C)
        [-3, 1]      # (-C OR A)
    ]

    # Add the clause representing that B does not know how to drive
clauses.append([-2])  # (-B)

result = resolution_algorithm(clauses) # B1 - Guilty
print(result)