import cv2
import os

os.chdir("machine_learning/video_parsing")
print(os.listdir())

import cv2
vidcap = cv2.VideoCapture('sample.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1