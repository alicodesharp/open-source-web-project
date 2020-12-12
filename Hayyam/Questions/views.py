from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, RedirectView, FormView
from Questions.forms import SoruyaGitForm
from Questions.models import Question, Testler, Statistics
from Posts.models import KONU, User


class soruCoz(FormView):
    template_name = "lounge/SORU_COZ_IN_USER.html"
    form_class = SoruyaGitForm
    success_url = "/akis_yonlendir/"

    def get_context_data(self, **kwargs):
        context=super(soruCoz, self).get_context_data(**kwargs)
        context['konular'] = KONU.objects.all()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            errormsg = "Bu sayfaya erişebilmek için öncelikle lütfen giriş yapınız."
            return render(self.request, "entrance/LOGIN_REQUIRED_PAGE.html", {
                'error': errormsg,
            })
        else:
            return super(soruCoz, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        konu = form.cleaned_data['konu']
        testler = Testler.objects.filter(test_konu=konu)
        soru_adeti = Question.objects.filter(question_test=testler[0]).count()
        return render(self.request, 'corridor/AKIS_GORUNTULE.html', {
            'konu': konu,
            'testler': testler,
            'soru_adeti': soru_adeti
        })


from datetime import datetime, timedelta


def TesteGit(request, id):
    test = Testler.objects.filter(id=id)
    now = datetime.now()
    new_time = timedelta(minutes=15)+now
    dt_string = new_time.strftime("%B %d, %Y %H:%M:%S")
    sorular = Question.objects.filter(question_test=test[0]).order_by("question_number")
    soru_adeti = sorular.count()
    return render(request, 'lounge/TEST_FIELD_IN_USER.html', {
        'sorular': sorular,
        'test': test[0],
        'sure': dt_string,
        'soru_adeti': soru_adeti,
    })


def testiTamamla(request):
    if request.method == 'POST':
        ogrenci_id = request.POST.get('ogrenci_id')
        print(ogrenci_id)
        ogrenci=User.objects.filter(id=ogrenci_id)
        print(ogrenci)
        test_id = request.POST.get('test_id')
        print(test_id)
        test = Testler.objects.filter(id=test_id)
        print(test)
#       -----------------------------------------
        soru_adet = request.POST.get('soru_adet', False)
        dogru_adet = request.POST.get('dogru_adet', False)
        yanlis_adet = request.POST.get('yanlis_adet', False)
        Statistics.objects.create(
            ogrenci = request.user.user,
            test = test,
            soru_adet=soru_adet,
            dogru_adet=dogru_adet,
            yanlis_adet=yanlis_adet
        )
        Statistics.save()
        return HttpResponse('')
# bu şekilde olmadığı için bu def yerine test_field_in_user.html dosyasını açan view ı form view olarak çalıştırıp, formu en sonda görünür hale getirip formview ile sonuca ulaşmayı dene. Bugünlük bukadar yeter

