from django import forms



class ContactForm(forms.Form):
	fullname = forms.CharField()
	phone_no = forms.CharField()
	email_add = forms.EmailField()
	msg = forms.CharField(widget=forms.Textarea)