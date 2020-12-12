from django import forms

class GirisForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı: ")
    password = forms.CharField(max_length=30, widget=forms.PasswordInput, label="Şifre:")

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)


