from math import cos, sin, tan
import numpy

class Matrices:
    @staticmethod
    def MatrixRotateX(a):
        return numpy.array([
            [1, 0, 0, 0],
            [0, cos(a), -sin(a), 0],
            [0, sin(a), cos(a), 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def MatrixRotateY(a):
        return numpy.array([
            [ cos(a), 0, sin(a), 0],
            [0, 1, 0, 0],
            [-sin(a), 0, cos(a), 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def MatrixRotateZ(a):
        return numpy.array([
            [cos(a), -sin(a), 0, 0],
            [sin(a), cos(a), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
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
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [pos[0], pos[1], pos[2], 1]
        ])

    @staticmethod
    def MatrixTransferToCameraScpace(pos, right, up, forward):
        m1 = numpy.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-pos[0], -pos[1], -pos[2], 1]
        ])
        m2 = numpy.array([
            [right[0], up[0], forward[0], 0],
            [right[1], up[1], forward[1], 0],
            [right[2], up[2], forward[2], 0],
            [0, 0, 0, 1]
        ])
        return m1 @ m2

    @staticmethod
    def MatrixProjectionCameraSpace(h_fov, v_fov, near_plane, far_plane):
        return numpy.array([
            [2 / (tan(h_fov / 2) + tan(h_fov / 2)), 0, 0, 0],
            [0, 2 / (tan(v_fov / 2) + tan(v_fov / 2)), 0, 0],
            [0, 0, (far_plane + near_plane) / (far_plane - near_plane), 1],
            [0, 0, -2 * near_plane * far_plane / (far_plane - near_plane), 0]
        ])

    @staticmethod
    def MatrixProjectionViewport(W, H):
        return numpy.array([
            [W, 0, 0, 0],
            [0, -H, 0, 0],
            [0, 0, 1, 0],
            [W, H, 0, 1]
        ])
