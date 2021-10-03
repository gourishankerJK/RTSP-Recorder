from django.urls import path
from . import views

urlpatterns = [
	path('',views.apioverview),
    path('file_checker/', views.file_checker),
    path('setup_camera/', views.setup_camera),
    path('start/', views.start),
    path('stop/', views.stop),
    path('getpath/', views.getpath),
    path('getfiltervideos/',views.getfiltervideos),
]