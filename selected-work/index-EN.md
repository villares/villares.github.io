# toc

# selected work

<sub>[versão em português](index.md)</sub>

---

### Grafos (v2022_09)

Work for Processing Community Day @ Brasil 2022.

![image](https://user-images.githubusercontent.com/3694604/226963594-f51fd82c-cbf5-44c4-bf6f-f7f006f64113.png)

Can be seen executing at https://abav.lugaralgum.com/selected-work/grafos-2022-09/

---

### Webs of collaboration

A poster generator for Processing Community Day @ Coimbra 2022. Mais informações sobre o evento em https://pcdcoimbra.dei.uc.pt/2022/

![image](https://user-images.githubusercontent.com/3694604/206052681-f21a5ee9-b523-4fb5-8ea8-2bc74d12881c.png)

Códe at https://abav.lugaralgum.com/collaboration_web_v2022_08_01

---

### Schools in Brazil

Published at *Internet e Sociedade,* n.2, v.2, Dec. 2021, available at [**revista.internetlab.org/escolas-no-brasil**](https://revista.internetlab.org/escolas-no-brasil).

![Escolas no Brasil](https://revista.internetlab.org.br/wp-content/uploads/2022/03/villaresdesenho-1024x1024.jpg) 

``` python
"""
Inspirado em uma demonstração feita pelo professor Fernando Massanori, este desenho
é produzido a partir de microdados do censo escolar 2020 que podem ser encontrados em
https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar
Varrendo cada uma das 181279 escolas em funcionamento encontradas nos dados,
dispostas em uma grade invisível, círculos verdes e azuis variam conforme o número de
computadores disponíveis para os alunos, desktop e portateis respectivamente, os
quadrados vazados nestas mesmas cores resultam de entradas possívelmente incorretas
indicadas como 88888 na tabela. Quadrados pretos vazados são causados por escolas sem
Internet banda larga e quadrados pretos cheios por escolas sem energia elétrica.
"""

import pandas as pd
import py5

escolas =  pd.read_csv('escolas2.csv', sep='\t', low_memory=False)
print(f'total de registros: {len(escolas)}')
filtro = escolas['TP_SITUACAO_FUNCIONAMENTO'] == 1
escolas_funcionando = escolas[filtro]
computadores = escolas_funcionando['QT_DESKTOP_ALUNO']
portateis = escolas_funcionando['QT_COMP_PORTATIL_ALUNO']
internet_bl = escolas_funcionando['IN_BANDA_LARGA']
sem_luz = escolas_funcionando['IN_ENERGIA_INEXISTENTE']

escala = 2

def plot(x, y, n, cor, internet=False):
    py5.stroke(*cor)
    py5.no_fill()
    if n != n or (internet and n):  # filter* NaN
        pass
    elif internet and n == 0:
        py5.square(x * escala, y * escala, escala)
    elif n == 88888:
        py5.square(x * escala, y * escala, escala * 1.5)
    else:
        py5.circle(x * escala, y * escala, n * escala / 10)

def setup():
    py5.size(426 * 2, 426 * 2, py5.PDF, 'desenho2.pdf')
    py5.background(255)
    py5.stroke_weight(0.3)
    py5.rect_mode(py5.CENTER)
    x = y = 0
    for c, p, sbl, sl in zip(computadores, portateis, internet_bl, sem_luz):
        if sl == 1:        
            py5.fill(0)
            py5.no_stroke()
            py5.square(x * escala, y * escala, escala)  # sem luz, quadrado preto
        plot(x, y, c, (0, 200, 0))    # computadores desktop para alunos em verde
        plot(x, y, p, (0, 0, 200))    # computadores portáteis em azul            
        plot(x, y, sbl, (0, 0, 0), True)  # sem banda larga, quadrado preto vazado
        x += 1
        if x > 426:
            x = 0
            y += 1
    print('FIM')

py5.run_sketch()
```


---

### 2850 Triangle Interpolations v3 (2019)

> ![](assets/Triangle-Interpolations.jpg)
>
> *"A visual arts work in the domain of new media, it can also be described as an algorithmic work. It was executed in the context of exploring graphically combinatorics of elements using code. It also reflects the author's concerns about knowledge sharing, licensing of cultural artifacts, use of free tools, access to source code and demystification of algorithmic procedures."*

---

### s328 series, 2018—2020

> ![](assets/s328_photo.jpg)
>
> a328_2020 (photographic print)

> ![](assets/penplotter328.jpg)
>
> s328 + S (simplified variation for  pen plotter )

---

### desenho(), 2019

> ![gif animado com amostras da publicação](http://desenho.lugaralgum.com/assets/amostra-desenho0.gif)
>
> Something between zine, folder and poster, every copy is unique.

Acknoledgments and more information at **desenho.lugaralgum.com](http://desenho.lugaralgum.com:).** 

---

### sketch 190514c, 2019

> ![](assets/sketch_riso.jpg)
>
> Risograph poster 190414c 

---

### *sketch-a-day*  project, 2018—ongoing

![2018](assets/2018.gif)
![2019](assets/2019.gif)
![2020](assets/2020.gif)
![2021](assets/2021.gif)

An artistic experiment that began in January 2018, publishing daily sketches, visual ideas expressed with code at  **[abav.lugaralgum.com/sketch-a-day](http://abav.lugaralgum.com)**.

---

### Lousa mágica e Lousa paramétrica, 2017—2018

>[![frame de vídeo da lousa mágica](https://camo.githubusercontent.com/24628b40caf9943f12bdb845bcfcf161b55d4370/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f44354861316268714275512f302e6a7067)](https://www.youtube.com/watch?v=D5Ha1bhqBuQ)
>
>Video by [João Adriano Freitas](https://github.com/jaafreitas)

Código e instruções de montagem em [**abav.lugaralgum.com/lousa-magica**](https://abav.lugaralgum.com/lousa-magica/).

![](assets/exemplos_lousa.png)

> Amostra dos desenhos produzidos pelo público (principalmente crianças).

---

### Matriz 8x8 animada com Arduino, 2016

> ![](assets/Matriz8x8.jpg)
>
> Implementing a curated set of rules for Wolfram' s Celular Automata in a LED matrix.

In colaboration with **Tiago Queiroz**  for colective exhibition *Zonas de compensação 3.0*,  5 to  21 Oct,  2016 at the galery of the Unesp Arts Instutute (IA-Unesp), São Paulo.

Code repository: [WolframCellularAutomataArduino](https://github.com/villares/WolframCellularAutomataArduino/blob/master/WolframCellularAutomataArduino.ino).

