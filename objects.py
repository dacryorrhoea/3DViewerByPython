import numpy
from math import *
from matrices import *

class Mesh:
    def __init__(self):
        self.vertices = []
        self.faces = []

    def LoadObject(self, path_to_file):
        with open(path_to_file) as f:
            for line in f:
                if line.startswith('v '):
                    self.vertices.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    self.faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])

    def Rotate(self, a, axis):
        if   axis == 'x': Matr = numpy.array(Matrices.MatrixRotateX(a))
        elif axis == 'y': Matr = numpy.array(Matrices.MatrixRotateY(a))
        elif axis == 'z': numpy.array(Matrices.MatrixRotateZ(a))
        self.vertices = self.vertices @ Matr

    def Transfer(self, pos):
        M = numpy.array(Matrices.MatrixTransfer(pos))
        self.vertices = self.vertices @ M

    def Scale(self, s):
        M = numpy.array(Matrices.MatrixScale(s))
        self.vertices = self.vertices @ M