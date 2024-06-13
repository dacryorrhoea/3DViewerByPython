import pygame as pg
from engine import *
from events import *

class App:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.engine = Engine(self.screen)

    def run(self):
        while True:
            self.engine.Rendering(self.screen)
            EventHandler.Events(self.engine)
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = App()
    app.run()