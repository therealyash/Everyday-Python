# Condition Expressions
'''
Syntax
<expr1> if <conditional expression> else <expr2>
'''

# Example 1
a = 20
b = 20
print(True if a > b else False)

# Example 2
weight = 65
msg = 'Obese' if weight > 80 else 'Hefty' if weight > 60 else 'Normal'
print(msg)

# Example 3
cric_score = 0
msg = 'Duck' if cric_score == 0 else 'Half Century!' if cric_score == 50 else 'Century!' if cric_score == 100 else "Near to Half Century!" if cric_score > 0 and cric_score < 51 else "Near to Century!" if cric_score < 101 and cric_score > 50 else 'Invalid Score'
print(msg)

# Example 4
c = 25
d = 35
op = all((a > 0, b > 0))
print(op)
op = any((a < 0, b < 0))
print(op)
