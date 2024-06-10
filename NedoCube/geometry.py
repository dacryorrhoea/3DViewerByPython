import numpy as np
from math import *

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
        self.vector = np.array([x, y, z])

class Rotate:
    @staticmethod
    def RotateX(vector, ang):
        rotate_x = np.array([
            [1, 0, 0],
            [0, cos(ang), -sin(ang)],
            [0, sin(ang), cos(ang)]
        ])
        return vector.dot(rotate_x)
        
    @staticmethod
    def RotateY(vector, ang):
        rotate_y = np.array([
            [cos(ang), 0 , sin(ang)],
            [0, 1, 0],
            [-sin(ang), 0, cos(ang)]
        ])
        return vector.dot(rotate_y)
        
    @staticmethod
    def RotateZ(vector, ang):
        rotate_z = np.array([
            [cos(ang), -sin(ang), 0],
            [sin(ang), cos(ang), 0],
            [0, 0, 1]
        ])
        return vector.dot(rotate_z)

class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Screen:
    def __init__(self):
        self.screen = []
        self.observer_x = 400
        self.observer_y = 400
        self.observer_z = 500

    def Render(self):
        pass

    def CreatingProjection(self, object3d):
        self.screen = list()
        for point3d in object3d.vertices:
            point2d = Point2D()
            point2d.x = ((self.observer_z * point3d.x) / (self.observer_z + point3d.z)) + self.x
            point2d.y = ((self.observer_z * point3d.y) / (self.observer_z + point3d.z)) + self.y
            self.screen.append(point2d)
            

class Object3D:
    def __init__(self, *args):
        self.vertices = list()
        if args:
            for point in args:
                self.vertices.append(point)

    def CreateCube(self, center, side):
        self.vertices.append(Point3D(center.x - side/2, center.y - side/2, center.z))
        self.vertices.append(Point3D(center.x + side/2, center.y - side/2, center.z))
        self.vertices.append(Point3D(center.x + side/2, center.y + side/2, center.z))
        self.vertices.append(Point3D(center.x - side/2, center.y + side/2, center.z))
        self.vertices.append(Point3D(center.x - side/2, center.y - side/2, center.z + side))
        self.vertices.append(Point3D(center.x + side/2, center.y - side/2, center.z + side))
        self.vertices.append(Point3D(center.x + side/2, center.y + side/2, center.z + side))
        self.vertices.append(Point3D(center.x - side/2, center.y + side/2, center.z + side))
