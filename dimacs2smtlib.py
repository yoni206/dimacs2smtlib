import sys
dimacs_path = sys.argv[1]
with open(dimacs_path, "r") as f:
  clauses_lines = f.read().splitlines()[1:]
declarations = sorted(list(set(["(declare-fun v_" + str(abs(int(lit))) + " () Bool)" for line in clauses_lines for lit in line.split(" ")[:-1]])))
assertions = ["(assert (or " + " ".join(["v_" + str(abs(int(lit))) if not lit.startswith("-") else "(not v_" + str(abs(int(lit))) + ")" for lit in line.split(" ")[:-1]]) + "))" for line in clauses_lines]
content = "(set-logic QF_UF)\n" + "\n".join(declarations + assertions) + "\n(check-sat)\n"
with open(dimacs_path + ".smt2", "w") as f:
  f.write(content) 
