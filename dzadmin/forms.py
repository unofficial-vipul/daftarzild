from django.forms import ModelForm
from dzadmin.models import Message

class ContactForm(ModelForm):
	class Meta:
		model = Message
		fields = ['fullname', 'email','phoneno', 'subject', 'msg']

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
				})

