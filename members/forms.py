from django import forms

class NameForm (forms.Form):
    intro = forms.Charfield(label='your name', max_length=20)
    intro = intro+1
    


