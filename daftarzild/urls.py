from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.conf.urls.static import static
from django.conf import settings

from .views import (
	home,
	)

urlpatterns = [
    # Examples:
    # url(r'^$', 'daftarzild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^dz/', include("dzadmin.urls", namespace='dzadmin')),
    url(r'^news/', include("posts.urls", namespace='posts')),
    url(r'^comments/', include("comments.urls", namespace='comments')),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)