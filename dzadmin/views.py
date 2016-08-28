from django.shortcuts import render
from .forms import ContactForm
import soundcloud
# Create your views here.
def contact(request):
	print "contact page"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print form.cleaned_data

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
	print client.get('/me')
	playlist_url = 'https://soundcloud.com/vipul-sharma-844733033/sets/trippin'
	embed_info = client.get('/oembed', url=playlist_url)
	print embed_info.html
	return render(request, 'music.html')


