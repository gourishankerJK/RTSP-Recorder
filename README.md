''''''  Instructions That are Required For the Setup '''''' 

1. Install all Required modules listed in requirements.txt
2. Django application is in app folder . open a terminal in base directory of application where manage.py file is located.
3. Fire the command ("python manage.py runserver") in terminal to start the server of our api.
4. To test our api open a new terminal in test directory where test.py file is located.
5. Make sure you have started api server , Then fire the command ("python3 test.py") in second terminal which is opened in test directory. when you fire ("python test.py") command you will see netx steps.




''''''  Instructions for Using Api ''''''

In all Requests (POST,PUT,GET) data can be only passed in JSON Format

1. First of all you should setup a camera in database.(you can add camera by test.py file)
Url for adding camera(Request Method : POST) : "http://127.0.0.1:8000/store_urls/"
data should be passed in this format (**List of camera info): 
        {
        "cam_info":
            {
		   "name":camera_name,
		   "url":url_of _camera,
		   "active_hours":"HH:MM:SS-HH:MM:SS" //in 24 hour format 
		    }
        }

2.  After adding the cameras to the system , you can start the recording.
 To start recording , send the command in the following format.
                 {
                    "name": Name of the camera,
                     'location': where the recording to be stored   //optional Default directory is where the django is +//Recording folder
                 }

url for start recording(Request Method : PUT) : "http://127.0.0.1:8000/start/"
(*** the recording will not stop untill you send a request to stop the camera or Current time will cross the active_hours)

3. To stop camera url is (Request Method : PUT):  "http://127.0.0.1:8000/stop"
  The request should be done in the following format:
     		{
     		  "name":name of the camera
     		}

4. To Check health of camera you can Check single camera's health by passing camera name in request body or if you want to see all camera's health simply pass "all" in request body
url  (Request Method : GET): "http://127.0.0.1:8000/health_check/?name=name of the camera" // if name = all is passed it will show the health of the cameras.


5. To Get all recording url is (Request Method : GET): "http://127.0.0.1:8000/getpath"
    It returns the path of all the recordings

6. To get filtered recording :
          url is http://127.0.0.1:8000/get_filter/?starttime=YYYY:MM:DDTHH:MM:SS&endtime=YYYY:MM:DDTHH:MM:SS

7. Corrupt Checker : This will return two lists first will valid videos and second will corrupted videos.
url (Request Method : GET): "http://127.0.0.1:8000/corrupt_checker"



''''''  Personal Info '''''' 
Name : Gouri Shanker
Phone Number : 8492804035
Address : Udhampur , Jammu&Kashmir
Current Job : Student (B.tech(2019,2023) Computer Science and Engineering)