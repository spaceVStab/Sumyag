from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread
import picamConfig
#Note: This class is readily available from "imutils" package under picamera link: 
#https://github.com/jrosebr1/imutils/blob/master/imutils/video/pivideostream.py
class PiVideoStream:
	def __init__(self, picam1):
		# initialize the camera and stream
		testWidth, testHeight, testFrames = picam1.getTestParam()
		self.camera = PiCamera()
		resolution = (testWidth, testHeight)
		self.camera.resolution = resolution
		self.camera.framerate = testFrames
		self.rawCapture = PiRGBArray(self.camera, size=resolution)
		self.stream = self.camera.capture_continuous(self.rawCapture,
			format="rgb", use_video_port=True)

		# initialize the frame and the variable used to indicate
		# if the thread should be stopped
		self.frame = None
		self.stopped = False

	def start(self):
		# start the thread to read frames from the video stream
		t = Thread(target=self.update, args=())
		t.daemon = True
		t.start()
		return self

	def update(self):
		# keep looping infinitely until the thread is stopped
		for f in self.stream:
			# grab the frame from the stream and clear the stream in
			# preparation for the next frame
			self.frame = f.array
			self.rawCapture.truncate(0)

			# if the thread indicator variable is set, stop the thread
			# and resource camera resources
			if self.stopped:
				self.stream.close()
				self.rawCapture.close()
				self.camera.close()
				return

	def read(self):
		# return the frame most recently read
		return self.frame

	def stop(self):
		# indicate that the thread should be stopped
		self.stopped = True
