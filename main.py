from vpython import *
canvas(background=color.green)
donut = ring(radius=0.5, thickness=0.25, color = vector(400,100,1))
donut_topping_layer = ring(radius=0.55, thickness=0.25, color = vector(0.4,0.2,0))

rad = 0
while True:
    rate(10)
    donut.pos = vector(3*cos(rad),sin(rad),0)                                        #donut.rotate(angle=1, axis=vector(0, 1, 0))
    donut_topping_layer.pos = vector(3 * cos(rad), sin(rad), 0)                      #donut_topping_layer.rotate(angle=1, axis=vector(0, 1, 0))
    rad = rad + 0.08