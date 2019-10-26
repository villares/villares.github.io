
---

## Slides da apresentação na Python Brasil 2019

# [slides_PyBR2019.pdf](slides_PyBR2019.pdf)

### árvore recursiva

<iframe src="https://abav.lugaralgum.com/sketch-a-day/2019/sketch_191025pybr2019/index.html" style="width: 500px; height: 500px; border: 0px"></iframe>

```python
"""Usando Processing Modo Python."""

def setup():
    size(500, 500)
 
def draw():
    background(240, 240, 200)
    translate(250, 300)
    galho(60)
    
def galho(tamanho):
    ang = radians(mouseX)
    encurtar = .8
    line(0, 0, 0, -tamanho)  
    if tamanho > 5:
        translate(0, -tamanho)
        rotate(ang)
        galho(tamanho * encurtar)  
        rotate(2 * -ang)
        galho(tamanho * encurtar) 
        rotate(ang)
        translate(0, tamanho)
    
```

### Sobre o zine/fôlder distribuido

# [desenho() #0_out_2019](http://desenho.lugaralgum.com/)


