from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import time
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS

# load OpenCV's Haar cascade for face detection,
# (This is faster than dlib's built-in HOG detector, but less accurate.)
detector_file = "model/haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(detector_file)

# create the facial landmark predictor.
predictor_file = "model/shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_file)

vs = PiVideoStream().start()
time.sleep(2.0)

while True:
    # load the input image, resize it, and convert it to grayscale
    frame = vs.read()
    image = imutils.resize(frame, width=500)

    # cvtColor: Converts an image from one color space to another.
    # Here, convert a RGB image to gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale frame by opencv's method
    rects = detector.detectMultiScale(gray, scaleFactor=1.1,
                                  minNeighbors=5, minSize=(30, 30),
                                  flags=cv2.CASCADE_SCALE_IMAGE)

    # loop over the face detections
    face_counter = 0
    for (x, y, w, h) in rects:
        # construct a dlib rectangle object from the Haar cascade bounding box
        rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))

        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # convert dlib's rectangle to a OpenCV-style bounding box
        # [i.e., (x, y, w, h)], then draw the face bounding box
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # show the face number
        cv2.putText(image, "Face #{}".format(face_counter + 1), (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # loop over the (x, y)-coordinates for the facial landmarks
        # and draw them on the image
        for (x, y) in shape:
            cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

        face_counter = face_counter + 1

    cv2.imshow("Frame", image)
    # show the output image with the face detections + facial landmarks
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
