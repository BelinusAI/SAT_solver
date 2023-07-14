def satisfying_assignment(formula):
    """
    Find a satisfying assignment for a given CNF formula.
    Returns that assignment if one exists, or None otherwise.

    >>> satisfying_assignment([])
    {}
    >>> x = satisfying_assignment([[('a', True), ('b', False), ('c', True)]])
    >>> x.get('a', None) is True or x.get('b', None) is False or x.get('c', None) is True
    True
    >>> satisfying_assignment([[('a', True)], [('a', False)]])
    """
    def SAT_solver(formula, assignments):

        if(formula is not None and not formula):
            return assignments
        
        elif(formula is None):
            return None
        
        for clause in formula:
            for literal in clause:
                if(assignments.get(literal[0]) is not None):
                    continue						
                for trial in [True, False]:
                    
                    assignments[literal[0]] = trial

                    new_formula , new_assigments = simplify_formula(formula, assignments)
                    solver = SAT_solver(new_formula, new_assigments)		
                    if(solver is not None):
                        return solver					
                return None			
    return SAT_solver(formula, dict())