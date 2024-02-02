from django.shortcuts import render,redirect
from .models import *

# Muallif uchun metodlar
def hamma_mualliflar(reqest):
    date = {
        "muallifs": Muallif.objects.all()

    }
    return render(reqest, 'Muallif.html', date)


def yoshi_kattalar(reqest):
    date = {
        "muallifs": Muallif.objects.filter(yosh__gt=20)

    }
    return render(reqest, 'Muallif.html', date)


def bitiruvchi(reqest):
    date = {
        "muallifs": Muallif.objects.filter(kurs__gt=2)

    }
    return render(reqest, 'Muallif.html', date)


def ochir_muallif(reqest, pk):
    Muallif.objects.get(id=pk).delete()
    return redirect("/studentlar/")



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Reja uchun metodlar:
def hamma_rejalar(reqest):
    if reqest.method=="POST":
        Reja.objects.create(
            sarlavha=reqest.POST.get("sarlavha"),
            sana=reqest.POST.get("sana"),
            malumot=reqest.POST.get("malumot"),
            bajarildi=reqest.POST.get("t")=="on",
            student=Muallif.objects.get(id=reqest.POST.get("m")),
        )
        return redirect("/rejalar/")
    date = {
        "rejalar": Reja.objects.all(),
        "mualliflar": Muallif.objects.all(),

    }
    return render(reqest, 'rejalar.html', date)


def bajarilmagan(reqest):
    date = {
        "rejalar": Reja.objects.filter(bajarildi=False)

    }
    return render(reqest, 'rejalar.html', date)


def bitiruvchilar_rejalari(reqest):

    date = {
        "rejalar": Reja.objects.filter(student__kurs=4)
    }
    return render(reqest, 'bitiruvchilar_rejalari.html', date)


def ochir_reja(reqest, pk):
    Reja.objects.get(id=pk).delete()
    return redirect("/rejalar/")

