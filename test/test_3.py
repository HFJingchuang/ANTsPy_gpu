import os
from ants import utils
import time
import numpy as np
import cv2

np.set_printoptions(suppress=True)

# 读取文件夹路径
moving_folder = r"E:\ANTsPy-master_gpu\ANTsPy-master\test\1344-524\QX"
output_folder = "registered_images"

# 获取文件夹中的所有图像文件名
moving_images = [os.path.join(moving_folder, file) for file in os.listdir(moving_folder) if file.endswith('.jpg')]

# 读取固定图像
fixed_image = cv2.imread(r"E:\ANTsPy-master_gpu\ANTsPy-master\test\1344-524\biaozhun\240326130151.jpg", cv2.IMREAD_GRAYSCALE)



# 转换固定图像形状
fixed_image = fixed_image.reshape((1344, 524), order="F")

# 获取 CUDA 加速的注册函数
cudaRegistration = utils.get_lib_fn("cudaRegistration")

# 遍历移动图像列表
for moving_image_path in moving_images:
    moving_image = cv2.imread(moving_image_path, cv2.IMREAD_GRAYSCALE)


    moving_image = moving_image.reshape((1344, 524), order="F")

    print("Registration start for:", moving_image_path)
    start = time.time()
    Gc = cudaRegistration(fixed_image, moving_image)
    end = time.time()
    print("Registration finished for:", moving_image_path, "Time taken:", end - start)

    # 转换固定图像数据类型
    fixed_image_int32 = fixed_image.astype(np.int32)

    # 将注册后的图像重塑为原始形状
    ants_img = Gc.reshape((524, 1344), order="F")

    # 计算固定图像和注册后图像的差异
    diff_img = cv2.absdiff(fixed_image_int32, ants_img)


    # 生成输出文件路径
    output_image_path = os.path.join(output_folder, os.path.basename(moving_image_path))

    # 保存图像
    cv2.imwrite(output_image_path, diff_img)

    print("Difference image saved for:", moving_image_path, "as:", output_image_path)
