<script src="https://www.brython.info/src/brython_dist.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.5.0/p5.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.5.16/addons/p5.dom.js"></script>
<script type="text/python">
# brython + p5js.org adapted from code from Kiko Correoso
# with correction from Pierre Quentel
from browser import document, window, alert

def sketch(p):

    def setup():
        p.createCanvas(700, 410)
        p.background(0)
        p.rectMode(p.CENTER)
    
    def draw():
       # p.background(0)
        p.fill(255,255,0,128)
        p.ellipse(p.mouseX,p.mouseY,50,50)
    
    def mousePressed():
        p.background(0)
    
    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
      
myp5 = window.p5.new(sketch)
</script>
