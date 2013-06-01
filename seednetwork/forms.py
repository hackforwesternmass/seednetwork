from django import forms

class MemberInfoForm(forms.Form):
	first_name = forms.CharField(max_length=150, required=False)
	last_name = forms.CharField(max_length=150, required=False)
	email = forms.CharField(max_length=150, required=False)
	email_is_public = forms.BooleanField(required=False)
	town = forms.CharField(max_length=150, required=False)
	phone = forms.CharField(max_length=150, required=False)
	phone_is_public = forms.BooleanField(required=False)

	street_address = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False)
	street_address_is_public = forms.BooleanField(required=False)

	mailing_address = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False)
	mailing_address_is_public = forms.BooleanField(required=False)

	about_me = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False)
	include_in_member_profiles = forms.BooleanField(required=False)