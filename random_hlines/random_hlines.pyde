class HLine(object):  # Class definition
  def __init__(self, ypos, stroke_color):  # Object constructor
    self.ypos = ypos
    self.stroke_color = stroke_color

  def display(self):  # Display method
    stroke(self.stroke_color)
    line(0, self.ypos, width, self.ypos)

itt = 0

def setup():
    size(300,300)
    background(127)

def draw():
    r = random(300)
    rc = color(random(255),random(255),random(255))
    h = HLine(r, rc)
    h.display()
