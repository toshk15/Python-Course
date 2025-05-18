import numpy as np

file_path = '/home/fernando/data/sets/nuscenes/samples/LIDAR_TOP/n008-2018-08-01-15-16-36-0400__LIDAR_TOP__1533151603547590.pcd.bin'

with open(file_path, "rb") as f:
    number = f.read(4)
    while number != b"":
        print(np.frombuffer(number, dtype=np.float32))
        number = f.read(4)