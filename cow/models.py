from django.db import models

# Create your models here.
class OurTeam(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to='pictures')