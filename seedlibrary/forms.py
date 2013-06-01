from django import forms

class SeedForm(forms.Form):
	seed_type = forms.CharField(max_length=150, required=False)
	crop_type = forms.CharField(max_length=150, required=False)
	seed_variety = forms.CharField(max_length=150, required=False)
	seed_description = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False)
	enough_to_share = forms.BooleanField(required=False)
	year = forms.CharField(max_length=150, required=False)
	origin = forms.CharField(max_length=150, required=False)

