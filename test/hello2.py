import ants
import cv2
import time

fixed_image = cv2.imread("fixed0.jpg", cv2.IMREAD_GRAYSCALE)
moving_image = cv2.imread("moving0.jpg", cv2.IMREAD_GRAYSCALE)

fixed_img = ants.from_numpy(fixed_image)
moving_img = ants.from_numpy(moving_image)

for i in range(1):
    start = time.time()
    # 3.进行配准
    outs = ants.registration(
        fixed=fixed_img,
        moving=moving_img,
        type_of_transform='SyN',
        useCompression=False,
        useHistogramMatching=True,
        smoothing_in_mm=True,
        aff_metric="meansquares",
        syn_metric="meansquares",
        verbose=False, )
    end = time.time()
    print(end - start)

registered_image = ants.apply_transforms(fixed=fixed_img, moving=moving_img, transformlist=outs["fwdtransforms"])

template_gary = cv2.imread("fixed0.jpg", cv2.IMREAD_GRAYSCALE)

ants_img = registered_image.numpy()

diff_img = cv2.absdiff(fixed_image, ants_img)

cv2.imwrite("diff3.jpg", diff_img)
# cv2.imshow("ants", diff_img)
# cv2.waitKey(0)
