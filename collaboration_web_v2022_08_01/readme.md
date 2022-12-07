
---

## Pôster para o Processing Community Day @ Coimbra 2022

Mais informações sobre o evento em https://pcdcoimbra.dei.uc.pt/2022/

![image](https://user-images.githubusercontent.com/3694604/206052681-f21a5ee9-b523-4fb5-8ea8-2bc74d12881c.png)

```python
import random  # sample, shuffle, seed
import py5     # https://py5coding.org

nodes = {}
unvisited_nodes = []
step = 6
NBS = ((-2, -2), (-2, 0), (-2, 2), (0,-2),
      (0, 2), (2, -2), (2,0), (2, 2))

COLORS = ( # PCD Coimbra colors!
    '#f2647a',
    '#eb9e5a',
    '#53c7ab',
    '#4955bf',
    '#8043d7'
    )

ox = oy = 0
save_pdf = False

def setup():
    global w, h, f
    py5.size(750, 1050)
    w, h = int(py5.width / 2 / step - 5), int(py5.height / 2 / step - 5)
    start(100)
    f = py5.create_font('Inconsolata', 12)

def start(rnd_seed):
    global s, nbs, colors
    s = rnd_seed
    random.seed(rnd_seed)
    nbs = list(NBS)
    random.shuffle(nbs)
    colors = list(COLORS) # I changed this, so not the same colors combos as in expo!
    random.shuffle(colors)
    nodes.clear()
    unvisited_nodes[:] = []
    x1, y1 = 0, 0
    unvisited_nodes.extend((
        (x1 + 0, y1 + 1),
        (x1 + 1, y1 + 0),
        (x1, y1),
    ))

def draw():
    global save_pdf
    if save_pdf:
        py5.begin_record(py5.PDF, f'PCD-Coimbra-seed{s}.pdf')
    py5.stroke_weight(2)
    py5.background(0)
    py5.translate(py5.width / 2 + ox * step, py5.height / 2 + oy * step)
    for n, v in nodes.items():
        xa, ya = n
        xb, yb, c, gen = v
        if visible(xa, ya) and visible(xb, yb):
            py5.stroke(colors[c % 4])
            py5.line(xa * step, ya * step, xb * step, yb * step)
    unvisited_nodes[:] = grow()
    py5.fill(colors[0])
    py5.text_font(f)
    py5.text(f'Alexandre B A Villares - seed: {s} - '
         'code at: https://abav.lugaralgum.com/collaboration_web_v2022_08_01',
         -py5.width / 2 + 5 * step, py5.height / 2 - 2.5 * step)
    if save_pdf:
        py5.end_record()
        save_pdf = False

def grow():
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        _, _, c, gen = nodes.get((x, y), (0, 0, len(unvisited_nodes), 0))
        if not visible(x, y):
            continue
        random.seed(gen // 13 + c)
        xnbs = random.sample(nbs, 6 - c * 2)
        for nx, ny in xnbs:
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, c, gen + 1)
                yield xnx, yny

def visible(x, y):
    return (abs((x + ox) * step) < py5.width / 2 - step * 5 and
            abs((y + oy) * step) < py5.height / 2 - step * 5)

def key_pressed():
    global save_pdf
    if py5.key == ' ':
        start(s + 10)
    elif py5.key == 'p':
        save_pdf = True

py5.run_sketch()

``` 
