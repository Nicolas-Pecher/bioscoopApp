from django.shortcuts import render, HttpResponseRedirect, get_list_or_404
from django.template import RequestContext
from django.contrib.auth import logout as auth_logout
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from .models import *

   
def home(request):
    movies = get_list_or_404(Movie)
    return render(request, 'home.html', {'movies':movies})

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/accounts/login')

class ScreeningsView(generic.ListView):
    context_object_name = "sessions"
    template_name = 'movies/screenings.html'

    def get_queryset(self):
        return Session.objects.all()

class MovieDescriptionView(generic.DetailView):
    model = Movie
    template_name = 'movies/description.html'

class ReservationView(generic.DetailView):
    model = Session
    template_name = 'movies/reservation.html'

class FavoritesView(generic.ListView):
    context_object_name = "favorites"
    template_name = 'movies/favorite.html'

    def get_queryset(self):
        return Favorites.objects.filter(user = self.request.user)

class confirmationView(generic.DetailView):
    model = Reservation
    template_name = 'movies/confirmation.html'

def comment(request,movie_id):
    print(request.POST['comment'])
    movie = Movie.objects.get(pk=movie_id)
    newComment = Comment(user = request.user,movie = movie,comment = request.POST['comment'])
    newComment.save()
    return  HttpResponseRedirect(reverse('movies:movieDescription', args = (movie.id,)))

def makeReservation(request,session_id):
    print(request.POST['seats'])
    session = Session.objects.get(pk=session_id)
    newReservation = Reservation(user = request.user,session = session,seats = request.POST['seats'],payment = request.POST['payment'])
    newReservation.save()
    return  HttpResponseRedirect(reverse('movies:confirmation', args = (newReservation.id,) ))

def addFavorite(request,movie_id):
    movie = Movie.objects.get(pk=movie_id)
    newFavorite = Favorites(user = request.user,movie = movie)
    newFavorite.save()
    messages.add_message(request,messages.INFO,"Succesfully saved to favorites!")
    return  HttpResponseRedirect(reverse('movies:movieDescription', args = (movie.id,)))