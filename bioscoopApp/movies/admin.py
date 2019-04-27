from django.contrib import admin

from .models import *

# Register your models here.

class ProducerInline(admin.TabularInline):
    model = Producer.movie.through
    extra = 1

class DirectorInline(admin.TabularInline):
    model = Director.movie.through
    extra = 1

class ActorInline(admin.TabularInline):
    model = Actor.movie.through
    extra = 3

class MovieAdmin(admin.ModelAdmin):
    inlines = [
        ProducerInline,DirectorInline,ActorInline
    ]
    exclude = ('movie',)
'''
class DirectorInline(admin.TabularInline):
    model = Director
    extra = 1

class ProducerInline(admin.TabularInline):
    model = Producer
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    inlines = [DirectorInline,ProducerInline]
'''

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'session', 'seats')

admin.site.register(Movie,MovieAdmin)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Producer)
admin.site.register(Session)
admin.site.register(ScreeningRoom)
admin.site.register(Comment)
admin.site.register(Favorites)
admin.site.register(Reservation,ReservationAdmin)
