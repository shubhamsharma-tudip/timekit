from django.contrib.auth.models import User

from django.db import models


class user(models.Model):
     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)
     name = models.CharField(max_length=20)
     email = models.CharField(max_length=20)
     timezone = models.CharField(max_length=50)
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now_add=True)
     password = models.CharField(max_length=20)
     api_token=models.CharField(max_length=100, null=True)

class calender(models.Model):
     user=models.ForeignKey(user,related_name='user_id',null=True)
     name = models.CharField(max_length=20)
     description=models.CharField(max_length=250)
     cal_id=models.CharField(max_length=50)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now_add=True)

