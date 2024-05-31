from django.contrib import admin
from .models import (Pages,
                     Blog_category,
                     Blog,
                     Upcoming_events,
                     Course_category,
                     Course,
                     Instructor,
                     Cards)
# Register your models here.

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')

admin.site.register(Blog_category)
admin.site.register(Blog)
admin.site.register(Upcoming_events)
admin.site.register(Course_category)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Cards)


