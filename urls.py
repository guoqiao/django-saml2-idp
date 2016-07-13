from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^idp/', include('saml2idp.urls')),
    url(r'^accounts/login/$', login),
]
