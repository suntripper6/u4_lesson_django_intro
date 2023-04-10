from django.shortcuts import render, redirect
from .models import Artist, Song
from .forms import ArtistForm
from rest_framework import generics
from .serializers import ArtistSerializer, SongSerializer

# Create your views here.


# def artist_list(request):
#     artists = Artist.objects.all()
#     return render(request, 'tunr/artist_list.html', {'artists': artists})


# def artist_detail(request, pk):
#     artist = Artist.objects.get(id=pk)
#     return render(request, 'tunr/artist_detail.html', {'artist': artist})


# def song_list(request):
#     songs = Song.objects.all()
#     return render(request, 'tunr/song_list.html', {'songs': songs})


# def song_detail(request, pk):
#     song = Song.objects.get(id=pk)
#     return render(request, 'tunr/song_detail.html', {'song': song})

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'tunr/artist_form.html', {'form': form})
