import numpy
from math import *

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

    def CameraMoving(self, direction): 
        if   direction == 'RIGHT':
            self.position += self.right * self.move_speed
        elif direction == 'LEFT':
            self.position -= self.right * self.move_speed
        elif direction == 'UP':
            self.position += self.up * self.move_speed
        elif direction == 'DOWN':
            self.position -= self.up * self.move_speed
        elif direction == 'FORWARD':
            self.position -= self.forward * self.move_speed
        elif direction == 'BACKWARD':
            self.position += self.forward * self.move_speed
        elif direction == "ROTATE_X_LEFT":
            Matr = numpy.array([
                [1,      0,       0, 0],
                [0, cos(-self.rotate_speed), -sin(-self.rotate_speed), 0],
                [0, sin(-self.rotate_speed),  cos(-self.rotate_speed), 0],
                [0,      0,       0, 1]
            ])
            self.forward = self.forward @ Matr
            self.up = self.up @ Matr
            self.right = self.right @ Matr
        elif direction == "ROTATE_X_RIGHT":
            Matr = numpy.array([
                [1,      0,       0, 0],
                [0, cos(self.rotate_speed), -sin(self.rotate_speed), 0],
                [0, sin(self.rotate_speed),  cos(self.rotate_speed), 0],
                [0,      0,       0, 1]
            ])
            self.forward = self.forward @ Matr
            self.up = self.up @ Matr
            self.right = self.right @ Matr
        elif direction == 'ROTATE_Y_LEFT':
            Matr = numpy.array([
                [ cos(-self.rotate_speed), 0, sin(-self.rotate_speed), 0],
                [      0, 1,      0, 0],
                [-sin(-self.rotate_speed), 0, cos(-self.rotate_speed), 0],
                [      0, 0,      0, 1]
            ])
            self.forward = self.forward @ Matr
            self.up = self.up @ Matr
            self.right = self.right @ Matr
        elif direction == 'ROTATE_Y_RIGHT':
            Matr = numpy.array([
                [ cos(self.rotate_speed), 0, sin(self.rotate_speed), 0],
                [      0, 1,      0, 0],
                [-sin(self.rotate_speed), 0, cos(self.rotate_speed), 0],
                [      0, 0,      0, 1]
            ])
            self.forward = self.forward @ Matr
            self.up = self.up @ Matr
            self.right = self.right @ Matr
        
        print(f'{self.position, self.forward, self.up, self.right}')

    def TransferToCameraSpace(self, vertices):
        m1 = numpy.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-self.position[0], -self.position[1], -self.position[2], 1]
        ])
        m2 = numpy.array([
            [self.right[0], self.up[0], self.forward[0], 0],
            [self.right[1], self.up[1], self.forward[1], 0],
            [self.right[2], self.up[2], self.forward[2], 0],
            [0, 0, 0, 1]
        ])
        return vertices @ (m1 @ m2)

    def ProjectionCameraSpace(self, vertices):
        NEAR   = self.near_plane
        FAR    = self.far_plane
        RIGHT  = tan(self.h_fov / 2)
        LEFT   = -RIGHT
        TOP    = tan(self.v_fov / 2)
        BOTTOM = -TOP

        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP - BOTTOM)
        m22 = (FAR + NEAR) / (FAR - NEAR)
        m32 = -2 * NEAR * FAR / (FAR - NEAR)
        m = numpy.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])

        return vertices @ m
