# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import time
import cv2
from imutils import resize
import sys
from requests import get, post
import uuid

API_ENDPOINT = "http://192.168.1.8:3000/face"
IMAGE_ENDPOINT = "http://192.168.1.8:3000/faceimage"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = int(sys.argv[1])
        if len(sys.argv) > 2:
            res2 = int(sys.argv[2])
    vs = VideoStream(usePiCamera=True, resolution=(res, res2)).start()
    time.sleep(2.0)
    
    # start the FPS counter
    fps = FPS().start()

    # loop over frames from the video file stream
    img_sent = 0
    start_time = time.time()
    model = cv2.CascadeClassifier("./model/haarcascade_frontalface_default.xml")
    frame_counter = 0
    emotion_list = []
    while True:
        frame = vs.read()
        # frame = cv2.imread("/home/pi/facial_recognition/dataset/Brillian/20230208-211036.jpg")
        frame = resize(frame, width=200)

        wajah = model.detectMultiScale(
            frame,
            scaleFactor=1.5,
            minNeighbors=2
        )
    
        if len(wajah) > 0:
            frame_counter += 1
            
            # detect wajah
            x, y, w, h = wajah[0]
            frame = cv2.rectangle(
                frame,
                (x, y),
                (x+w, y+h),
                (0, 0, 255),
                1
            )

            emotion = 1
            emotion_list.append(emotion)

        if frame_counter == 15:
            uuid_ = str(uuid.uuid4()) + ".jpg"
            cv2.imwrite(f"./img_saved/{uuid_}", frame)


        if frame_counter >= 30:
            emotion_final = "".join(str(x) for x in emotion_list)
            data_post = {
                'img_url' : f"{uuid_}.jpg",
                'emotion' : emotion_final   
            }
            r = post(url = API_ENDPOINT, data = data_post)
            
            files = {"files" : open(f"./img_saved/{uuid_}", 'rb').read()}
            r = post(IMAGE_ENDPOINT, files=files)
            print("image sent!")   
            frame_counter = 0 
            emotion_list = []

        cv2.imshow("Facial Recognition is Running", frame)
        key = cv2.waitKey(1) & 0xFF

    #    if key == ord("q"):
    #        break
        if time.time() - start_time >= 60:
            break

        fps.update()
    fps.stop()
    print(f"[INFO] Resolution = {res}, {res2}")
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()

