from django.db import models

# Create your models here.
class FillDetailsModels(models.Model):
    sno = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    fileInput = models.FileField(upload_to='media/')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

class SignUpModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    pass1 = models.CharField(max_length=10)
    pass2 = models.CharField(max_length=10)