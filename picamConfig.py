"""
Sumyag
Author:Manish Agrawal

Code for the main picamera function calling
"""
import picamera
import threadPicam
import time
import os
from picamera.array import PiRGBArray 

class picamConfig(object):
	def __init__(self):
		return

	#setting the test parameters as set in main.py
	def setTestParam(self, testWidth=600,testHeight=480, testFrames=30):
		self.testWidth = testWidth
		self.testHeight = testHeight
		self.testFrames = testFrames
		return

	#setting the image parameters as set in main.py
	def setImageParam(self, imageWidth=600,imageHeight=480, imageFrames=30):
		self.imageWidth = imageWidth
		self.imageHeight = imageHeight
		self.imageFrames = imageFrames
		return

	#setting the motion parameters as set in main.py
	def setMotionParam(self, sensitivity=30, threshold=300):
		self.sensitivity = sensitivity
		self.threshold = threshold
		return

	def setImageRotation(self, angle):
		self.rotAngle = angle
		return

	def setImageQuality(self, quality = 50):
		#50 -> 100 to 120 KB
		self.quality = quality
		return

	#returning the test parameters for other operations
	def getTestParam(self):
		return(self.testWidth, self.testHeight, self.testFrames)

	#returning the test parameters for other operations
	def getImageParam(self):
		return(self.imageWidth, self.imageHeight, self.imageFrames)

	#returning the test parameters for other operation
	def getMotionParam(self):
		return(self.sensitivity, self.threshold)

	def getRotationAngle(self):
		return(self.rotAngle)

	#taking images after motion is attained as per set parameters
	def takeImages(self, no_Images):
		self.no_Images = no_Images
		currDirec = os.getcwd()
		dirName = 'photosCaptured'
		if not os.path.isdir(dirName):
			os.mkdir('photosCaptured')
		imageDirec = currDirec + '/'+ dirName + '/'
		os.chdir(imageDirec)
		with picamera.PiCamera() as camera:
			camera.resolution = (self.imageWidth, self.imageHeight)
			camera.framerate = self.imageFrames
			camera.rotation = self.rotAngle
			outputs = ["image_%d.jpeg"%i for i in range(no_Images)]
			camera.capture_sequence(outputs, 'jpeg', use_video_port=True,quality=self.quality)
		return

	#printing the set parameters
	def printParam(self):
		print("Test Width: ",self.testWidth,"Test Height: ",self.testHeight,"Test Frames: ",self.testFrames)
		print("Image Width: ",self.imageWidth,"Image Height: ",self.imageHeight,"Image Frames: ",self.imageFrames)
		print("Sensitivity: ",self.sensitivity,"Threshold: ",self.threshold)
		return