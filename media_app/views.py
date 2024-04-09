from django.shortcuts import render
from .models import Song

def indexPage(request):
    songs = Song.objects.all()
    favSongs = Song.objects.filter(audio_link=1)
    return render(request,'media_app/index.html',{'songs':songs,'fav':favSongs})

def allsongs(request):
    songs = Song.objects.all()
    return render(request,'media_app/allsongs.html',{'songs':songs})