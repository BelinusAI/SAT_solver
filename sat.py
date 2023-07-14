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

def simplify_formula(formula, assignments):
	"""
	Simplify a formula given a set of assignments.

	Args:
		formula (list): a boolean formula in the CNF format.
		assignments (dict): a set of assignments to boolean variables represented
							as a dictionary from variables to boolean values.

	Returns:
		A length-two tuple of (formula, assignments), described as follows:

		formula (list): the new simplified formula
		assignments (dict): a set of assignments to boolean variables represented
							as a dictionary from variables to boolean values.
		
		When a clause has one literal remaining, and if it is not in assignments 
		dictionary, we should map that literal to its designated value in the CNF 
		so that the clause evaluates to true and it is added to assignments.

	If the assignment causes the formula to evaluate to False, formula is None . If the 
	assignment causes the formula to evaluate to True, formula is [].

	Examples:
	>>> formula = [[("a", True)]]
	>>> assignments = dict()
	>>> simplify_formula(formula, assignments)
	([], {'a': True})
	
	>>> formula = [[("a", True), ("b", False), ("c", True)], [("a", True), ("b", True)]]
	>>> assignments = {"a": False}
	>>> simplify_formula(formula, assignments)
	([], {'a': False, 'b': True, 'c': True})
	
	"""
	new_formula = []
	new_assignments = assignments.copy()

	for clause in formula:
		new_clause = []
		counter = 0
		for literal in clause:
			if(new_assignments.get(literal[0]) is True and literal[1]
      			or new_assignments.get(literal[0]) is False and not literal[1]):
				new_clause = []
				break	
			elif(new_assignments.get(literal[0]) is True and not literal[1]
      			or new_assignments.get(literal[0]) is False and literal[1]):
				counter += 1
				if counter == len(clause):
					return None, new_assignments			
	
			elif(new_assignments.get(literal[0]) is None):
				new_clause.append(literal)
			
		if(new_clause):
				new_formula.append(new_clause)	
		
	for new_clause in new_formula:
		if(len(new_clause) == 1):
			new_assignments[new_clause[0][0]] = new_clause[0][1]
			return simplify_formula(new_formula, new_assignments)
			
	return new_formula, new_assignments						
