from django.urls import path

from .views import batsuView01, batsuView02, batsuView03, batsuView04, batsuView05



urlpatterns = [

    path ('batsu01/',batsuView01.as_view()),
    path ('batsu02/',batsuView02.as_view()),
    path ('batsu03/',batsuView03.as_view()),
    path ('batsu04/',batsuView04.as_view()),
    path ('batsu05/',batsuView05.as_view()),
]