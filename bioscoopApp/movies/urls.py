from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.home, name="home"),
    path('logout', views.logout, name="logout"),
    path('screenings', views.ScreeningsView.as_view(), name="screenings"),
    path('<int:pk>/movieDescription', views.MovieDescriptionView.as_view(), name="movieDescription"),
    path('<int:pk>/reservation', views.ReservationView.as_view(), name="reservation"),
    path('confirmation',views.ConfirmationView, name="confirmation")
]
