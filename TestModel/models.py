from django.db import models

# Create your models here.
class C21Students(models.Model):
    ch_name = models.CharField(max_length=10)
    salary = models.FloatField(default=None)
    graduation_school = models.CharField(max_length=50,default='湖南理工学院')
    age = models.IntegerField(default=24)
    sex = models.CharField(max_length=4,default='女')
    company = models.CharField(max_length=40,default='阿里巴巴')

class GroupInformation(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(default=30)
    email = models.EmailField(default=None)

class PrivateInformation(models.Model):
    sex = models.CharField(max_length=2,default='女')

class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=4)
    event_limit = models.IntegerField()
    event_status = models.IntegerField()
    event_address = models.CharField(max_length=4)
    event_start_time = models.DateTimeField()
