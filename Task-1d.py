import glob
import os
import cv2 as cv

path = 'task1_Ravi_Kumar/*.*'
directory_name = 'task1_image_FACE'
os.mkdir(directory_name)

for img in glob.glob(path):
    filename = os.path.basename(img)
    name, ext = filename.split('.')

    face_cascade = cv.CascadeClassifier('C:/Users/ravi0/PycharmProjects/ML_assignment/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    image = cv.imread(img)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cropped_image_name = 'task1_' + name + '_FACE' + '.jpg'
        crop_img = image[y:y + h, x:x + w]
        cv.imwrite(os.path.join(directory_name, cropped_image_name), crop_img)

cv.destroyAllWindows()