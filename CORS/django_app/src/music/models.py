from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=256)
    artist = models.ForeignKey(Artist, models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.artist}'


class Song(models.Model):
    title = models.CharField(max_length=256)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return f'{self.title} ({self.album})'
