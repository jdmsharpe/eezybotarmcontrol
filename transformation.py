import numpy as np

def rotx(x: float) -> np.array:
    return np.array([[1, 0, 0, 0], \
                     [0, np.cos(x), -np.sin(x), 0], \
                     [0, np.sin(x), np.cos(x), 0], \
                     [0, 0, 0, 1]])

def roty(y: float) -> np.array:
    return np.array([[np.cos(y), 0, np.sin(y), 0], \
                     [0, 1, 0, 0], \
                     [-np.sin(y), 0, np.cos(y), 0], \
                     [0, 0, 0, 1]])

def rotz(z: float) -> np.array:
    return np.array([[np.cos(z), -np.sin(z), 0, 0], \
                     [np.sin(z), np.cos(z), 0, 0], \
                     [0, 0, 1, 0], \
                     [0, 0, 0, 1]])

def rotxyz(x: float, y: float, z: float) -> np.array:
    return rotz(z) @ roty(y) @ rotx(x)

def transx(lx: float) -> np.array:
    return np.array([[1, 0, 0, lx], \
                     [0, 1, 0, 0], \
                     [0, 0, 1, 0], \
                     [0, 0, 0, 1]])

def transy(ly: float) -> np.array:
    return np.array([[1, 0, 0, 0], \
                     [0, 1, 0, ly], \
                     [0, 0, 1, 0], \
                     [0, 0, 0, 1]])

def transz(lz: float) -> np.array:
    return np.array([[1, 0, 0, 0], \
                     [0, 1, 0, 0], \
                     [0, 0, 1, lz], \
                     [0, 0, 0, 1]])

def transxyz(lx: float, ly: float, lz: float) -> np.array:
    return np.array([[1, 0, 0, lx], \
                     [0, 1, 0, ly], \
                     [0, 0, 1, lz], \
                     [0, 0, 0, 1]])

def transform(x: float, y: float, z: float, lx: float, ly: float, lz: float) -> np.array:
    R = rotxyz(x, y, z)
    R[0, 3] = lx
    R[1, 3] = ly
    R[2, 3] = lz
    return R

# L1 = 92.0
# L2 = 135.0
# L3 = 147.0
# L4 = 87.0

# # DH table
# DH = np.array([[0,  0,     L1, np.pi/2],
#                 [0,  np.pi/2,  0,  np.pi/2],
#                 [L2, 0,     0,  np.pi/2],
#                 [L3, 0,     0,  0],
#                 [0,  -np.pi/2, 0,  0]])

# # Find number of rows in DH table
# rows, cols = DH.shape

# # Pre-allocate Array to store Transformation matrix
# T = np.zeros((4, 4, rows), dtype=float)

# # Determine transformation matrix between each frame
# for i in range(rows):
#     T[:, :, i] = [[np.cos(DH[i, 3]),              -np.sin(DH[i, 3]),               0,             DH[i, 0]],
#                     [np.sin(DH[i, 3])*np.cos(DH[i, 1]),  np.cos(DH[i, 3]) *
#                     np.cos(DH[i, 1]), -np.sin(DH[i, 1]), -np.sin(DH[i, 1])*DH[i, 2]],
#                     [np.sin(DH[i, 3])*np.sin(DH[i, 1]),  np.cos(DH[i, 3]) *
#                     np.sin(DH[i, 1]),  np.cos(DH[i, 1]),  np.cos(DH[i, 1])*DH[i, 2]],
#                     [0,                          0,                          0,             1]]

# print(T[:,:,4] @ T[:,:,3] @ T[:,:,2] @ T[:,:,1] @ T[:,:,0])
# print(T[:,:,2])
# r = R.from_matrix(T[0:3,0:3,2])
# print(r.as_euler('zyx', degrees=True))
# print(T[:,:,4])
# print(rotx(np.pi/2) @ rotz(np.pi/6))
