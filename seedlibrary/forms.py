from django import forms

class SeedForm(forms.Form):
	seed_type = forms.CharField(max_length=150, required=False, help_text="i.e. vegetable, herb, perennial, fruit bush, fruit tree, etc.")
	crop_type = forms.CharField(max_length=150, required=False, help_text="i.e. carrot, bean, mint, ,day lillies, currant, apple, etc.")
	seed_variety = forms.CharField(max_length=150, required=False, help_text="i.e. Danvers, KY Wonder, Peppermint, etc.")
	seed_description = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="How has it performend? Days to maturity? What traits? etc.")
	enough_to_share = forms.BooleanField(required=False, help_text="Do you have enough to share?")
	year = forms.CharField(max_length=150, required=False)
	origin = forms.CharField(max_length=150, required=False, help_text="Where did you first obtain the seed?")

