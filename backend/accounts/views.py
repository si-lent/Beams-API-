from rest_framework.permissions import AllowAny, BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import permissions
from rest_framework.views import APIView
from .serializer import User_Profile_Serializer
from .models import User_Profile
from rest_framework.response import Response
from rest_framework import status




class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

class User_Profile_View(APIView):

    permission_classes = [IsAuthenticated,]
    
    def get(self, request, format = None):
        profile = User_Profile.objects.all()
        serializer = User_Profile_Serializer (profile, many=True)
        return Response (serializer.data)

    def post(self, request, format = None):
        serializer = User_Profile_Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

