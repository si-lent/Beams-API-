from django.db import models

# Create your models here.
class Batsu_01 (models.Model):

    x_axis = models.FloatField(max_length=5)
    y_axis = models.FloatField(max_length=5)
    z_axis = models.FloatField(max_length=5)
    temp = models.FloatField (max_length=5)
    dateTime = models.DateTimeField()

    class Meta:
        db_table = "Batsu01" 

class Batsu_02 (models.Model):
    
    x_axis = models.FloatField(max_length=5)
    y_axis = models.FloatField(max_length=5)
    z_axis = models.FloatField(max_length=5)
    temp = models.FloatField (max_length=5)
    dateTime = models.DateTimeField()

    class Meta:
        db_table = "Batsu02" 

class Batsu_03 (models.Model):
    
    x_axis = models.FloatField(max_length=5)
    y_axis = models.FloatField(max_length=5)
    z_axis = models.FloatField(max_length=5)
    temp = models.FloatField (max_length=5)
    dateTime = models.DateTimeField()

    class Meta:
        db_table = "Batsu03" 

class Batsu_04 (models.Model):
    
    x_axis = models.FloatField(max_length=5)
    y_axis = models.FloatField(max_length=5)
    z_axis = models.FloatField(max_length=5)
    temp = models.FloatField (max_length=5)
    dateTime = models.DateTimeField()

    class Meta:
        db_table = "Batsu04" 

class Batsu_05 (models.Model):
    
    x_axis = models.FloatField(max_length=5)
    y_axis = models.FloatField(max_length=5)
    z_axis = models.FloatField(max_length=5)
    temp = models.FloatField (max_length=5)
    dateTime = models.DateTimeField()

    class Meta:
        db_table = "Batsu05" 