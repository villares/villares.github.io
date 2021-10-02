```python
import py5
from math import dist
from itertools import product
import random as rnd

def inside(x, y, w, h):
    return rnd.randint(0, w) < dist((x, y), (w / 2, h / 2))

def outside(x, y, w, h):
    return rnd.randint(0, w) > dist((x, y), (w / 2, h / 2))

def setup():
    py5.size(2250, 3000)
    isb = py5.create_font("Inconsolata SemiBold", 24)
    py5.text_font(isb)
    s = 1
    rnd.seed(s)
    py5.background(255)
    py5.load_np_pixels()
    grid(128, 94 + 128, py5.width - 256, extra=True)
    py5.update_np_pixels()
    py5.fill(0)
    py5.text('Created with Processing + Python 3, using the py5 library. Code at <abav.lugaralgum.com/selected-work/processing2021>.',
             800, 2950)
    #py5.apply_filter(py5.BLUR)
    py5.save_frame(f'processing_20_years_catalog_seed{s}.TIF')
    print('done')

   
def grid(xo, yo, w, extra=False):
    qw = w // 4
    for i in range(4):
        x = xo + i * qw
        for j in range(4 + extra):
            y = yo + j * qw
            r = rnd.randint(1, 3)
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
            py5.np_pixels[y,x,1:] = (max(py5.np_pixels[y,x,1] - 84, 0),
                                     max(py5.np_pixels[y,x,2] - 84, 0),
                                     max(py5.np_pixels[y,x,2] - 84, 0))
          
py5.run_sketch()


```