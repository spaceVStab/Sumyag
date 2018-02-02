from picamConfig import picamConfig

class motionConfig(object):
	def __init__(self, picam1):
		self.picam = picam1

		#importing the test images param from picamConfig
		self.testWidth, self.testHeight, self.testFrames = self.picam.getTestParam()

		#importing the motion detect param from picamConfig
		self.sensitivity, self.threshold = self.picam.getMotionParam()
		return

	def motionStatus(self,capture1,capture2):
		motionDetected = False
		pixColor = 1 # red=0 green=1 blue=2 since green is most detected
		pixChanges = 0;
		for w in range(0, self.testWidth):
		    for h in range(0, self.testHeight):
		        # get the diff of the pixel. Conversion to int
		        # is required to avoid unsigned short overflow.
		        pixDiff = abs(int(capture1[h][w][pixColor]) - int(capture2[h][w][pixColor]))
		        # print(pixChanges,pixDiff)
		        if  pixDiff > self.threshold:
		            pixChanges += 1
		        if pixChanges > self.sensitivity:
		        	#if threshold and sensitivity are crossed beyond the limits motion is present
		            motionDetected = True
		            return motionDetected
		#print("motion status  ",motionDetected)
		#print("pixchanges ",pixChanges)
		return motionDetected
