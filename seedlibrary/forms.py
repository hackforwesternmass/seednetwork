from django import forms
from seednetwork.forms import SeedNetworkBaseForm
from seedlibrary.models import Event

class SeedForm(SeedNetworkBaseForm):
	seed_type = forms.CharField(max_length=150, required=False, help_text="i.e. vegetable, herb, perennial, fruit bush, fruit tree, etc.")
	crop_type = forms.CharField(max_length=150, required=False, help_text="i.e. carrot, bean, mint, day lillies, currant, apple, etc.")
	seed_variety = forms.CharField(max_length=150, required=False, help_text="i.e. Danvers, KY Wonder, Peppermint, etc.")
	seed_description = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="How has it performed? Days to maturity? What traits? etc.")
	enough_to_share = forms.BooleanField(required=False, help_text="Do you have enough to share?")
	year = forms.CharField(max_length=150, required=False)
	origin = forms.CharField(max_length=150, required=False, help_text="Where did you first obtain the seed?")
	events = forms.ModelMultipleChoiceField(Event.objects.filter(show_on_seed_edit=True), required=False, widget=forms.CheckboxSelectMultiple, help_text="What events will you bring the seed to?")

class SeedExportForm(SeedNetworkBaseForm):
	archive = forms.BooleanField(required=False, help_text="Do you want to export your archived seed listings?")
