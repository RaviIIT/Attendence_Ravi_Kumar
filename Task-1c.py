import glob
import os
import cv2 as cv

path = 'task1_Ravi_Kumar/*.*'
RGB_dir_name = 'task1_RGB'

for img in glob.glob(path):
    filename = os.path.basename(img)
    name, ext = filename.split('.')
    n2 = 'task1_' + name
    sub_directory = RGB_dir_name + '/' + n2 + '/'
    os.makedirs(sub_directory, exist_ok=True)

    frames = cv.imread(img)
    img_cp_b = frames.copy()
    img_cp_g = frames.copy()
    img_cp_r = frames.copy()

    img_cp_b[:, :, 1] = 0
    img_cp_b[:, :, 2] = 0
    img_names_B = name + '_B' + '.jpg'

    img_cp_g[:, :, 0] = 0
    img_cp_g[:, :, 2] = 0
    img_names_G = name + '_G' + '.jpg'

    img_cp_r[:, :, 0] = 0
    img_cp_r[:, :, 1] = 0
    img_names_R = name + '_R' + '.jpg'

    cv.imwrite(os.path.join(sub_directory, img_names_R), img_cp_r)
    cv.imwrite(os.path.join(sub_directory, img_names_G), img_cp_g)
    cv.imwrite(os.path.join(sub_directory, img_names_B), img_cp_b)

cv.destroyAllWindows()
