from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^idp/', include('saml2idp.urls')),
    url(r'', include(admin.site.urls)),
]
