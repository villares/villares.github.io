```python
"""
Page for the Processing Community Catalog 2021 - Alexandre B A Villares
"""

from math import dist
from itertools import product
from random import seed, randint

import py5
import numpy as np

caption = 'Created with Processing + Python 3, using the py5 library. Code at <abav.lugaralgum.com/selected-work/processing2021>.'

def setup():
    global npa
    py5.size(2250, 3000)
    isb = py5.create_font("Inconsolata SemiBold", 24)
    py5.text_font(isb)
    s = 1
    seed(s)
    npa = np.empty((py5.width, py5.height)).T
    npa.fill(255)
    grid(128, 94 + 128, py5.width - 256, extra=True)
    py5.set_np_pixels(npa, 'L')
    py5.fill(0)
    py5.text(caption, 800, 2950)
    py5.save_frame(f'processing_20_years_catalog_seed{s}.TIF')
    print('done')

   
def grid(xo, yo, w, extra=False):
    qw = w // 4
    for i in range(4):
        x = xo + i * qw
        for j in range(4 + extra):
            y = yo + j * qw
            r = randint(1, 3)
            if qw > 64 and r == 1:
                grid(x, y, qw)
            elif r == 2:
                py5.stroke(255)
                region(x, y, qw, qw, inside)
            else:
                py5.stroke(255)
                region(x, y, qw, qw, outside)

def region(xo, yo, w, h, rule, overlap=0.25):
    o = int(w * overlap)
    for x, y in product(range(xo - o, xo + w + o), range(yo - o, yo + h + o)):
        if rule(x - xo, y - yo, w, h):
            npa[y,x] = max(npa[y,x] - 84, 0)
      
def inside(x, y, w, h):
    return randint(0, w) < dist((x, y), (w / 2, h / 2))

def outside(x, y, w, h):
    return randint(0, w) > dist((x, y), (w / 2, h / 2))
          
py5.run_sketch()
```