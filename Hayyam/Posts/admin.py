from django.contrib import admin
from Posts.models import KONU
# Register your models here.


def tyt_alan(DERS, request, turler):
    turler.update(türü='both')


tyt_alan.short_description = "TYT alanı yap"


class KonuAdmin(admin.ModelAdmin):
    list_display = ['isim', 'ders_kodu','KONUNUN_DERSI', 'ders_alan','ders_text','soru_Sayisi']
    list_filter = ['ders_alan']
    actions = [tyt_alan]

admin.site.register(KONU, KonuAdmin)

