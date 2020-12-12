from django.db import models
from django.contrib.auth.models import User as AsilUser
turler = [('tyt', 'Temel Yeterlilik Testi'), ('ayt', 'Alan Yeterlilik Testi'), ('both', 'AYT ve TYT')]
derslerim = [('MAT','Matematik'),
             ('GEO','Geometri')]

class User(AsilUser):
    Solved_problems_count = models.FloatField(default=0,null=True)

class KONU(models.Model):
    ders_kodu = models.CharField(max_length=20)
    isim = models.CharField(max_length=50)
    ders_alan = models.CharField(choices=turler, max_length=20, default=('both','AYT ve TYT'))
    KONUNUN_DERSI = models.CharField(choices=derslerim, default=('MAT','Matematik'), max_length=30)
    ders_text = models.TextField(default="Ders hk. bilgi")
    soru_Sayisi = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Konular"
    def __str__(self):
        return self.isim
