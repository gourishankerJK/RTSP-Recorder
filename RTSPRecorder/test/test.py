import requests
import json

def start(name=None):
	URL = "http://127.0.0.1:8000/start/"
	if name is not None:
		data ={"name":name}
	json_data = json.dumps(data)
	header = {"content-type":'application/json'}
	r = requests.put(url=URL,headers=header,data=json_data)
	data = r.json()
	print(data)
def stop(name=None):
	URL = "http://127.0.0.1:8000/stop/"
	if name is not None:
		data ={"name":name}
	json_data = json.dumps(data)
	header = {"content-type":'application/json'}
	r = requests.put(url=URL,headers=header,data=json_data)
	data = r.json()
	print(data)
def health_check(name=None):
	URL = "http://127.0.0.1:8000/health_check/"
	header = {"content-type":'application/json'}
	r = requests.get(url=URL,headers=header)
	print(data)
def store_urls(cam_info=None):
	URL = "http://127.0.0.1:8000/store_urls/"
	if url is not None:
		header = {"content-type":'application/json'}
		r = requests.post(url=URL,headers=header,data=cam_info)
		data = r.json()
		print(data)
def getpath(name=None):
	URL = "http://127.0.0.1:8000/getpath/"
	header = {"content-type":'application/json'}
	r = requests.get(url=URL,headers=header)
	# r = requests.get(url=URL)
	data = r.json()
	print(data[0]["path"])
	print(data)
def filechecker():
	URL = "http://127.0.0.1:8000/file_checker/"
	header = {"content-type":'application/json'}
	r = request.get(URL,headers = header)
	print(r)

def getfiltervideos(request):
	URL = f"http://127.0.0.1:8000/getfiltervideos/?starttime={request['starttime']}&endtime={request['endtime']}"
	header = {"content-type":'multipart/form-data'}
	json_data = json.dumps(request)
	r = requests.get(url=URL,headers=header)	
	print(r)
s ='''Welcome you are in the tester of RTSPAPI
 	     First of all set the  for the Camera
 	     1.> To set the Camera press 1
 	     2.> To start recording press 2
 	     3.> To stop recording press 3
 	     4.> To check the health of Camera,press 4
 	     5.> To get the path of all recordings ,press 5
 	     6.>To  get the list of courrpt and uncoruppt recordings,press 7'''
print(s)
while True:
	n = int(input("Enter your choice:"))
	if n == 1:
		camera = input("Enter the name of camera: ")
		url = input("Enter the url of camera: ")
		active_hours = input("Enter the active hours: ")
		d = {
		   "name":camera,
		   "url":url,
		   "active_hours":active_hours
		}
		print(d)
		store_urls(d)
	elif n == 2:
		start(input("Enter the name of camera: "))
	elif n == 3:
		stop(input("Enter the name of camera: "))
	elif n == 4:
		print(health_check())
	elif n == 5:
		print(getpath())
	elif n == 6:
		print(filechecker())
	elif n == 7:
		starttime = input("Enter start time: ")
		endtime = input("Enter end time: ")
		data = {
		     'starttime':starttime,
		     'endtime':endtime
		}
		print(getfiltervideos(data))
	else :
		break


