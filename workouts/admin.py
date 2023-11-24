from django.contrib import admin
from .models import Workout, Type, Intensity
from django_summernote.admin import SummernoteModelAdmin

# Register Type Model
admin.site.register(Type)

# Register Intensity Model
admin.site.register(Intensity)

@admin.register(Workout)
class WorkoutAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'slug')
    summernote_fields = ('your_rich_text_field',)
    list_display = ('title', 'type', 'intensity', 'created_on')
    search_fields = ['title', 'type', 'intensity']
