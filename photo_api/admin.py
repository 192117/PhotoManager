from django.contrib import admin

from .models import Photo, User

admin.site.register(User)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    search_fields = ('description', 'date',)
    list_display = ('latitude', 'longitude', 'date', 'people', )
    list_filter = ('latitude', 'longitude', 'date', 'people', )
