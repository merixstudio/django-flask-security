from rest_framework import serializers

from music.models import Album, Song, Artist


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title',)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'songs', 'artist',)

    songs = SongsSerializer(many=True)
    artist = ArtistSerializer()
