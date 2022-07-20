from django.shortcuts import render, redirect
from .models import Song, User, Musician, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  SignUpForm
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect
# from .forms import  SignUpForm
import uuid
import boto3

# Add the following import
from django.http import HttpResponse

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = "rv-collector"



# Define the home view
def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

@login_required
def songs_index(request):
  songs = Song.objects.filter(user=request.user)
  return render(request, 'songs/index.html', { 'songs': songs })


@login_required
def songs_detail(request, song_id):
  song = Song.objects.get(id=song_id)
  musicians_song_doesnt_have = Musician.objects.exclude(id__in = song.musicians.all().values_list('id'))
  
  return render(request, 'songs/detail.html', {
        'song': song,
        'musicians': musicians_song_doesnt_have})

# @login_required
def add_photo(request, musician_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to musician_id or musician (if you have a musician object)
            photo = Photo(url=url, musician_id=musician_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('musicians_detail', pk=musician_id)




class SongCreate(LoginRequiredMixin,CreateView):
  model = Song
  fields = ['name', 'author', 'lyrics', 'original_key', 'arranger', 'producer', 'links', 'notes']
  # success_url = '/songs/'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the song
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class SongUpdate(LoginRequiredMixin,UpdateView):
  model = Song
  fields = ['name', 'author', 'lyrics', 'original_key', 'arranger', 'producer', 'links', 'notes']

class SongDelete(LoginRequiredMixin,DeleteView):
  model = Song
  success_url = '/songs/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = SignUpForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = SignUpForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)  





class MusicianList(LoginRequiredMixin,ListView):
    model = Musician


class MusicianDetail(LoginRequiredMixin,DetailView):
    model = Musician


class MusicianCreate(LoginRequiredMixin,CreateView):
    model = Musician
    fields = '__all__'
    # success_url: 


class MusicianUpdate(LoginRequiredMixin,UpdateView):
    model = Musician
    fields = '__all__'


class MusicianDelete(LoginRequiredMixin,DeleteView):
    model = Musician
    success_url = '/musician/'

class PhotoDelete(LoginRequiredMixin,DeleteView):
    model = Photo
    def get_success_url(self):
       
        return reverse('musicians_detail', kwargs={'pk': self.object.musician_id})

   



@login_required
def assoc_musician(request, song_id, musician_id):
    # Note that you can pass a toy's id instead of the whole object
    Song.objects.get(id=song_id).musicians.add(musician_id)
    return redirect('detail', song_id=song_id)

@login_required
def rm_song_musician(request, song_id, musician_id):
    Song.objects.get(id=song_id).musicians.remove(musician_id)
    return redirect('detail', song_id=song_id)

    