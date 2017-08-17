"""
Sumyag
Author:Manish Agrawal

main.py is the script where main objective is written
"""

import picamConfig
import time
import datetime
import picamera
import motion
from threadPicam import PiVideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera
from fractions import Fraction

#these are the pararmeter to be set

#sensitivity is the threshold for number o fpixel that has changed
sensitivity = 300

#threshold is the threshold for each pixel changes to detect the motion
threshold = 30

#testWidth is the width of the image which will be analyzed during the motion
testWidth = 800

#testHegth is the heigth of the image which will be analyzed during the motion
testHeight = 600

#testWidth is the width of the image which will be captured during the motion
imageWidth = 800

#testHeigth is the heigth of the image which will be captured during the motion
imageHeight = 600

#testFrames is defined for analyzing the motion
testFrames = 30

#imageFrames is defined for capturing the images
imageFrames = 30

#threading is True by nature
#TODO add for False
threading = True

#number of images to be taken 
no_Images = 15

def main():
	#create a instances of a testcamera and start detecting for the motion
	picam1 = picamConfig.picamConfig()

	#feeding in the camera parameters
	picam1.setTestParam(testWidth,testHeight,testFrames)
	picam1.setImageParam(imageWidth,imageHeight,imageFrames)
	picam1.setMotionParam(sensitivity,threshold)
	picam1.printParam()
	#creating an instance for threaded motion class PiVideoStream()
	#Note: the class PiVideoStream() can be found from package imutils under picamera link: 
	#https://github.com/jrosebr1/imutils/blob/master/imutils/video/pivideostream.py
	imageFeed = PiVideoStream(picam1).start()

	#creating an instance for motion detection passing the picam1 instance
	motionFeed = motion.motionConfig(picam1)

	#some time delay
	time.sleep(1)

	#tinit.read() captures an image array and saves it to capture1
	capture1 = imageFeed.read()
	while True:
		#tinit.read() captures an image array and saves it to capture2
		capture2 = imageFeed.read()

		#passing our captures to detect for motion
		motionStatus = motionFeed.motionStatus(capture1,capture2)
		#m = checkForMotion(capture1, capture2)
		if motionStatus is True:
			print("Motion Found\n")
			print("Taking Images...\n")

			#stopping the PiVideoStream to capture images
			imageFeed.stop()
			time.sleep(0.5)

			#takeImages() gives back images in jpeg format with paramters defined above
			picam1.takeImages(no_Images)
			print("Images saved \n")
			return
	return

if __name__ == "__main__":
	try:
		#initiation
		main()
	finally:
		print("*******\n Exiting Program")
