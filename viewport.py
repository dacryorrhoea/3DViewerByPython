from matrices import *

class Viewport:
    def __init__(self, W, H):
        self.W = W//2
        self.H = H//2
        self.polygons = []

    def ClearViewport(self):
        self.polygons = []

    def ProjectionToViewport(self, mesh, cam):
        vertices = mesh.vertices @ Matrices.MatrixTransferToCameraScpace(cam.position, cam.right, cam.up, cam.forward)
        vertices = vertices @ Matrices.MatrixProjectionCameraSpace(cam.h_fov, cam.v_fov, cam.near_plane, cam.far_plane)
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 1) | (vertices < -1)] = 0
        vertices = vertices @ Matrices.MatrixProjectionViewport(self.W, self.H)
        vertices = vertices[:, :2]

        for face in mesh.faces:
            if not ((vertices[face[0]][0] == self.W or vertices[face[0]][1] == self.H) or
                    (vertices[face[1]][0] == self.W or vertices[face[1]][1] == self.H) or
                    (vertices[face[2]][0] == self.W or vertices[face[2]][1] == self.H)):
                self.polygons.append([vertices[face[0]], vertices[face[1]], vertices[face[2]]])


