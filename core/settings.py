# -*- coding: utf-8 -*-
import os
import djcelery
djcelery.setup_loader()

BROKER_URL = 'mongodb://isells:baster551737@ds045907.mongolab.com:45907/isells'

CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "ds045907.mongolab.com",
    "port": 45907,
    "user": "isells",
    "password": "baster551737",
    "database": "isells",
}

gettext = lambda s: s

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

LANGUAGES = [('en', 'English'), ('de', gettext('German')), ('ru', gettext('Russian'))]
DEFAULT_LANGUAGE = 0

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'mycms.db'),
        }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0r6%7gip5tmez*vygfv+u14h@4lbt^8e2^26o#5_f_#b7%cm)u'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',

    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

CMS_TEMPLATES = (
    ('base.html', 'Example Template'),
    ('coming-soon.html', 'Coming soon'),
    ('features.html', 'Features'),
    ('pricing.html', 'Pricing'),
    ('contact-us.html', 'Contact us'),
    )

CMS_HIDE_UNTRANSLATED = True

ROOT_URLCONF = 'core.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'cms',
    'menus',
    'mptt',
    'south',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'sekizai',
    'theme',
    'djcelery',
    'social_auth',
    'shop'
    )

REGISTRATION_OPEN = True

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_ENABLED_BACKENDS = ('google-oauth2', 'linkedin')

GOOGLE_OAUTH2_CLIENT_ID      = '947818718224.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = '70DLvY2X491gnztPMCJumMvU'

LINKEDIN_CONSUMER_KEY    = 'd7749002-5a9b-4974-bf80-2263f3e19f83'
LINKEDIN_CONSUMER_SECRET = 'dfb1163f-3eb4-431c-be2a-8d0ef6bae264'

LINKEDIN_CONSUMER_KEY        = '3hmojjjaavya' #API Key
LINKEDIN_CONSUMER_SECRET     = 'LtGKHdTJG8YDgpfU' #Secret Key


# Add email to requested authorizations.
LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress']
# Add the fields so they will be requested from linkedin.
LINKEDIN_EXTRA_FIELD_SELECTORS = ['email-address', 'headline', 'industry']
# Arrange to add the fields to UserSocialAuth.extra_data
LINKEDIN_EXTRA_DATA = [('id', 'id'),
                       ('first-name', 'first_name'),
                       ('last-name', 'last_name'),
                       ('email-address', 'email_address'),
                       ('headline', 'headline'),
                       ('industry', 'industry')]


LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/shop/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/shop/create/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/shop/create/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/new-error-url/'
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

SOCIAL_AUTH_SESSION_EXPIRATION = False


# include local_setting.py - for production
try:
    from local_settings import *
except ImportError:
    pass