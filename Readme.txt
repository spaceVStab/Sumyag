Simple Implementation for motion detection and image capture system in Raspberry Pi

The package uses `picamera` for image read which shall only be found in a Raspberry Pi.
Thus code can't be run in a PC.

To run the code in Raspberry Pi simply run the main.py with Python3

There are different parameters which can be set

You can look over the other three config files: picamConfig.py, motion.py and threadPicam.py for understanding the logic.

Simply import these files into main.py files and you can pass the parameters onto those above config files.

TODO:
1. The code now only runs in thread mode. 
2. The night mode is not added. The implementaition may not work with low light.
3. Pytest framework has to be added. (picamera only works with Raspbian system. Thus have work on it)
4. There might be some glitch during hardware run. The motion might not be detected properly.
5. Better detection algorithm