x_offset = 0
y_offset = 0
paletteHeight = 300
paletteWidth = 300
x_init = 0
backgroundColor = color(250)

import wobbly_line as W

all_lines = []

# parameters
angle = 45  # random(0,60)
spacing_min = 25
spacing_randomness = 2
x_jitter = 3
y_jump_min = 5
y_jump_max = 10

def setup():
    size(300, 300)
    background(backgroundColor)
    
    global angleRadians, x_starts

    # find x-position
    gen_diff = lambda : random(spacing_min, spacing_min + spacing_randomness)
    #gen_diff = lambda : 40
    angleRadians = radians(angle)
    
    x_cutoff = paletteWidth + paletteHeight * tan(angleRadians)
    x_starts = [gen_diff()]
    
    while x_starts[-1] < x_cutoff:
        x_starts.append(round(x_starts[-1] + gen_diff()))

def draw():
    global y_max, x_max
    global x_init, x_diff
    global angle
    global all_lines
    background(backgroundColor)
    noFill()

    # box transforms (if offsets)
    if x_offset > 0 or y_offset > 0:
        translate(x_offset, y_offset)

    # diagnostic lines to frame box
    # line(-width,0,width,0)
    # line(-width,paletteHeight,width,paletteHeight)
    # line(0,-height,0,height)
    # line(paletteWidth,-height,paletteWidth,height)

    # diagnostic lines (angled)
    # line(-width,0,width,0)
    # line(0,-height,0,height)

    # draw wobbly line
    newline = lambda: W.wobbly_line(
        paletteWidth, paletteHeight, angle, x_jitter, y_jump_min, y_jump_max)
    if not all_lines:
        all_lines = [newline() for xx in x_starts]
    
    for idx,ll in enumerate(all_lines):
        
        ll.step()
        
        # rotations and spacing
        pushMatrix()
        # move it 
        translate(x_starts[idx], 0)
        # rotate!
        rotate(angleRadians)
        ll.display()
        popMatrix()
        #delay(10)

    
