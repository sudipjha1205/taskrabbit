from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=255,unique=True)
    bio = models.TextField()
    designation = models.CharField(max_length=255)
    joined_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile_pics',default='default.jpg')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)