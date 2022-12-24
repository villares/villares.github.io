---

## sketch_2022_12_21d

> ![21](21.png)
> `rnd_seed = 21`

This is a simplified version of the code that generates the `sketch_2022_12_21d` series, it produces the same compositions to the provided random seed numbers. 


```python
import random 
import py5  # https://py5coding.org

NBS = ((-1, -1), (-2,  0), (-1, 1), (0, -2),
       ( 0,  2), ( 1, -1), ( 2, 0), (1,  1))

step = 8
rnd_seed = 21

nodes = {}
unvisited_nodes = []

def setup():
    global nbs, colors, orientation_offset

    py5.size(1200, 900)
    py5.color_mode(py5.HSB)
    py5.rect_mode(py5.CENTER)
    py5.no_stroke()

    w = int(py5.width / 2 / step - 5)
    h = int(py5.height / 2 / step - 5)
    
    random.seed(rnd_seed)
    nbs = list(NBS)
    random.shuffle(nbs)
    colors = {nb: py5.color(i * 16, 200, 200)
              for i, nb in enumerate(nbs)}
    random.shuffle(nbs)
    orientation_offset = {nb: i * py5.PI
                          for i, nb in enumerate(nbs)}
    unvisited_nodes[:] = [(random.randint(-w, w), random.randint(-h, h))
                           for _ in range(8)]

def draw():
    unvisited_nodes[:] = grow()

    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    for (x, y), (x0, y0, c, gen) in nodes.items():
        orientation = (x - x0, y - y0)  # delta/direction
        py5.fill(colors[orientation])
        d = (2 + py5.sin(gen / 5 + orientation_offset[orientation])) / 3
        py5.circle(x * step, y * step, d * step)

def grow():
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        _, _, i, gen = nodes.get((x, y), (0, 0, len(unvisited_nodes), 0))
        if (abs(x * step) > py5.width / 2 - step * 8 or
            abs(y * step) > py5.height / 2 - step * 8):
            continue
        random.seed(rnd_seed + i)
        xnbs = random.sample(nbs, 5)
        for nx, ny in xnbs:
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, i, gen + 1)
                yield xnx, yny

py5.run_sketch()
```

The actual code I used to generate the prints had a few tweaks: It had the `    unvisited_nodes[:] = grow()` inside a `while` loop in order to produce a finished composition in a single frame, it hade a `Py5Graphics` image buffer to provide a higher output resolution.
