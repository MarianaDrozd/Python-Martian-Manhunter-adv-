from django import forms

from apps.newsletters.models import NewsLetter


class NewsLetterModelForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']
        labels = {'Email': ''}
