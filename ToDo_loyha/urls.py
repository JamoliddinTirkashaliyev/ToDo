from django.contrib import admin
from django.urls import path
from malumot.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentlar/', hamma_mualliflar),
    path('bitiruvchi/', bitiruvchi),
    path('yoshi_kattalar/', yoshi_kattalar),
    #path('bitta_muallif/<int:pk>/', bitta_muallif),
    path('muallif_ochir/<int:pk>/', ochir_muallif),


    path('rejalar/', hamma_rejalar),
    path('bajarilmagan/', bajarilmagan),
    path('bitiruvchilar_rejalari/', bitiruvchilar_rejalari),
    path('reja_ochir/<int:pk>/', ochir_reja),
]
