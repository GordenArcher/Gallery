from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Images(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Stock_Images")
    date_created = models.DateTimeField(auto_now_add=True)
    
    