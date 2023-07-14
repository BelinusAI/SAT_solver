# SAT_solver
Satisfiability solver or SAT solver is a classic tool that works on Boolean formulas. 
Given a formula, either the solver finds Boolean variable values that make the formula true, or the solver indicates that no solution exists.

The formula is in conjunctive normal form (CNF):
variable: a Python string. 
literal: a pair (a tuple), containing a variable and a Boolean value (False if not appears in this literal, True otherwise)
clause: a list of literals
formula: as a list of clauses

## Implementation
* Read and parse input from a file.
* Convert the problem to CNF clauses.
* Execute


```
  sat.satisfying_assignment(formula)
```



