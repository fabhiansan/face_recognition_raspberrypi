
# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import pickle
import time
import cv2

vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# start the FPS counter
fps = FPS().start()

# loop over frames from the video file stream
img_counter = 1
start_time = time.time()
while True:
    frame = vs.read()
    # frame = imutils.resize(frame, width=200)
    # cv2.imshow("Facial Recognition is Running", frame)
#    key = cv2.waitKey(1) & 0xFF

 #   if key == ord("q"):
  #      break
    if time.time() - start_time >= 60:
        break
    fps.update()
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
