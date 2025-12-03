
<img width="950" height="950" alt="caneca-0" src="https://github.com/user-attachments/assets/02c3ac29-48cd-4492-ad1d-2130938c1f5d" />

Mais sobre L-Sytems no [material-aulas: L-System - Sistema de Lindenmayer](https://abav.lugaralgum.com/material-aulas/Processing-Python-py5/LSystem.html).

```python
# An L-System made with Python and py5 <py5coding.org>
# Alxandre B A Villares <abav.lugaralgum.com>

size(950, 950)
background(255)
stroke_weight(2)
step = 25
axiom = 'F'
rules = {'F': 'F[+F-F0]-F+[-F+F0]'}
angle = 22.5
iterations = 4
starting_sequence = axiom
for i in range(iterations):
    sequence = ''
    for symbol in starting_sequence:
        sequence = sequence + rules.get(symbol, symbol)
    starting_sequence = sequence
    
translate(width * 0.1, height * 0.95)
for symbol in sequence:
    if symbol == 'F':
        line(0, 0, 0, -step)
        translate(0, -step)
    elif symbol == '+':
        rotate(radians(-angle))
    elif symbol == '-':
        rotate(radians(angle))
    elif symbol == '[':
        push_matrix()
    elif symbol == ']':
        pop_matrix()
    elif symbol == '0':
        with push_style():
            fill(255, 0, 0)
            no_stroke()
            circle(0, 0, step / 3)


```
[experimente no editor online](https://abav.lugaralgum.com/material-aulas/pyp5js/py5mode/?sketch=JTIzJTIwQW4lMjBMLVN5c3RlbSUyMG1hZGUlMjB3aXRoJTIwUHl0aG9uJTIwYW5kJTIwcHk1JTIwJTNDcHk1Y29kaW5nLm9yZyUzRSUwQSUyMyUyMEFseGFuZHJlJTIwQiUyMEElMjBWaWxsYXJlcyUyMCUzQ2FiYXYubHVnYXJhbGd1bS5jb20lM0UlMEElMEFzaXplKDk1MCUyQyUyMDk1MCklMEFiYWNrZ3JvdW5kKDI1NSklMEFzdHJva2Vfd2VpZ2h0KDIpJTBBJTBBc3RlcCUyMCUzRCUyMDI1JTBBYXhpb20lMjAlM0QlMjAnRiclMEFydWxlcyUyMCUzRCUyMCU3QidGJyUzQSUyMCdGJTVCJTJCRi1GMCU1RC1GJTJCJTVCLUYlMkJGMCU1RCclN0QlMEFhbmdsZSUyMCUzRCUyMDIyLjUlMEFpdGVyYXRpb25zJTIwJTNEJTIwNCUwQSUwQXN0YXJ0aW5nX3NlcXVlbmNlJTIwJTNEJTIwYXhpb20lMEFmb3IlMjBpJTIwaW4lMjByYW5nZShpdGVyYXRpb25zKSUzQSUwQSUyMCUyMCUyMCUyMHNlcXVlbmNlJTIwJTNEJTIwJyclMEElMjAlMjAlMjAlMjBmb3IlMjBzeW1ib2wlMjBpbiUyMHN0YXJ0aW5nX3NlcXVlbmNlJTNBJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwc2VxdWVuY2UlMjAlM0QlMjBzZXF1ZW5jZSUyMCUyQiUyMHJ1bGVzLmdldChzeW1ib2wlMkMlMjBzeW1ib2wpJTBBJTIwJTIwJTIwJTIwc3RhcnRpbmdfc2VxdWVuY2UlMjAlM0QlMjBzZXF1ZW5jZSUwQSUyMCUyMCUyMCUyMCUwQXRyYW5zbGF0ZSh3aWR0aCUyMColMjAwLjElMkMlMjBoZWlnaHQlMjAqJTIwMC45NSklMEFmb3IlMjBzeW1ib2wlMjBpbiUyMHNlcXVlbmNlJTNBJTBBJTIwJTIwJTIwJTIwaWYlMjBzeW1ib2wlMjAlM0QlM0QlMjAnRiclM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBsaW5lKDAlMkMlMjAwJTJDJTIwMCUyQyUyMC1zdGVwKSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHRyYW5zbGF0ZSgwJTJDJTIwLXN0ZXApJTBBJTIwJTIwJTIwJTIwZWxpZiUyMHN5bWJvbCUyMCUzRCUzRCUyMCclMkInJTNBJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwcm90YXRlKHJhZGlhbnMoLWFuZ2xlKSklMEElMjAlMjAlMjAlMjBlbGlmJTIwc3ltYm9sJTIwJTNEJTNEJTIwJy0nJTNBJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwcm90YXRlKHJhZGlhbnMoYW5nbGUpKSUwQSUyMCUyMCUyMCUyMGVsaWYlMjBzeW1ib2wlMjAlM0QlM0QlMjAnJTVCJyUzQSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHB1c2hfbWF0cml4KCklMEElMjAlMjAlMjAlMjBlbGlmJTIwc3ltYm9sJTIwJTNEJTNEJTIwJyU1RCclM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBwb3BfbWF0cml4KCklMEElMjAlMjAlMjAlMjBlbGlmJTIwc3ltYm9sJTIwJTNEJTNEJTIwJzAnJTNBJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwd2l0aCUyMHB1c2hfc3R5bGUoKSUzQSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGZpbGwoMjU1JTJDJTIwMCUyQyUyMDApJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwbm9fc3Ryb2tlKCklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBjaXJjbGUoMCUyQyUyMDAlMkMlMjBzdGVwJTIwJTJGJTIwMyklMEE%3D)

