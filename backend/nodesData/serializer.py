from rest_framework import serializers
from .models import Batsu_01, Batsu_02, Batsu_03, Batsu_04, Batsu_05

class nodesSerializer01 (serializers.Serializer):

    class Meta:
        models = Batsu_01
        fields = ['x_axis', 'y_axis', 'z_axis', 'temp', 'dateTime']

class nodesSerializer02 (serializers.ModelSerializer):
    
    class Meta:
        models = Batsu_02
        fields = ['x_axis', 'y_axis', 'z_axis', 'temp', 'dateTime']

class nodesSerializer03 (serializers.ModelSerializer):
    
    class Meta:
        models = Batsu_03
        fields = ['x_axis', 'y_axis', 'z_axis', 'temp', 'dateTime']

class nodesSerializer04 (serializers.ModelSerializer):
    
    class Meta:
        models = Batsu_04
        fields = ['x_axis', 'y_axis', 'z_axis', 'temp', 'dateTime']

class nodesSerializer05 (serializers.ModelSerializer):
    
    class Meta:
        models = Batsu_05
        fields = ['x_axis', 'y_axis', 'z_axis', 'temp', 'dateTime']
