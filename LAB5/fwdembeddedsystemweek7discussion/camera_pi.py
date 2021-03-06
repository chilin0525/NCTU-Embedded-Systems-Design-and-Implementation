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
        
        

        self.video =PiVideoStream().start()
        #time.sleep(2.0)
        #self.video = cv2.VideoCapture(1)
        #self.video.set(PROP_FRAME_WIDTH, 640)
        #self.video.set(PROP_FRAME_HEIGHT, 480)
        #self.video.set(PROP_FRAME_WIDTH, 320)
        #self.video.set(PROP_FRAME_HEIGHT, 240)
    
    #def __del__(self):
     #   self.video.release()
    
    def get_frame(self):
        image = self.video.read()
        #mage = imutils.resize(image, width=400)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tostring()

