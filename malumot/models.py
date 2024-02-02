from django.db import models

# Create your models here.


class Muallif(models.Model):
    ism=models.CharField(max_length=30)
    yosh=models.PositiveIntegerField()
    kurs=models.PositiveIntegerField()
    student_raqam=models.PositiveIntegerField(unique=True)
    def __str__(self):
        return f"{self.ism}, {self.kurs}-kurs"

class Reja(models.Model):
    sarlavha=models.CharField(max_length=200)
    sana=models.DateField()
    malumot=models.TextField(null=True)
    bajarildi=models.BooleanField()
    student=models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.satrlavha},"