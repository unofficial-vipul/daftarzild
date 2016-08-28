from django.conf.urls import include, url
from django.contrib import admin



from .views import (
	contact,
	band_members,
    music,

	)

urlpatterns = [
    # Examples:
    # url(r'^$', 'daftarzild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^contact/$',contact, name="contact" ),
    url(r'^bandmembers/$',band_members, name="bandmembers" ),
    url(r'^music/$',music, name="music" ),
    



]