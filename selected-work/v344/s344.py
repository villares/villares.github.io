# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
from random import choice
from cell import Cell
SKETCH_NAME = "s344"  # 20181208
OUTPUT = ".png"
mode = 0

caps_locked = True

CELL_SIZE = 12

xo, yo = 100, 100
xio, yio = 0, 0
s = 10


def setup():
    size(800, 800)
    global img, grid_size
    img = load_image("data/unifont-11.0.02.png")
    grid_size = width / CELL_SIZE
    Cell.grid = dict()


def init_grid(f=None):
    w, h = width // CELL_SIZE, height // CELL_SIZE
    for i in range(w):
        for j in range(h):
            if f is None:
                def state(i, j): return choice((True, False))
            else:
                state = p_ou_b(i, j)
            Cell.grid[(i, j)] = Cell((i, j), CELL_SIZE, state)


def p_ou_b(i, j):
    c = img.get(xo + i, yo + j)
    if c == color(0):
        return True
    else:
        return False


def draw():
    background(220)
    stroke_weight(1)
    # KeyEvent.VK_CAPS_LOCK is 20

    if caps_locked:
        rect_mode(CORNER)
        image(img, xio, yio)
        no_fill()
        stroke_weight(3)
        stroke(200, 0, 0)
        rect(xio + xo, yio + yo, grid_size, grid_size)
        init_grid(1)
    else:
        rect_mode(CENTER)
        for c in Cell.grid.values():
            c.update()
        for c in Cell.grid.values():
            c.plot(mode)


def key_pressed():
    global mode, caps_locked
    global xo, yo, xio, yio
    if key == CODED:

        if key_code == RIGHT and xo < img.width - 11:
            xo += 5
        if key_code == LEFT and xo > 10:
            xo -= 5
        if key_code == DOWN and yo < img.height - 11:
            yo += 5
        if key_code == UP and yo > 10:
            yo -= 5
    else:
        if key == "s" or key == "S":
            save_frame(SKETCH_NAME + "_###.png")
        if key in "01234567789":
            mode = int(key)
        if key == "-":
            mode = -1
        if key == " ":
            init_grid(lambda i, j: False)
        if key == "x":
            init_grid(lambda i, j: (i + j) % 2 == 0)
        if key == "r":
            init_grid()
        if key == TAB:
            caps_locked = not caps_locked
            
    if xo > width - grid_size:
        xio = width - grid_size - xo
    if yo > height - grid_size:
        yio = height - grid_size - yo



class Cell():
    # neighbours list
    NL = ((-1, -1), (+0, -1), (+1, -1),
          (-1, +0), (+0, +0), (+1, +0),
          (-1, +1), (+0, +1), (+1, +1))
    ONL = ((+0, -1),
           (-1, +0), (+0, +0), (+1, +0),
           (+0, +1))
    DNL = ((-1, -1), (+1, -1),
           (+0, +0),
           (-1, +1), (+1, +1))

    def __init__(self, index, cell_size, state=False):
        self.index = index
        self.state = state
        self.size_ = cell_size
        self.mouse_down = False
        i, j = index[0], index[1]
        self.pos = Py5Vector(self.size_ / 2 + i * self.size_,
                             self.size_ / 2 + j * self.size_)

    def update(self):
        # mouse over & selection treatment
        hs = self.size_ / 2
        px, py = self.pos.x, self.pos.y
        self.mouse_on = (px - hs < mouse_x < px + hs and
                         py - hs < mouse_y < py + hs)
        if self.mouse_on and is_mouse_pressed:
            self.mouse_down = True
        if self.mouse_down and not is_mouse_pressed:
            self.state = not self.state
            self.mouse_down = False
        if self.mouse_on:
            fill(128, 128)
        else:
            no_fill()
        stroke_weight(1)
        stroke(200)
        rect(self.pos.x, self.pos.y, self.size_, self.size_)

    def plot(self, mode):
        if self.state:
            stroke_weight(self.size_ / 5.)
            if mode == -1:
                fill(0)
                no_stroke()
                rect(self.pos.x, self.pos.y, self.size_, self.size_)
            if mode == 0:
                stroke(0)
                self.draw_lines(Cell.NL)
                self.draw_lines2(Cell.NL)
            elif mode == 1:
                stroke(0, 150, 0)
                self.draw_lines2(Cell.ONL)
            elif mode == 2:
                stroke(0, 0, 150)
                self.draw_lines(Cell.DNL)
            elif mode == 3:
                stroke(0, 150, 0)
                self.draw_lines2(Cell.ONL)
                stroke(0, 0, 150)
                self.draw_lines(Cell.DNL)
            elif mode == 4:
                stroke(0, 150, 0)
                self.draw_lines(Cell.DNL)
                stroke(0, 0, 150)
                self.draw_lines2(Cell.ONL)

    def draw_lines(self, nbs):
        third = self.size_ / 3
        i, j = self.index[0], self.index[1]
        for (ni, nj) in nbs:
            nb = Cell.grid.get((i + ni, j + nj), None)
            if nb and nb.state:
                line(self.pos.x + ni * third * 1.5,
                     self.pos.y + nj * third * 1.5,
                     self.pos.x, self.pos.y)
                ellipse(self.pos.x, self.pos.y, third, third)

    def draw_lines2(self, nbs):
        third = self.size_ / 3
        i, j = self.index[0], self.index[1]
        for (ni, nj) in nbs:
            nb = Cell.grid.get((i + ni, j + nj), None)
            if nb and nb.state:
                with push_matrix():
                    translate(self.pos.x, self.pos.y)
                    if ni == 0 and nj != 0:
                        line(-third, nj * third * 1.5, -third, 0)
                        line(+third, nj * third * 1.5, +third, 0)
                    elif nj == 0 and ni != 0:
                        line(ni * third * 1.5, -third, 0, -third)
                        line(ni * third * 1.5, +third, 0, +third)
                    else:
                        ellipse(0, 0, third * 2, third * 2)

