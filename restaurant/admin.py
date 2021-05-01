from django.contrib import admin

from .models import Restaurant
# Register your models here.
#admin.site.register(Restaurant)

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'area', 'cuisine', 'live_capacity', 'address1', 'address2', 'city', 'state', 'zipcode', 'created_at')
    list_display_links = ('name',)
    ordering = ('-created_at',)
