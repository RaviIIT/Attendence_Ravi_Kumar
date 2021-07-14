import os.path
import cv2 as cv

cap = cv.VideoCapture('Project_video.avi')

dir_name = 'task1_Ravi_Kumar'
os.mkdir(dir_name)
i = 0

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        i = i+1
        cv.imwrite(os.path.join(dir_name, 'frame_' + str(i) + '.jpg'), frame)

cap.release()
cv.destroyAllWindows()