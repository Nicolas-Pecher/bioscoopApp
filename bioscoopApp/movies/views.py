from django.shortcuts import render, render_to_response,get_list_or_404
from django.template import RequestContext
from django.contrib.auth import logout as auth_logout
from django.views import generic
from .models import Movie

   
def home(request):
    movies = get_list_or_404(Movie)
    return render(request, 'home.html', {'movies':movies})

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('home.html', {}, RequestContext(request))

class ScreeningsView(generic.ListView):
    model = Movie
    template_name = 'movies/screenings.html'

    def get_queryset(self):
        return Movie.objects.all()

class MovieDescriptionView(generic.DetailView):
    model = Movie
    template_name = 'movies/description.html'

class MovieDescriptionView(generic.DetailView):
    model = Movie
    template_name = 'movies/description.html'

class ReservationView(generic.DetailView):
    model = Movie
    template_name = 'movies/reservation.html'

   
def ConfirmationView(request):
    return render(request, 'movies/confirmation.html')
