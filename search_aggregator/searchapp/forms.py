from django import forms

class NameForm(forms.Form):
    searchkey = forms.CharField(label='Search keyword', max_length=100)