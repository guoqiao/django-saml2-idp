from django.conf.urls import url, include
from views import descriptor, login_begin, login_init, login_process, logout
from metadata import get_deeplink_resources

def deeplink_url_patterns(
        prefix='',
        url_base_pattern=r'^init/{}/$',
        login_init_func=login_init,
    ):
    """
    Returns new deeplink URLs based on 'links' from settings.SAML2IDP_REMOTES.
    Parameters:
    - url_base_pattern - Specify this if you need non-standard deeplink URLs.
        NOTE: This will probably closely match the 'login_init' URL.
    """
    resources = get_deeplink_resources()
    return [
        url(
             url_base_pattern.format(resource),
             login_init_func,
             kwargs ={'resource': resource},
        ) for resource in resources
    ]

urlpatterns = [
    url(r'^login/$', login_begin, name="login_begin"),
    url(r'^login/process/$', login_process, name='login_process'),
    url(r'^logout/$', logout, name="logout"),
    url(r'^metadata/xml/$', descriptor),
    url(r'^init/(?P<resource>\w+)/(?P<target>\w+)/$', login_init, name="login_init"),
]
# Issue 13 - Add new automagically-created URLs for deeplinks:
urlpatterns += deeplink_url_patterns()
