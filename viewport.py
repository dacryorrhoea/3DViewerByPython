import numpy as np

class Viewport:
    def __init__(self, W, H):
        self.W = W//2
        self.H = H//2
        self.polygons = []

    def ClearViewport(self):
        self.polygons = []

    def ProjectionToViewport(self, vertices, faces):
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 1) | (vertices < -1)] = 0
        vertices = vertices @ np.array([
            [self.W,       0, 0, 0],
            [     0, -self.H, 0, 0],
            [     0,       0, 1, 0],
            [self.W,  self.H, 0, 1]
        ])
        vertices = vertices[:, :2]

        for face in faces:
            if not ((vertices[face[0]][0] == self.W or vertices[face[0]][1] == self.H) or
                    (vertices[face[1]][0] == self.W or vertices[face[1]][1] == self.H) or
                    (vertices[face[2]][0] == self.W or vertices[face[2]][1] == self.H)):
                self.polygons.append([vertices[face[0]], vertices[face[1]], vertices[face[2]]])


