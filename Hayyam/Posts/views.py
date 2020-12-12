from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, RedirectView, FormView
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from Posts.forms import GirisForm, RegisterForm
from Posts.models import User, KONU
# Create your views here.


class Logout(RedirectView):
    permanent = False
    pattern_name = "karsilama"

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(Logout, self).get_redirect_url(*args,**kwargs)


class Loggin(FormView):
    template_name = 'entrance/OFF_USER_WELCOME.html'
    form_class = GirisForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/hayyam-anasayfa/")
        return super(Loggin, self).dispatch(request,*args,**kwargs)

    def form_valid(self, form):
        user = authenticate(
           username=form.cleaned_data['username'],
           password=form.cleaned_data['password']
        )
        if user:
            login(self.request,user)
            return super(Loggin, self).form_valid(form)
        else:
            form = GirisForm()
            errormsg = "Yanlış kullanıcı adı veya şifre girdiniz, lütfen tekrar deneyiniz veya bir hesap oluşturunuz."
            return render(self.request, "entrance/OFF_USER_WELCOME.html", {
                'error': errormsg,
                'form': form
            })


class Register(FormView):
    template_name = 'entrance/REGISTER.html'
    form_class = RegisterForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        context['form'] = RegisterForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super(Register, self).dispatch(request,*args,**kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        if not User.objects.filter(username=username):
            user = User.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                username = form.cleaned_data['username']
            )
            user.set_password('{}'.format(form.cleaned_data['password']))
            user.save()
            login(self.request,user)
            return super(Register, self).form_valid(form)
        else:
            errormsg = "Bu kullanıcı adı daha önceden alınmıştır."
            return render(self.request, "entrance/REGISTER.html", {
                'error': errormsg,
                'form': form
            })


class Welcome(TemplateView):
    template_name = "corridor/IN_USER_WELCOME.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            errormsg = "Bu sayfaya erişebilmek için öncelikle lütfen giriş yapınız."
            return render(self.request, "entrance/LOGIN_REQUIRED_PAGE.html", {
                'error': errormsg,
            })
        else:
            return super(Welcome, self).dispatch(request,*args,**kwargs)


class Profilim(TemplateView):
    template_name = "lounge/PROFIL_IN_USER.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            errormsg = "Bu sayfaya erişebilmek için öncelikle lütfen giriş yapınız."
            return render(self.request, "entrance/LOGIN_REQUIRED_PAGE.html", {
                'error': errormsg,
            })
        else:
            return super(Profilim, self).dispatch(request,*args,**kwargs)


class Konular(TemplateView):
    template_name = "lounge/KONULAR_IN_USER.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            errormsg = "Bu sayfaya erişebilmek için öncelikle lütfen giriş yapınız."
            return render(self.request, "entrance/LOGIN_REQUIRED_PAGE.html", {
                'error': errormsg,
            })
        else:
            return super(Konular, self).dispatch(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(Konular, self).get_context_data(**kwargs)
        context['MAT_KONULARI'] = KONU.objects.filter(KONUNUN_DERSI='MAT').order_by("-soru_Sayisi")
        context['GEO_KONULARI'] = KONU.objects.filter(KONUNUN_DERSI='GEO').order_by("-soru_Sayisi")
        return context


def Konu_Profil(request, id):
    konu = KONU.objects.filter(id=id)
    return render(request, "lounge/KONU_IN_OFF_USER.html", {
        'konu':konu[0],
        'konu_id':konu[0].id,
    })


class User_List(TemplateView):
    template_name = "lounge/USER_LIST_IN_USER.html"

    def get_context_data(self, **kwargs):
        context = super(User_List, self).get_context_data(**kwargs)
        context['USERS'] = User.objects.all()
        return context
