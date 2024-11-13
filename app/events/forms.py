from django import forms


class AddToWatchlistForm(forms.Form):
    name = forms.IntegerField(widget=forms.HiddenInput)
