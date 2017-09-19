angle = 0
# 1 - exp(-tt/C)
finalScale = 2.0
nRot = 1
finalAngle = nRot*PI
nSteps = 100.
step = 0;
from math import *


def setup():
    size(500, 500,P3D)
    fill(255)
    rectMode(CENTER)

    global rcolor
    rcolor = newColor()

def newColor():
    rgb = [random(255), random(255),random(255)]
    return rgb

#logistic
def logistic(t):
    result = 1./(1+exp(-0.4*(t-nSteps/2)))
    return result

def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2*pi*var)**.5
    num = exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def overshoot(t):
    tt = float(t)/nSteps
    sigmoid = (1+erf(4.7*tt-2))/2.
    gauss = normpdf(tt,0.5,0.07)/12
    result = gauss+sigmoid
    return result


def draw():
    noStroke()
    background(200)
    global rcolor
    global step
    global oldColor

    if step >= nSteps:
        step = 0
        oldColor = rcolor
        rcolor = newColor()
    elif step == 0:
        oldColor = newColor()

    step += 1


    # draw big rectangle
    pushMatrix()
    translate(width / 2, height / 2)
    scale(finalScale)
    fill(oldColor[0],oldColor[1],oldColor[2])
    rect(0, 0, 200, 200)
    popMatrix()

    global angle
    #angle = lerp(0,finalAngle,step/nSteps)
    angle = finalAngle*overshoot(step)
    currentScale = finalScale*overshoot(step);
    c = radians(angle)
    translate(width / 2, height / 2)
    rotate(angle)
    scale(currentScale)
    fill(rcolor[0],rcolor[1],rcolor[2])
    rect(0, 0, 200, 200)

    #delay(250)