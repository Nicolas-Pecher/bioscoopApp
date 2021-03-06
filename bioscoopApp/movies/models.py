from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#movie related tables
class Movie(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField()
    description = models.TextField()
    releaseDate = models.DateTimeField()
    picture = models.CharField(max_length=200)
    trailer = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Producer(models.Model):
    name = models.CharField(max_length=50)
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=50)
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=50)
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

#session related tables

class ScreeningRoom(models.Model):
    roomNumber = models.IntegerField()
    rows = models.IntegerField()
    seat = models.IntegerField()

    def __str__(self):
        return str(self.roomNumber)

class Session(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    screeningRoom = models.ForeignKey(ScreeningRoom, on_delete=models.CASCADE)
    begin = models.DateTimeField()
    version = models.CharField(max_length=50)
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.version

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    seats = models.IntegerField()
    payment = models.CharField(max_length=50)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    comment = models.TextField()

class Favorites(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title