from django.contrib import admin
from .models import *


class RejaAdmin(admin.ModelAdmin):
    list_display = ['sarlavha', 'sana', 'malumot', 'bajarildi', 'student']
    list_filter = ['bajarildi']
    search_fields = ['sarlavha']
    list_display_links = ['sarlavha']
    autocomplete_fields = ['student']

class MuallifAdmin(admin.ModelAdmin):
    list_display = ['ism','yosh','kurs','student_raqam']
    list_filter = ["kurs"]
    search_fields = ['ism']
    list_display_links = ['ism']


admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Reja, RejaAdmin)


