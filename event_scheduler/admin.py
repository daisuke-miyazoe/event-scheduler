from django.contrib import admin
from .models import Event, Performer, Place

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    pass

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass
