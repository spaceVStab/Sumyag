import threading
import time
import os
import random
import picamConfig
import time
import datetime
import picamera
import motion
from threadPicam import PiVideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera
from fractions import Fraction


sensitivity = 300

#threshold is the threshold for each pixel changes to detect the motion
threshold = 30

#testWidth is the width of the image which will be captured during the motion
imageWidth = 800

#testHeigth is the height of the image which will be captured during the motion
imageHeight = 600

# set the vertical flip to true, since camera is turned 180 degrees
vflip = True

#number of images to be taken 
no_Images = 15


#testWidth is the width of the image which will be analyzed during the motion
testWidth = 600

#testHegth is the heigth of the image which will be analyzed during the motion
testHeight = 480

#testFrames is defined for analyzing the motion
testFrames = 60

#imageFrames is defined for capturing the images
#imageFrames = 30

class CameraManager(threading.Thread):
	global testWidth, testHeight, testFrames
	def __init__(self, camera_id, app, height, width, fps, quality, vflip, sensitivity, threshold, num_images):
		threading.Thread.__init__(self)
		self.app = app
		self.camera_id = camera_id
		self.height = height
		self.width = width
		self.imageFrames = fps
		self.quality = quality
		self.vflip = vflip
		self.sensitivity = sensitivity
		self.threshold = threshold
		self.num_images = num_images
		self.initCameraMgr()

	def initCameraMgr(self):
		self.picam1 = picamConfig.picamConfig()
		self.picam1.setTestParam(testWidth,testHeight,testFrames)
		self.picam1.setImageParam(self.width,self.height,self.imageFrames, self.vflip)
		self.picam1.setMotionParam(self.sensitivity,self.threshold)
		#picam1.setImageRotation(imageRotAngle)
		self.picam1.setImageQuality(self.quality)
		self.picam1.printParam()
		self.picam1.setDirectory()

		try:
			self.imageFeed = PiVideoStream(self.picam1).start()
			self.motionFeed = motion.motionConfig(self.picam1)
		except Exception as ex:
			print("Exception in initCameraMgr!")
			print(ex)


	def run(self):
		time.sleep(1)
		self.capture1 = self.imageFeed.read()
		while True:
			self.capture2 = self.imageFeed.read()
			motionStatus = self.motionFeed.motionStatus(self.capture1,self.capture2)
			print("motionstatus: ",motionStatus,"\n")
			if motionStatus is True:
				print("Motion Found\n")
				print("Taking Images...\n")

				#stopping the PiVideoStream to capture images
				self.imageFeed.stop()
				time.sleep(0.5)

				#takeImages() gives back images in jpeg format with paramters defined above
				self.picam1.takeImages(no_Images)
				print("Images saved \n")
				try:
					self.imageFeed = PiVideoStream(self.picam1).start()
				except Exception as ex:
					print("Exception in initCameraMgr!")
					print(ex)
				time.sleep(1)
			self.capture1 = self.capture2
		return


