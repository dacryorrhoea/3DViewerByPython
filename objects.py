import numpy
from math import *

class Mesh:
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.edge = []

    def LoadObject(self, path_to_file):
        with open(path_to_file) as f:
            for line in f:
                if line.startswith('v '):
                    self.vertices.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    self.faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])

    def Rotate(self, a, axis):
        if   axis == 'x': Matr = numpy.array([
            [1,      0,       0, 0],
            [0, cos(a), -sin(a), 0],
            [0, sin(a),  cos(a), 0],
            [0,      0,       0, 1]
        ])
        elif axis == 'y': Matr = numpy.array([
            [ cos(a), 0, sin(a), 0],
            [      0, 1,      0, 0],
            [-sin(a), 0, cos(a), 0],
            [      0, 0,      0, 1]
        ])
        elif axis == 'z': numpy.array([
            [cos(a), -sin(a), 0, 0],
            [sin(a),  cos(a), 0, 0],
            [     0,       0, 1, 0],
            [     0,       0, 0, 1]
        ])

        self.vertices = self.vertices @ Matr

    def Transfer(self, pos):
        tx, ty ,tz, _ = pos
        M = numpy.array([
            [ 1,  0,  0, 0],
            [ 0,  1,  0, 0],
            [ 0,  0,  1, 0],
            [tx, ty, tz, 1]
        ])

        self.vertices = self.vertices @ M

    def Scale(self, s):
        M = numpy.array([
            [s, 0, 0, 0],
            [0, s, 0, 0],
            [0, 0, s, 0],
            [0, 0, 0, 1]
        ])

        self.vertices = self.vertices @ M

class Cube(Mesh):
    def __init__(self):
        self.vertices = numpy.array([
            (0, 0, 0, 1), (0, 10, 0, 1), (10, 10, 0, 1), (10, 0, 0, 1),
            (0, 0, 10, 1),(0, 10, 10, 1),(10, 10, 10, 1),(10, 0, 10, 1)
        ])
        self.faces = numpy.array([
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (0, 4, 5, 1),
            (2, 3, 7, 6),
            (1, 2, 6, 5),
            (0, 3, 7, 4)
        ])
        self.edge = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
