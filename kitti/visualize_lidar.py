import pykitti
import os
import numpy as np
import pcl
import pcl.pcl_visualization


def get_lidar(liadr_path):
    ## load pc
    pc = np.fromfile(liadr_path, dtype=np.float32)
    pc = pc.reshape((-1, 4))
    # pc = pc[:,0:3]
    return pc

def show_lidar(liadr_path):
    pc = get_lidar(liadr_path)
    cloud = pcl.PointCloud_PointXYZI()
    cloud.from_array(pc)
    visual = pcl.pcl_visualization.CloudViewing()
    visual.ShowGrayCloud(cloud, b'cloud')
    flag = True
    while flag:
        flag != visual.WasStopped()

if __name__ == '__main__':
    show_lidar("/home/yl/Dataset/DL_Tools/kitti/kitti_object_vis/data/object/training/velodyne/000000.bin")
