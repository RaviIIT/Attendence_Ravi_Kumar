# Attendence_Ravi_Kumar
Task for selection of Video based Attendance project

If you are opening these projects and getting any red colour underlined line then you need to install some packages.
For this, click on FILE -> SETTINGS -> PYTHON INTERPRETER -> click on (+) sign -> search for opencv-python -> install package
All red lined errors will not appear now.

We will be going sequentially for our 4 files:-

.............................................................................Task-1a.py.......................................................................................... 

AIM -> Record a video from your webcam of 30 seconds duration and save it to an .avi file named 'Project_video.avi'.

We used time module of python to get first the starting time of project and then we are subtracting current time from starting time to get the total time duration so that recorded video is of 30 seconds duration.
Then we are capturing frame by frame images from our webcam and saving it to form a video by video writer.
If q button is pressed from keyboard before completion of 30 seconds the video saving procedure stops and saves till that time only, otherwise completes whole 30 seconds video and then task execution becomes successful.


.............................................................................Task-1b.py..........................................................................................
 
 AIM -> Save the frames captured from the 'Project_video.avi' to a folder named 'task1_Ravi_Kumar'
 
 We created a folder by mkdir method, named 'task1_Ravi_Kumar' to store images by mkdir function captured from the video 'Project_video.avi'. 
 We opened the recorded video by passing it's name and then storing images captured frame by frame from the video by imwrite method. Closing all the video frames and destroying     windows thereafter.
                
                
..............................................................................Task1c.py..........................................................................................   
AIM -> To store R,G, and B formats of all captured images into a subfolder named task1_<image_name> under a folder named task1_RGB.

To create subfolders under folders we used makedirs method. Then we made 3 copies to our individual images for our 3 channels and then made each channel 0 line bye line and stored them into task1_<image_name> folder (i.e. basically 3 images into 1 folder) by the imwrote method.


..............................................................................Task-1d.py.........................................................................................

AIM -> To store faces only from the images captured by the 'Project_video.avi'.

We created a folder named task1_image_FACE to store all the images containing cropped faces from the frames captured by 'Project_video.avi'.
We used HAAR CASCADE FRONTAL FACE CLASSIFIER to find the the dimensions and coordinates of the face in the given image.
Then we cropped the image based on the dimensions and coordinates and stored it into our folder by imwrite mwthod.





Following are the snaps of procedural working of Task1-a, Task1-b, Task1-c, Task1-d :-

(i) initially ss of folder. -> ![image](https://user-images.githubusercontent.com/75074493/125585976-039448dc-82f6-4785-ad6f-ae1f3754b0b6.png)

(ii) after executing Task1-a -> ![image](https://user-images.githubusercontent.com/75074493/125586336-1717af2e-c921-4330-94a0-51dc3c651435.png)

(iii) after executing Task1-b -> ![image](https://user-images.githubusercontent.com/75074493/125586524-434f56e3-a7bc-4786-b2dd-11357c218ee7.png)
                                 ![image](https://user-images.githubusercontent.com/75074493/125586549-744ecf5a-2223-45e8-807b-99ff92f625e6.png)
                                 
(iv) after executing Task1-c ->![image](https://user-images.githubusercontent.com/75074493/125586656-536cdbf9-e330-4f3f-8d5f-20b199f25518.png)
                               ![image](https://user-images.githubusercontent.com/75074493/125586765-3dd28437-b3ff-4b85-8de6-ef1db77c5793.png)
                               ![image](https://user-images.githubusercontent.com/75074493/125586789-16b2ce5b-3031-442a-aa49-fdec13ded413.png)

(v) after executing Task1-d -> ![image](https://user-images.githubusercontent.com/75074493/125587007-ce2dd874-bfd0-49b1-ad43-167e407fa366.png)
                               ![image](https://user-images.githubusercontent.com/75074493/125587096-b83c9775-7fda-4235-ae48-b3532c08b044.png)







!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  THANKS   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
