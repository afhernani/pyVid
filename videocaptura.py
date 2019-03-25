
'''
If you just want to play an mp4 video, then this opencv program will help you to do that.
'''
import cv2

cap = cv2.VideoCapture("v2.mp4")
ret, frame = cap.read()
while(1):
   ret, frame = cap.read()
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
       cap.release()
       cv2.destroyAllWindows()
       break
   cv2.imshow('frame',frame)
'''
You can change the name of the window as you like. If video file is in another directory, then give the patch of the video in the format 'Drive://x/x/xx.mp4'. 'ret' value shows whether the video file is read or not, frame wise.
'''