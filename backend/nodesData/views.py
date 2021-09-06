from rest_framework.permissions import AllowAny, BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import permissions
from rest_framework.views import APIView
from .serializer import nodesSerializer01, nodesSerializer02, nodesSerializer03, nodesSerializer04, nodesSerializer05
from .models import Batsu_05, Batsu_04, Batsu_03, Batsu_01, Batsu_02
from rest_framework.response import Response


class batsuView01 (APIView):

    permission_classes = [IsAuthenticated]

    def get (self, request, format = None):
        data = Batsu_01.objects.all()
        serializer  = nodesSerializer01(data, many =True)
        return Response (serializer.data)

class batsuView02 (APIView):
    
    permission_classes = [IsAuthenticated]

    def get (self, request, format = None):
        data = Batsu_02.objects.all()
        serializer  = nodesSerializer01(data, many =True)
        return Response (serializer.data)

class batsuView03 (APIView):
    
    permission_classes = [IsAuthenticated]

    def get (self, request, format = None):
        data = Batsu_03.objects.all()
        serializer  = nodesSerializer01(data, many =True)
        return Response (serializer.data)

class batsuView04 (APIView):
    
    permission_classes = [IsAuthenticated]

    def get (self, request, format = None):
        data = Batsu_04.objects.all()
        serializer  = nodesSerializer01(data, many =True)
        return Response (serializer.data)

class batsuView05 (APIView):
    
    permission_classes = [IsAuthenticated]

    def get (self, request, format = None):
        data = Batsu_05.objects.all()
        serializer  = nodesSerializer01(data, many =True)
        return Response (serializer.data)



