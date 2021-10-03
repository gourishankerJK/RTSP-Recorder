import cv2
from .models import Camera,Recording
import numpy as np
import os
import cv2
from datetime import datetime
import threading
from django.conf import settings
from django.utils import timezone
from .serializer import RecordingSerializer,CameraSerializer

def Recorder(name,Camera_object,path):
	url = Camera_object.url
	time = datetime.now()
	filename = "recording"+time.strftime("%d_%a_%yT%H_%M_%S")+".avi"
	if path is None:
		path= os.path.join(settings.BASE_DIR,"Recordings\\",filename)
	else:
		path+=filename
	path.replace("\\","/")
	cap = cv2.VideoCapture(url)
	if cap.isOpened():
		t = threading.Thread(target = _recorder,args= (cap,Camera_object,path,time,filename))
		t.start()
		return ({"OK":"Accepted ,recording has started"},200)
	else :
		return ({'Error':"Camera Down"},500)
	
def _recorder(cap,Camera_object ,path,time,filename):
		frame_height,frame_width = int(cap.get(3)),int(cap.get(4))
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		out = cv2.VideoWriter(path,fourcc,25,(frame_height,frame_width))
		while Camera.objects.filter(name = Camera_object.name).first().status:
			ret,frame = cap.read()
			if ret:
				out.write(frame)
			else:
				status = False
				break
		else :
			 status = True
		cap.release()
		out.release()
		cv2.destroyAllWindows()
		cap = cv2.VideoCapture(path)
		if cap.isOpened():
			status = True
		else :
			status = False
		cap.release()
		cv2.destroyAllWindows()
		data = {
			'name':filename,
			'path':path,
			'recorded_time':time,
			 'status':status
		}
		serializer = RecordingSerializer(data = data)
		if serializer.is_valid():
			serializer.save(camera = Camera_object)
		serializer = CameraSerializer(Camera_object,data = {"status":False},partial = True)
		if serializer.is_valid():
			serializer.save()






			









