import numpy as np 
import cv2 as cv 
# HIER MOET DENK IK FF ZO'N LOOKUP TABLE KOMEN
def create_voxel_volume(width, height, depth): 
       
       """
       Creates a voxel volume of a certain size (wxhxd)
       outputs the array representation of this volume 
       """
       
       x = np.arange(0, width)
       y = np.arange(0, height)
       z = np.arange(0, depth)
       
       X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
       
       voxel_volume = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T
       
       return voxel_volume 

def project_points_to_image(points, rvec, tvec, intrinsics_matrix):
       
       """
       Given some points, projects to 2D points. Should be able to input the voxel volume to test this 
       """
       
       # make it to array if needed 
       points = np.asarray(points, dtype=np.float32) 
       
       # project points 
       points_2d, _ = cv.projectPoints(points, rvec, tvec, intrinsics_matrix, distCoeffs=None)
       
       # reshape 
       points_2d = points_2d.reshape(-1, 2)  # Shape (N, 2)
       
       return points_2d



"""
def dataPrint():
    for i_camera in range(1, 5):  # Loop through cameras
        calibration_data = get_calib_data(f'data/cam{i_camera}/calibration_data_camera{i_camera}.pkl')
        print('JOE HOEE{i_camera}: ' ,calibration_data)
        i_camera = i_camera+1

xx = dataPrint()
print(xx)"""

"""
CAMERA 1:
{'intrinsics': (array([[485.1177443 ,   0.        , 332.98365685],
       [  0.        , 484.9610468 , 202.75566137],
       [  0.        ,   0.        ,   1.        ]]), array([[-3.76727518e-01,  2.15054213e-01,  1.60041800e-03,
        -3.76677609e-04, -8.29090355e-02]])), 
        
        'extrinsics': (array([[ 0.95802775],
       [-0.2506112 ],
       [ 0.59182046]]), array([[ 1.54438396],
       [ 6.4532927 ],
       [31.96617062]]))}

CAMERA 2
{'intrinsics': (array([[487.83946971,   0.        , 326.60039139],
       [  0.        , 490.56175247, 221.5664529 ],
       [  0.        ,   0.        ,   1.        ]]), array([[-0.36319401,  0.18497725,  0.00094371,  0.00054592, -0.05772399]])), 
       
       'extrinsics': (array([[ 0.72706296],
       [ 0.06643008],
       [-0.03597984]]), array([[-2.22670362],
       [11.19159628],
       [26.87128088]]))}

CAMERA 3
{'intrinsics': (array([[489.44781609,   0.        , 323.73514956],
       [  0.        , 488.30979314, 230.29012934],
       [  0.        ,   0.        ,   1.        ]]), array([[-0.35650842,  0.16262734,  0.00168899, -0.0005054 , -0.03538211]])), 
       
       'extrinsics': (array([[ 0.42044901],
       [-0.66613475],
       [ 1.4708585 ]]), array([[-1.91692089],
       [ 7.67366606],
       [22.2919395 ]]))}

CAMERA 4
{'intrinsics': (array([[490.45580518,   0.        , 344.17748593],
       [  0.        , 492.54769547, 243.14202893],
       [  0.        ,   0.        ,   1.        ]]), array([[-0.38197332,  0.23846688, -0.00129589, -0.00099103, -0.10186802]])), 
       
       'extrinsics': (array([[ 1.00978892],
       [ 0.2791067 ],
       [-0.63964191]]), array([[-8.60383695],
       [ 8.28163153],
       [36.29197865]]))}


"""