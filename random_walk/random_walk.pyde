x_offset = 0
y_offset = 0
paletteHeight = 300
paletteWidth = 300
x_init = 0

import wobbly_line as W


# parameters
angle = 0 #random(0,60)
spacing_min = 5
spacing_randomness = 20
x_jitter = 10
y_jump_min = 10
y_jump_max = 20

def setup():
  size(300,300)
  background(240)

def draw():
    global y_max, x_max
    global x_init, x_diff
    global angle
    
    noFill()
    
    # box transforms (if offsets)
    if x_offset > 0 or y_offset > 0:
        translate(x_offset,y_offset)
    
    # diagnostic lines to frame box 
    #line(-width,0,width,0)
    #line(-width,paletteHeight,width,paletteHeight)
    #line(0,-height,0,height)
    #line(paletteWidth,-height,paletteWidth,height)
    
    # rotations and spacing
    rot = radians(angle)
    pushMatrix()
    
    # find x-position
    x_diff = random(spacing_min,spacing_min+spacing_randomness)
    x_diff = 40
    x_init += x_diff
    translate(x_init,0)
    
    # rotate!
    rotate(rot)
    
    ## diagnostic lines (angled)
    #line(-width,0,width,0)
    #line(0,-height,0,height)
    
    # draw wobbly line
    wline = W.wobbly_line(paletteWidth,paletteHeight,angle,x_jitter,y_jump_min,y_jump_max)

    while wline.step():
        print "going"
    
    wline.display()

    if x_init > paletteWidth+paletteHeight*tan(rot)-x_diff:
        noLoop()
    popMatrix()
    