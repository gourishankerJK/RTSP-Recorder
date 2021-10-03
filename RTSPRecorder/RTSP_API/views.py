from django.shortcuts import render
from datetime import datetime
from .models import Camera,Recording
from .serializer import RecordingSerializer,CameraSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .recorder import Recorder

#overview of my api
@api_view(['GET'])
def apioverview(request):
    api_urls = {
        "Start Camera":'/start/',
        "Stop Camera":'/stop/',
        "File Check":'/file_checker/',
        "Get path": '/getpath/',
         "Setup Camera" : '/setup_camera/',
         'Get Filter Videos':"/getfiltervideos/?starttime = 'YYY/MM/DD/TH:M:S'&endtime ='YYY/MM/DD/TH:M:S'"

    }
    return (Response(api_urls))
#this is the function responsible for starting the camera
@api_view(['PUT'])
def start(request):
    name=request.data.get('name',None)
    location = request.data.get('location',None)
    try:
        camera = Camera.objects.filter(name=name).first()
    except Exception as e:
        return Response({'Error':str(e)},404)
    if camera.status:
        return Response({"Success":"Camera is already runing"},200)
    serializer = CameraSerializer(camera,data ={"status":True},partial=True)
    if serializer.is_valid():
        serializer.save()
        response , response_code = Recorder(name,camera,location)
        return (Response(response,response_code))
    else:
        return Response({"error":serializer.errors},420)


#this is reponsible for stopping the camera
@api_view(['PUT'])
def stop(request):
    name=request.data.get('name',None)
    if name is not None:
        try:
            camera = Camera.objects.get(name=name)
        except Exception as e:
            return Response({"Error":str(e)},404)
        if camera.status is False:
            return Response({'Camera':f"{camera.name} is already stopped"},200)
        serializer = CameraSerializer(camera,{"status":False},partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(f"{name} is Stopped",200)
    else:
        return Response("Please,enter the name of camera",404)


@api_view(['GET'])
def file_checker(request):
    corrupt_videos = Recording.objects.filter(status=False)
    corrupt_videos = [video.path for video in corrupt_videos]
    good_videos = Recording.objects.filter(status=True)
    good_videos = [video.path for video in good_videos]
    return Response({'Corrupt_videos':good_videos,'Good_videos':good_videos},200)




@api_view(['POST'])
def setup_camera(request):
        cam_info = request.data.get("cam_info",None)
        if cam_info:
                serializer = CameraSerializer(data = cam_info)
                if serializer.is_valid():
                    serializer.save()
                    res = {"Success":"Camera url is set"}
                else:
                    res = {"Error":serializer.errors}
        else:
            res = {"Error":"data not passed by you"}
        
        return Response(res)


@api_view(['GET'])
def health_check(request):
    l = []
    camera = Camera.objects.filter(status = True)
    for cam in camera:
        l.append(cam.name)
    return Response({"Recording":l})


@api_view(['GET'])
def getpath(request):
        recording = Recording.objects.all()
        paths = [recording.path for recording in recording]
        return Response({"Paths":paths})


@api_view(['GET'])
def getfiltervideos(request):
    startdate = request.query_params.get('starttime')
    enddate = request.query_params.get('endtime')
    starthour,startminute,startsecond, endhour,endminute,endsecond =(0,0,0,0,0,0)

    try:
        startdate,startTime = startdate.split("T")
        enddate,endTime = enddate.split("T")
    except Exception as e:
        return Response({'Error':"Please enter the date as per format"})
    try:
        startyear,startmonth,startday =tuple(map(int ,startdate.split('-')))
        endyear,endmonth,endday =tuple(map(int,enddate.split('-')))
    except Exception as e:
        return Response({'Error':"Please enter the date as per format"})
    try :
        starthour,startminute,startsecond = tuple(map(int,startTime.split(":")))
        endhour,endminute,endsecond = tuple(map(int,endTime.split(':')))
    except :
        pass
    try:
        startdate = datetime(startyear,startmonth,startday,starthour,startminute,startsecond)
        enddate = datetime(endyear,endmonth,endday, endhour,endminute,endsecond )
    except Exception as e:
        return Response({"Error":str(e)})
    requested_recording = Recording.objects.filter(recorded_time__gte = startdate,recorded_time__lte = enddate)
    filter_videos = [ video.path for video in requested_recording]
    return Response({"Filter Videos":filter_videos})



