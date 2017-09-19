class swingline(object):  # Class definition
    def __init__(self, finalAngle,pix,pct=0.8,startAngle=-90,strokeColor=200):  # Object constructor
        self.finalAngle = finalAngle
        self.pix = pix
        self.currentAngle = float(startAngle)
        self.easing = 0.02
        self.pctDraw = pct
        self.strokeColor = strokeColor
        
        self.finalAngle = self.finalAngle + self.currentAngle
        
    def step(self):
        dtheta = float(self.finalAngle) - self.currentAngle
        self.currentAngle += dtheta * self.easing
    
    def display(self):  # Display method
        pushMatrix()
        translate(width/2,height/2)
        rotate(radians(self.currentAngle))
        stroke(self.strokeColor)
        line(self.pctDraw*self.pix, 0, self.pix, 0)
        popMatrix()