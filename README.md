# dimacs2smtlib
```
 $ cat example.cnf
 p cnf 2 4
 1 2 0
 -1 -2 0
 1 -2 0
 -1 2 0
 $ python3 dimacs2smtlib.py example.cnf
 $ cat example.cnf.smt2
 (set-logic QF_UF)
 (declare-fun v_1 () Bool)
 (declare-fun v_2 () Bool)
 (assert (or v_1 v_2))
 (assert (or (not v_1) (not v_2)))
 (assert (or v_1 (not v_2)))
 (assert (or (not v_1) v_2))
 (check-sat)
```
