from django.contrib import admin
from .models import Musician, Song, Musician_Photo
# Register your models here.
admin.site.register(Song)
admin.site.register(Musician)
admin.site.register(Musician_Photo)