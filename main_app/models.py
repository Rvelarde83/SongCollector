from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Musician(models.Model):
  name = models.CharField(max_length=50)
  instrument = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('musicians_detail', kwargs={'pk': self.id})


class Song(models.Model):
    name= models.CharField(max_length=150, default='')
    author= models.CharField(max_length=150, default='')
    lyrics= models.CharField(max_length=3000, default='')
    # date= models.DateField
    original_key= models.CharField(max_length=10, default='')
    arranger=models.CharField(max_length=150, default='')
    producer=models.CharField(max_length=150, default='')
    musicians=models.ManyToManyField(Musician)
    links=models.CharField(max_length=300, default='')
    notes=models.CharField(max_length=3000, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'song_id': self.id})

class Musician_Photo(models.Model):
    url = models.CharField(max_length=200)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for musician_id: {self.musician_id} @{self.url}"

# Arranger: 
# Producer:
# Musicians:
# Link:
# Notes: