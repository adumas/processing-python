class wobbly_line:
    def __init__(self,paletteWidth,paletteHeight,angle,x_jitter,y_jump_min,y_jump_max):
        self.paletteWidth = paletteWidth
        self.paletteHeight = paletteHeight
        self.angle = angle
        self.x_jitter = x_jitter
        self.y_jump_min = y_jump_min
        self.y_jump_max = y_jump_max
        
        self.vertices = []
        
    def step(self):
        if not self.vertices:
            x0 = 0
            y0 = 0
            self.vertices.append([x0,y0])
        
        cvert = self.vertices[-1]
        x0 = cvert[0]
        y0 = cvert[1]
        
        #print x0,y0
        
        # additional padding to ensure line clears bottom
        y_add = (0.1*self.paletteHeight)/cos(self.angle)
        
        # loop to draw line using curveVertex
        #print "wee"
        xx = random(-self.x_jitter,self.x_jitter)
        yy = random(self.y_jump_min,self.y_jump_max)
        xsig = x0 + xx
        ysig = y0 + yy
        if not(xsig > self.paletteWidth*1.05 or ysig > (self.paletteHeight+y_add)/cos(self.angle)):
            #print "added " + str(xsig) + " "  + str(ysig)
            self.vertices.append([xsig, ysig])
            return True
        else:
            return False
    
    def display(self):
        # draw wobbly line
        vertices = list(self.vertices)
        v0 = vertices.pop(0)
        #print v0
        noFill()
        beginShape()
        vertex(v0[0],v0[1])
        for vert in vertices:
            curveVertex(vert[0], vert[1])
        endShape()