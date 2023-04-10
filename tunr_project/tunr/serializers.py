from rest_framework import serializers
from .models import Artist, Song


class SongSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        read_only=True
    )

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all()
    )

    class Meta:
        model = Song
        fields = ('id', 'artist', 'artist_id', 'title', 'album', 'preview_url')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    songs = SongSerializer(
        many=True,  # One To Many
        read_only=True
    )

    artist_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artist_detail')

    class Meta:
        model = Artist
        fields = ('id', 'artist_url', 'name', 'photo_url',
                  'songs', 'nationality')
