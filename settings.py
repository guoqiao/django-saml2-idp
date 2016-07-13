from path import path
from os.path import abspath, dirname

BASE_DIR = path(dirname(abspath(__file__)))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR/'db.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = ''

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'q+0vb%)c7c%&kl&jcca^6n7$3q4ktle9i28t(fd&qh28%l-%58'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR/'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'saml2idp',
)

LOGIN_REDIRECT_URL = '/idp/sso/post/response/preview/'

# SAML2IDP metadata settings
SAML2IDP_CONFIG = {
    'autosubmit': False,
    'issuer': 'http://127.0.0.1:8000',
    'signing': True,
    'certificate_file': BASE_DIR/'keys/sample/sample-certificate.pem',
    'private_key_file': BASE_DIR/'keys/sample/sample-private-key.pem',
}

demoSpConfig = {
    'acs_url': 'http://127.0.0.1:9000/sp/acs/',
    'processor': 'saml2idp.demo.Processor',
    'links': [ # a list of (resource, pattern) tuples, or a {resource: pattern} dict
        #NOTE: This should still work, due to the "simple" 'login_init' URL in urls.py:
        #TEST BY BROWSING TO: http://127.0.0.1:8000/sp/test/
        ('deeplink', 'http://127.0.0.1:9000/sp/%s/'),
        # The following are "new" deeplink mappings that let you specify more than one capture group:
        # This is equivalent to the above, using the 'new' deeplink mapping:
        #TEST BY BROWSING TO: http://127.0.0.1:8000/sp/test/
        (r'deeplink/(?P<target>\w+)', 'http://127.0.0.1:9000/sp/%(target)s/'),
        # Using two capture groups:
        #TEST BY BROWSING TO: http://127.0.0.1:8000/sp/test/
        (r'deeplink/(?P<target>\w+)/(?P<page>\w+)', 'http://127.0.0.1:9000/%(target)s/%(page)s/'),
        # Deeplink to a resource that requires query parameters:
        #NOTE: In the pattern, always use %(variable)s, because the captured
        # parameters will always be in unicode.
        #TEST BY BROWSING TO: http://127.0.0.1:8000/sp/test/123/
        (r'deeplink/(?P<target>\w+)/(?P<page>\w+)/(?P<param>\d+)',
            'http://127.0.0.1:9000/%(target)s/%(page)s/?param=%(param)s'),
    ],
}

attrSpConfig = {
    'acs_url': 'http://127.0.0.1:9000/sp/acs/',
    'processor': 'saml2idp.demo.AttributeProcessor',
    'links': {
        'attr': 'http://127.0.0.1:9000/sp/%s/',
    },
}

SAML2IDP_REMOTES = {
    # Group of SP CONFIGs.
    # friendlyname: SP config
    'attr_demo': attrSpConfig,
    'demo': demoSpConfig,
}

# Setup logging.
import logging
logging.basicConfig(
    filename=BASE_DIR/'saml2idp.log',
    format='%(asctime)s: %(message)s',
    level=logging.DEBUG
)
logging.info('Logging setup.')
