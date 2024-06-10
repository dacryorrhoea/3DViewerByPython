import pygame as pg
from viewport import *
from objects import *
from camera import *

PINK = (230, 50, 230)
BLACK = (0, 0, 0)

class Engine:
    def __init__(self, screen):
        self.scene = [Mesh()]
        self.scene[0].LoadObject('obj/t_34_obj.obj')
        self.camera = Camera()
        self.viewport = Viewport(*screen.get_size())

    def Rendering(self, screen):
        # проецирование сцены
        self.viewport.ClearViewport()
        for mesh in self.scene:
            vertices = self.camera.TransferToCameraSpace(mesh.vertices)
            vertices = self.camera.ProjectionCameraSpace(vertices)
            self.viewport.ProjectionToViewport(vertices, mesh.faces)
        
        # отрисовка на экране
        screen.fill(BLACK)
        for polygon in self.viewport.polygons:            
            pg.draw.polygon(screen, PINK, polygon, 1)
