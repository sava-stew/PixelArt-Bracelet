from constraint import Problem

problem = Problem()

strings = [0, 1, 2, 3]

problem.addVariables(strings, ['p', 'g', 'o'])

problem.addVariable('s11', strings[:2])
problem.addVariable('s12', strings[:2])
problem.addVariable('s13', strings[2:])
problem.addVariable('s14', strings[2:])

problem.addVariable('s21', strings)
problem.addVariable('s22', strings)
problem.addVariable('s23', strings)
problem.addVariable('s24', strings)


# Constraint Type 1:
problem.addConstraint(lambda s11, s12, *colors: 'p' in (colors[s11], colors[s12]), ('s11', 's12', *strings))
problem.addConstraint(lambda s13, s14, *colors: 'g' in (colors[s13], colors[s14]), ('s13', 's14', *strings))

problem.addConstraint(lambda s11, *colors: colors[s11] == 'g', ('s11', *strings))
problem.addConstraint(lambda s12, s13, *colors: 'p' in (colors[s12], colors[s13]), ('s12', 's13', *strings))
problem.addConstraint(lambda s14, *colors: colors[s14] == 'g', ('s14', *strings))

problem.addConstraint(lambda s21, *colors: colors[s21] == 'g', ('s21', *strings))
problem.addConstraint(lambda s22, s23, *colors: 'p' in (colors[s22], colors[s23]), ('s22', 's23', *strings))
problem.addConstraint(lambda s24, *colors: colors[s24] == 'g', ('s24', *strings))

problem.addConstraint(lambda s21, s22, *colors: 'o' in (colors[s21], colors[s22]), ('s21', 's22', *strings))
problem.addConstraint(lambda s23, s24, *colors: 'p' in (colors[s23], colors[s24]), ('s23', 's24', *strings))

# Constraint Type 2:
problem.addConstraint(lambda s11, s21: s11 == s21, ('s11', 's21'))
problem.addConstraint(lambda s12, s13, s22, s23: (s12 == s22 and s13 == s23) or (s12 == s23 and s13 == s22), ('s12', 's13', 's22', 's23'))
problem.addConstraint(lambda s14, s24: s14 == s24, ('s14', 's24'))

print(problem.getSolution())
