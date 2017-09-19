import swingline as S

L = [S.swingline(theta,200,0.25) for theta in range(0,360,5)]

def setup():
    size(600,600)
    background(20)
    
def draw():
    background(40)
    global L
    strokeWeight(2)
    [l.step() for l in L]
    [l.display() for l in L]
    