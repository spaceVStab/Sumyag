"""
Sumyag
Author:Manish Agrawal

Code for the main picamera function calling
"""
import picamera
import threadPicam
import time
import os
import datetime
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
	def setImageParam(self, imageWidth=600,imageHeight=480, imageFrames=30,vflip = True):
		self.imageWidth = imageWidth
		self.imageHeight = imageHeight
		self.imageFrames = imageFrames
		self.vflip = vflip
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

	def setDirectory(self):
		currDirec = os.getcwd()
		dirName = 'photosCaptured'
		if not os.path.isdir(dirName):
			os.mkdir('photosCaptured')
		self.imageDirec = currDirec + '/'+ dirName + '/'
		os.chdir(self.imageDirec)
		return

	def takeImages(self, no_Images):
		time = (str(datetime.datetime.now()).split('.')[0]).split(' ')
		time = '_'.join(time)
		subDirec = time+'_imgfolder'
		os.mkdir(subDirec)
		os.chdir(os.getcwd()+'/'+subDirec+'/')
		self.no_Images = no_Images
		with picamera.PiCamera() as camera:
			camera.resolution = (self.imageWidth, self.imageHeight)
			camera.framerate = self.imageFrames
			#camera.rotation = self.rotAngle
			camera.vflip = self.vflip
			outputs = ['img{}_{}.jpeg'.format(i,(time)) for i in range(no_Images)]
			#print((outputs))
			camera.capture_sequence(outputs, 'jpeg', use_video_port=True,quality=self.quality)
		os.chdir(self.imageDirec)
		return

	#printing the set parameters
	def printParam(self):
		print("Test Width: ",self.testWidth,"Test Height: ",self.testHeight,"Test Frames: ",self.testFrames)
		print("Image Width: ",self.imageWidth,"Image Height: ",self.imageHeight,"Image Frames: ",self.imageFrames)
		print("Sensitivity: ",self.sensitivity,"Threshold: ",self.threshold)
		return