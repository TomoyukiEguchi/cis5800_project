from django.contrib import admin
from .models import Comment


# Register your models here.
#admin.site.register(Restaurant)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', )
    list_display_links = ('id',)
    ordering = ('-created',)