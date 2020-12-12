from django.db import models
from Posts.models import User, KONU
# Create your models here.
abcde = [('A','A'),('B','B'),('C','C'),('D','D'),('E','E')]

class Testler(models.Model):
    test_konu = models.ForeignKey(KONU,on_delete=models.CASCADE, default="")
    test_isim = models.CharField(max_length=50,default="DefaultTest")

    class Meta:
        verbose_name_plural = "Testler"

    def __str__(self):
        return self.test_isim


class Question(models.Model):
    question_test = models.ForeignKey(Testler, on_delete=models.CASCADE, default="")
    question_number = models.IntegerField(default=1)
    question = models.TextField(max_length=300,default="")
    option1 = models.CharField(max_length=100,default="")
    option2 = models.CharField(max_length=100,default="")
    option3 = models.CharField(max_length=100, default="")
    option4 = models.CharField(max_length=100, default="")
    option5 = models.CharField(max_length=100, default="")
    answer = models.CharField(max_length=10,default="a", choices=abcde)

    class Meta:
        verbose_name_plural = "Sorular"

    def __unicode__(self):
        return self.question

    def __str__(self):
        return self.question


class Statistics(models.Model):
    ogrenci = models.ForeignKey(User,on_delete=models.CASCADE, default="")
    test = models.ForeignKey(Testler, on_delete=models.CASCADE, default="")
    soru_adet = models.FloatField(default=0)
    dogru_adet = models.FloatField(default=0)
    yanlis_adet = models.FloatField(default=0)