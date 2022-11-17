from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.FloatField()


