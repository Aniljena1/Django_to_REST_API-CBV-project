
from django import forms


class ContactForm(forms.Form):
    eid = forms.IntegerField()
    ename = forms.CharField()
    eemail = forms.EmailField()
    econtact = forms.IntegerField()

