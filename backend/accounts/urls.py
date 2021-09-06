from django.urls import path

from .views import User_Profile_View



urlpatterns = [

    path ('profile/', User_Profile_View.as_view()),
]