import numpy as np
import cv2 as cv
import filetype
shades = [' ','`','.',',',':',';','\'','\"','^','*','-','_','!','|','?','1','[',']','7','{','}','/','\\','+','=','<','>','?','2','3','4','5','6','0','8','%','$','&','#']
framesize = 1
badapple = False
videodir = 0
if not badapple:
    guess = filetype.guess(videodir)
    while guess == None or not guess.mime.startswith('video'):
        videodir = str(input("Enter Video Directory Here:"))
        guess = filetype.guess(videodir)
else:
    videodir = "Documents/badapple.mp4"
    aspectratio = 8/3
video_capture = cv.VideoCapture(videodir)
aspectratio = 2*int(input("Enter aspect ratio here\nHorizontal ratio:"))/int(input("Vertical ratio:"))
print("Calibrate screen size, enter d when T gets to top of screen")
print("T")
while input("|") != "d":
    framesize += 1
print("ꓕ")
dim = (round(aspectratio*framesize),framesize)
saved_frame_name = 0
numframes = int(video_capture.get(cv.CAP_PROP_FRAME_COUNT))
framenumber = 0
testframe = True
frames = []
starttime = 0
timeoffset = 0
while video_capture.isOpened():
    frame_is_read, frame = video_capture.read()
    if frame_is_read:
        img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        img = cv.resize(img,dim,interpolation=cv.INTER_AREA)
        converted = ""
        for i in img:
            for b in enumerate(i):
                # print(b)
                converted += (shades[round(b[1]/(255/(len(shades)-1)))])
            converted += '\\n'
        framenumber+= 1
        frames.append(converted)
        print(f"Processing frame {framenumber} out of {numframes}")
    else:
        print("Could not read the frame.")
        break
with open("frames.txt", "w") as w:
    w.write("\n".join(frames))
