#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Author : sosorry
# Date   : 05/31/2015
# Origin : http://blog.miguelgrinberg.com/post/video-streaming-with-flask

import cv2
import imutils
import time
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS


class Camera(object):
    def __init__(self):
        """if cv2.__version__.startswith('2'):
            PROP_FRAME_WIDTH = cv2.cv.CV_CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
        else:
            PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT"""

        self.video = cv2.VideoCapture(0)
        time.sleep(2.0)
        #self.video.set(PROP_FRAME_WIDTH, 640)
        #self.video.set(PROP_FRAME_HEIGHT, 480)
        #self.video.set(PROP_FRAME_WIDTH, 320)
        #self.video.set(PROP_FRAME_HEIGHT, 240)

    #def __del__(self):
     #   self.video.release()

    def get_frame(self):
        image = self.video.read()

        #mage = imutils.resize(image, width=400)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        detector = dlib.get_frontal_face_detector()

        predictor_file = "model/shape_predictor_68_face_landmarks.dat"
        predictor = dlib.shape_predictor(predictor_file)


        rects = detector(gray, 1)
        
        for (i, rect) in enumerate(rects):
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
            cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # loop over the (x, y)-coordinates for the facial landmarks
            # and draw them on the image
            for (x, y) in shape:
                cv2.circle(image, (x, y), 1, (0, 0, 255), -1)


        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tostring()
