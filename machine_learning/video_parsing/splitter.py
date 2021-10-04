import cv2
import os

import cv2

def extract_frames(seconds, filename, output_folder):
      
  vidcap = cv2.VideoCapture(filename)
  success,image = vidcap.read()
  clipname = filename.rsplit('/', 1)[-1]
  clipname = clipname[:-4]
  #measures placement in seconds
  time = 0

  while success:
    shotname = clipname+"-frame%d.jpg" % time
    cv2.imwrite(os.path.join(output_folder, shotname), image)     # save frame as JPEG file      
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(time*1000))    
    success,image = vidcap.read()
    print('Read frame', shotname, " - ", success)
    time += seconds # sets the new time for new frame


file = "/Users/tristansaldanha/Desktop/torrents/Dexters_lab/Dexter-01.mkv"
place = "/Users/tristansaldanha/Desktop/dexter_frames"

for e in range(10, 20):
  file = "/Users/tristansaldanha/Desktop/torrents/Dexters_lab/Dexter-%d.mkv" % e
  extract_frames(30, file, place)
