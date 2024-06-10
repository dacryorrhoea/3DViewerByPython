import pygame as pg
import sys
from geometry import *

PINK = (230, 50, 230)
BLACK = (0, 0, 0)

clock = pg.time.Clock()
sc = pg.display.set_mode((800, 800))
cube = Object3D()
cube.CreateCube(Point3D(0, 0, -100), 200)
Scr = Screen()

a = 1
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    sc.fill(BLACK)

    if a <= 360:
        a += 0.1
    else:
        a = 1
    
    for i, point in enumerate(cube.vertices):
        vect = Rotate.RotateY(point.vector, a)
        cube.vertices[i].x = vect[0]
        cube.vertices[i].y = vect[1]
        cube.vertices[i].z = vect[2]

    Scr.CreatingProjection(cube)

    pg.draw.line(sc, PINK, [Scr.screen[0].x, Scr.screen[0].y], [Scr.screen[4].x, Scr.screen[4].y])
    pg.draw.line(sc, PINK, [Scr.screen[1].x, Scr.screen[1].y], [Scr.screen[5].x, Scr.screen[5].y])
    pg.draw.line(sc, PINK, [Scr.screen[2].x, Scr.screen[2].y], [Scr.screen[6].x, Scr.screen[6].y])
    pg.draw.line(sc, PINK, [Scr.screen[3].x, Scr.screen[3].y], [Scr.screen[7].x, Scr.screen[7].y])
    
    
    pg.draw.line(sc, PINK, [Scr.screen[0].x, Scr.screen[0].y], [Scr.screen[1].x, Scr.screen[1].y])
    pg.draw.line(sc, PINK, [Scr.screen[1].x, Scr.screen[1].y], [Scr.screen[2].x, Scr.screen[2].y])
    pg.draw.line(sc, PINK, [Scr.screen[2].x, Scr.screen[2].y], [Scr.screen[3].x, Scr.screen[3].y])
    pg.draw.line(sc, PINK, [Scr.screen[3].x, Scr.screen[3].y], [Scr.screen[0].x, Scr.screen[0].y])
    
    
    pg.draw.line(sc, PINK, [Scr.screen[4].x, Scr.screen[4].y], [Scr.screen[5].x, Scr.screen[5].y])
    pg.draw.line(sc, PINK, [Scr.screen[5].x, Scr.screen[5].y], [Scr.screen[6].x, Scr.screen[6].y])
    pg.draw.line(sc, PINK, [Scr.screen[6].x, Scr.screen[6].y], [Scr.screen[7].x, Scr.screen[7].y])
    pg.draw.line(sc, PINK, [Scr.screen[7].x, Scr.screen[7].y], [Scr.screen[4].x, Scr.screen[4].y])

    
    pg.display.update()
    pg.time.delay(60)
    
    