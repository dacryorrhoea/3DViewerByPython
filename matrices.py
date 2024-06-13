from math import cos, sin
import numpy

class Matrices:
    @staticmethod
    def MatrixRotateX(a):
        return numpy.array([
            [1,      0,       0, 0],
            [0, cos(a), -sin(a), 0],
            [0, sin(a),  cos(a), 0],
            [0,      0,       0, 1]
        ])
    
    @staticmethod
    def MatrixRotateY(a):
        return numpy.array([
            [ cos(a), 0, sin(a), 0],
            [      0, 1,      0, 0],
            [-sin(a), 0, cos(a), 0],
            [      0, 0,      0, 1]
        ])
    
    @staticmethod
    def MatrixRotateZ(a):
        return numpy.array([
            [cos(a), -sin(a), 0, 0],
            [sin(a),  cos(a), 0, 0],
            [     0,       0, 1, 0],
            [     0,       0, 0, 1]
        ])
    
    @staticmethod
    def MatrixScale(s):
        return numpy.array([
            [s, 0, 0, 0],
            [0, s, 0, 0],
            [0, 0, s, 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def MatrixTransfer(pos):
        return numpy.array([
            [ 1,  0,  0, 0],
            [ 0,  1,  0, 0],
            [ 0,  0,  1, 0],
            [pos[0], pos[1], pos[2], 1]
        ])
