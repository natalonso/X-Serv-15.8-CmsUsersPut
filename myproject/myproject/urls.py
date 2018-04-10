from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.auth.views import login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^logout$', logout),
    url(r'^login', login),
    url(r'^$','cms.views.home'), #me lleva a la pagina PRINCIPAL
    url(r'^(\w+)$','cms.views.pagina'),
    url(r'^admin/', include(admin.site.urls)),
)
