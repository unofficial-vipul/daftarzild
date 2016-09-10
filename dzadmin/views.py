from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
import soundcloud
# Create your views here.
def contact(request):
	form = ContactForm(request.POST or None)	
	if form.is_valid():
		sub = form.cleaned_data['subject']
		msg = form.cleaned_data['msg']
		fromemail = form.cleaned_data['email']
		toemail = 'vipul.sharma029@gmail.com'
		send_mail( sub, msg, fromemail, [toemail], fail_silently=True )

	ctx = {
		"form":form,
		}
	return render(request, 'contact.html', ctx)

def band_members(request):
	return render(request, 'band members.html')

def newshome(request):
	return render(request, 'newshome.html')

def music(request):
	client = soundcloud.Client(
				client_id='c3ba3b862a2ff085f07e051a79767aa3',
				client_secret='343c2dbc0bf1a99776b06521ecbea65d',
				username='vipul-sharma-844733033',
				password='readit1234'
				)
	playlist_url = 'https://soundcloud.com/vipul-sharma-844733033/sets/trippin'
	embed_info = client.get('/oembed', url=playlist_url)
	return render(request, 'music.html')


