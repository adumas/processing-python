add_library('Ani')
lineLength = 360
backgroundColor = color(219, 59, 107)
W = 500
H = 500
rW = 175
spacing = 4
x_start = W/2-rW/2+spacing
lines = range(1,rW-spacing,floor(spacing))
step = 0

def setup():
    size(W,H);
    
def draw():
    background(backgroundColor)
    
    noStroke()
    pushMatrix()
    translate(x_start,0)
    rect(0,0,rW,lineLength)
    
    strokeWeight(2)
    stroke(0)
    for ii in lines:
        line(ii+2,0,ii+2,lineLength)
    popMatrix()
    
    pushMatrix()
    global step
    step += 1;
    deg = 4*sin((PI/50)*step)
    
    if step == 100:
        noLoop()
    
    translate(x_start-22,100)
    raddeg = radians(deg)
    print step, raddeg
    rotate(raddeg)
    
    for ii in lines:
        line(ii+2,0,ii+2,lineLength)
    popMatrix()
    
    saveFrame("frame/lines-######.png")
    
