from django.db import models

# Create your models here.
class Event(models.Model):
    Name=models.CharField(max_length=50)
    Date=models.CharField(max_length=15)
    Venue=models.CharField(max_length=10000)


    def __str__(self):
        return self.Name
