import pygame as pg

class EventHandler:
    def Events(engine):
        [exit() for i in pg.event.get() if i.type == pg.QUIT]

        key = pg.key.get_pressed()
        if key[pg.K_a]:
            engine.camera.CameraMoving('LEFT')
        if key[pg.K_d]:
            engine.camera.CameraMoving('RIGHT')
        if key[pg.K_w]:
            engine.camera.CameraMoving('UP')
        if key[pg.K_s]:
            engine.camera.CameraMoving('DOWN')
        
        if key[pg.K_EQUALS]:
            engine.camera.CameraMoving('FORWARD')
        elif key[pg.K_MINUS]:
            engine.camera.CameraMoving('BACKWARD')

        if key[pg.K_i]:
            engine.camera.CameraMoving('ROTATE_X_LEFT')
        elif key[pg.K_o]:
            engine.camera.CameraMoving('ROTATE_X_RIGHT')
        elif key[pg.K_k]:
            engine.camera.CameraMoving('ROTATE_Y_LEFT')
        elif key[pg.K_l]:
            engine.camera.CameraMoving('ROTATE_Y_RIGHT')