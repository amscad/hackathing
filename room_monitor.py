#!/usr/bin/python
from subprocess import call
from datetime import datetime
import time
import os
import subprocess


RESOLUTION = "1280x720"


def init():
    # setup connection to google cloud
    # make sure there is a folder to save the pics
    pass


def capture(pic_name):
    #call(["fswebcam", "-d", "/dev/video0", "-r", "1280x720", "--no-banner", "./pics/%d.jpg" % pic_name])
    #call(["fswebcam", "-d", "/dev/video0", "-r", "1280x720", "--no-banner", "%s" % pic_name])
    call(["fswebcam", "-d", "/dev/video0", "-r", RESOLUTION, "--no-banner", "%s" % pic_name])
    
    
def upload_pic(pic_name):
	bashCommand = "gsutil cp %s gs://tmg_meeting_room_images" % pic_name
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()    

def delete_uploaded_pic(pic_name):
	if os.path.isfile(pic_name):
		os.remove(pic_name)
	else:    ## Show an error ##
		print("Error: %s file not found" % pic_name)
	

if __name__ == '__main__':
	init()
	
	try:
		while True:
			#dt = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
			#dtime = dt[0:4]+dt[5:7]+dt[8:10]+dt[11:13]+dt[14:16]+dt[17:19]
			#201809091 -> /pic/2018..
			#pic_name = './pics/{0}.jpg'.format(str(int(dtime)))
			pic_name = "meeting_room.jpg"
			capture(pic_name)
			
			upload_pic(pic_name)
			
			time.sleep(10)
			delete_uploaded_pic(pic_name)

	except KeyboardInterrupt: 
		print 'The end !'
