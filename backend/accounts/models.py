from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.db.models.deletion import CASCADE



class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('This object requires an email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        is_active = True
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that uses email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']


class User_Profile (models.Model):

    Batangas_State_University = 'BATSU'
    Don_Honorio_Ventura_State_University = 'DHVSU'
    Bulacan_State_University = 'BULSU'
    University_Of_Rizal_System = 'URS'
    Tarlac_State_University = 'TSU'
    Mountain_Province_State_Polytechnic_College = 'MPSPU'
    Kalinga_State_University = 'KSU'
    University_of_Southern_Mindanao = 'USM'


    SCHOOL_CHOICES = [
        (Batangas_State_University, 'BATANGAS_STATE_UNIVERSITY'),
        (Don_Honorio_Ventura_State_University, 'DON_HONORIO_VENTURA_STATE_UNIVERSITY'),
        (Bulacan_State_University, 'BULACAN_STATE_UNIVERSITY'),
        (University_Of_Rizal_System, 'UNIVERSITY_OF_RIZAL_SYSTEM'),
        (Tarlac_State_University, 'TARLAC_STATE_UNIVERSITY'),
        (Mountain_Province_State_Polytechnic_College, 'MOUNTAIN_PROVINCE_STATE_POLYTECHNIC_COLLEGE'),
        (Kalinga_State_University, 'KALINGA_STATE_UNIVERSITY'),
        (University_of_Southern_Mindanao, 'UNIVERSITY_OF_SOUTHERN_MINDANAO'),
        
    ]

    user  = models.OneToOneField(User, on_delete=CASCADE)
    University = models.CharField(max_length=6, choices = SCHOOL_CHOICES, default = Batangas_State_University)
    First_Name = models.CharField(max_length=100, null= False)
    Last_Name = models.CharField(max_length=100, null= False)
    Date_Made = models.DateTimeField (auto_now_add=True)
    Date_Modified = models.DateTimeField (auto_now=True)

    
