from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'), 
path('about/', views.about, name='about'),
path('songs/', views.songs_index, name='index'),
path('songs/<int:song_id>/', views.songs_detail, name='detail'),
path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
path('accounts/signup/', views.signup, name='signup'),
path('musician/<int:musician_id>/add_photo/', views.add_photo, name='add_photo'),
path('musician/', views.MusicianList.as_view(), name='musicians_index'),
path('musician/create/', views.MusicianCreate.as_view(), name='musicians_create'),
path('musician/<int:pk>/update/', views.MusicianUpdate.as_view(), name='musicians_update'),
path('musician/<int:pk>/delete/', views.MusicianDelete.as_view(), name='musicians_delete'),
path('musician/<int:pk>/', views.MusicianDetail.as_view(), name='musicians_detail'),
path('accounts/signup/', views.signup, name='signup'),
path('songs/<int:song_id>/assoc_musician/<int:musician_id>/', views.assoc_musician, name='assoc_musician'),
path('songs/<int:song_id>/rm_song_musician/<int:musician_id>/', views.rm_song_musician, name='rm_song_musician'),
path('photos/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo_delete'),



]