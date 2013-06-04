from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

def as_table_func(self):
	return self._html_output(
		normal_row = '<tr%(html_class_attr)s><th>%(label)s</th><td>%(field)s%(errors)s%(help_text)s</td></tr>',
		error_row = '<tr><td colspan="2">%s</td></tr>',
		row_ender = '</td></tr>',
		help_text_html = '<br /><span class="helptext">%s</span>',
		errors_on_separate_row = False)

class SeedNetworkBaseForm(forms.Form):
	def as_table(self):
		"Returns this form rendered as HTML <tr>s -- excluding the <table></table>."
		return as_table_func(self)


class MemberInfoForm(SeedNetworkBaseForm):
	first_name = forms.CharField(max_length=150, required=True)
	last_name = forms.CharField(max_length=150, required=True)
	email = forms.CharField(max_length=150, required=True)
	email_is_public = forms.BooleanField(required=False)
	town = forms.CharField(max_length=150, required=True)
	phone = forms.CharField(max_length=150, required=False)
	phone_is_public = forms.BooleanField(required=False)

	street_address = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False)
	street_address_is_public = forms.BooleanField(required=False)

	mailing_address = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="(if different from street address)")
	mailing_address_is_public = forms.BooleanField(required=False)

	about_me = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False)
	include_in_member_profiles = forms.BooleanField(required=False)

class SeedNetworkAuthForm(AuthenticationForm):
	def as_table(self):
		return as_table_func(self)

class SeedNetworkPasswordChangeForm(PasswordChangeForm):
	def as_table(self):
		return as_table_func(self)

