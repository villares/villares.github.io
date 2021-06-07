---

## s140_s141_s142_v2020

<img src="s140_s141_s142_v2020.svg">

> Publicado em ANDRADE, Gisele (org.); [Multiverso](https://multiverso-docs.s3-sa-east-1.amazonaws.com/multiverso-1a-edicao.pdf), Rio de Janeiro, RJ : Barleu Edições, 2020. 

Esta obra é uma exploração da combinação de duas ideias frequentes na arte algorítmica. A primeira ideia é a recursividade, quando se tem funções que chamam a elas mesmas, até um certo limite, o caso base. Dessa maneira é possível, com muito pouco código, alcançar produtos visuais intrincados que se assemelham a formas fractais. Nos vértices de polígonos regulares foram desenhados outros polígonos e assim sucessivamente em cinco níveis.

A segunda ideia é a introdução de perturbações, ruído, com o uso de valores pseudo-aleatórios. Essas variações remetem a fenômenos naturais e podem propiciar surpresa, variedade, bem como singularidade ao produzir imagens sem repetição. Tornam-se possíveis “múltiplos únicos”, por meio de impressões digitais. Nesta composição a magnitude do efeito da função *random()* na posição dos vértices dos elementos se reduz a zero nas quatro colunas do meio, intensificada nas bordas.

Trata-se de um desdobramento de estudos produzidos no contexto do experimento artístico iniciado em janeiro de 2018, e em curso, em que são publicados diariamente esboços, *sketches*, ideias visuais expressadas por meio de programação, sempre acompanhados do código fonte, de forma que o código aqui apresentado é parte integrante do trabalho.

```python
"""
s140_s141_s142_v2020
Alexandre B A Villares - https://abav.lugaralgum.com
Based on 3 sketches from sketch-a-day project in 2018
Running on Processing 3.5.5 with Python Mode (3063)
"""
add_library('pdf')

def setup():
    size(1925, 875)
    randomSeed(20200803)
    pdf = createGraphics(width, height, PDF, "s140_s141_s142_v2020")
    beginRecord(pdf)
    noFill()
    strokeWeight(0.5)
    background(200)
    grid = 4
    space = 175
    translate(space / 2 - 10, space / 2)
    for x in range(grid):
        for y in range(grid):
            px = space / 2 + x * space
            py = space / 2 + y * space
            poly_shape(px, py, n=3+y, rnd=3-x, gen=5, scaling=0)
    translate(space * 3, 0)
    for x in range(1, grid):
        for y in range(grid):
            px = space / 2 + x * space
            py = space / 2 + y * space
            poly_shape(px, py, n=3+y, rnd=0, gen=5, scaling=x)
    translate(space * 3, 0)
    for x in range(1, grid):
        for y in range(grid):
            px = space / 2 + x * space
            py = space / 2 + y * space
            poly_shape(px, py, n=3+y, rnd=x, gen=5, scaling=3)
    endRecord()

def poly_shape(x, y, n, rnd, gen, scaling):
    with pushMatrix():
        translate(x, y)
        radius = map(scaling, 0, 3, gen * 6, gen ** 2 * 1.7)
        ps = createShape()  # to create a polygon on a ps PShape object
        ps.beginShape()
        a, step = 0, TWO_PI / n
        while a < TWO_PI:
            sx = cos(a - PI / 6) * radius
            sy = sin(a - PI / 6) * radius
            ps.vertex(sx + random(-rnd, rnd), sy + random(-rnd, rnd))
            a += step
        ps.endShape(CLOSE)  # end of PShape creation
        shape(ps, 0, 0)  # Draw the PShape
        if gen > 0:  # if the recursion 'distance'/'depth' allows...
            for i in range(ps.getVertexCount()):
                # for each vertex
                pv = ps.getVertex(i)  # gets vertex as a PVector
                # recusively call poly_shape with a smaller gen
                poly_shape(pv.x, pv.y, n, rnd, gen - 1, scaling)
```


