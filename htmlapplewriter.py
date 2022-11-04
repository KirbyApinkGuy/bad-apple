import numpy as np
import cv2 as cv
import time
shades = ['1','0']
framesize = 1
badapple = False
if not badapple:
    while True:
        try:
            videodir = str(input("Enter Video Directory Here:"))
            video_capture = cv.VideoCapture(videodir)
            break
        except Exception:
            print('Invalid Directory. Enter a valid directory')
else:
    videodir = "Documents/badapple.mp4"
    fps = 30
print("Calibrate screen size, enter d when T gets to top of screen")
print("T")
while input("|") != "d":
    framesize += 1
print("ꓕ")
dim = (round((8/3)*framesize),framesize)
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
with open("webframes.txt", "w") as w:
    w.write("\n".join(frames))
