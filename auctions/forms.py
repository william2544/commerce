from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'

class BidForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ['status','category','description','name','watchlist']