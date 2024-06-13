import numpy
from math import *
from matrices import *

class Camera:
    def __init__(self):
        # параметры позиции и направления камеры
        self.position = numpy.array([0.0, 0.0, 200.0, 1.0])
        self.forward = numpy.array([0.0, 0.0, 1.0, 1.0])
        self.up = numpy.array([0.0, 1.0, 0.0, 1.0])
        self.right = numpy.array([1.0, 0.0, 0.0, 1.0])
        # параметры области видимости камеры
        self.h_fov = pi / 2.0
        self.v_fov = self.h_fov * (900/1600)
        self.near_plane = 0.1
        self.far_plane = 100.0
        # параметры перемещения камеры
        self.move_speed = 1.0
        self.rotate_speed = 0.01

    def CameraChangeDirection(self, matrix_rotate):
        self.forward = self.forward @ matrix_rotate
        self.up = self.up @ matrix_rotate
        self.right = self.right @ matrix_rotate

    def CameraMoving(self, direction): 
        if   direction == 'RIGHT':
            self.position += self.right * self.move_speed
        elif direction == 'LEFT':
            self.position -= self.right * self.move_speed
        elif direction == 'UP':
            self.position += self.up * self.move_speed
        elif direction == 'DOWN':
            self.position -= self.up * self.move_speed
        elif direction == 'BACKWARD':
            self.position += self.forward * self.move_speed
        elif direction == 'FORWARD':
            self.position -= self.forward * self.move_speed
        elif direction == "ROTATE_X_LEFT":
            self.CameraChangeDirection(numpy.array(Matrices.MatrixRotateX(-self.rotate_speed)))
        elif direction == "ROTATE_X_RIGHT":
            self.CameraChangeDirection(numpy.array(Matrices.MatrixRotateX(self.rotate_speed)))
        elif direction == 'ROTATE_Y_LEFT':
            self.CameraChangeDirection(numpy.array(Matrices.MatrixRotateY(-self.rotate_speed)))
        elif direction == 'ROTATE_Y_RIGHT':
            self.CameraChangeDirection(numpy.array(Matrices.MatrixRotateY(self.rotate_speed)))