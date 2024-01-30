from django.db import models

# Create your models here.
class FillDetailsModels(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    file_detail = models.TextField()
    fileInput = models.FileField(upload_to='media/')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

