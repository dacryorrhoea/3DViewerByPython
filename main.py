import pygame as pg
from engine import *

class App:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.engine = Engine(self.screen)

    def EventHandler(self):
        [exit() for i in pg.event.get() if i.type == pg.QUIT]

        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.engine.camera.CameraMoving('LEFT')
        if key[pg.K_d]:
            self.engine.camera.CameraMoving('RIGHT')
        if key[pg.K_w]:
            self.engine.camera.CameraMoving('UP')
        if key[pg.K_s]:
            self.engine.camera.CameraMoving('DOWN')
        
        if key[pg.K_EQUALS]:
            self.engine.camera.CameraMoving('FORWARD')
        elif key[pg.K_MINUS]:
            self.engine.camera.CameraMoving('BACKWARD')

        if key[pg.K_i]:
            self.engine.camera.CameraMoving('ROTATE_X_LEFT')
        elif key[pg.K_o]:
            self.engine.camera.CameraMoving('ROTATE_X_RIGHT')
        elif key[pg.K_k]:
            self.engine.camera.CameraMoving('ROTATE_Y_LEFT')
        elif key[pg.K_l]:
            self.engine.camera.CameraMoving('ROTATE_Y_RIGHT')

    def run(self):
        while True:
            self.engine.Rendering(self.screen)
            self.EventHandler()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = App()
    app.run()