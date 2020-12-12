from django import forms
from Questions.models import KONU

class SoruyaGitForm(forms.Form):
    konu = forms.ModelChoiceField(
        queryset=KONU.objects.all(),
        label="konu"
    )