import time
import cv2 as cv

cap = cv.VideoCapture(0)
start_time = time.time()
time_elapsed = start_time - time.time()

fps = cap.get(cv.CAP_PROP_FPS)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

four_cc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
saved_image_frames = cv.VideoWriter('Project_video.avi', four_cc, fps, (int(frame_width), int(frame_height)))

start_time = time.time()

while int(time.time() - start_time) < 6:
    print(int(time.time() - start_time))
    ret, frame = cap.read()
    if ret:
        saved_image_frames.write(frame)
        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):         # if we want to pause the video before completion of 30 seconds
                                                     # press q from keyboard
            break
    else:
        break

cap.release()
saved_image_frames.release()
cv.destroyAllWindows()