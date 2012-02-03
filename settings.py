# Django settings for thess project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
import os.path
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

ADMINS = (
    ('Dom', 'contact@quinode.fr'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CHARSET='utf-8'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.abspath(PROJECT_PATH+'/media/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.abspath(PROJECT_PATH+'/static_collected/')
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

import admin_tools
ADMIN_TOOLS_PATH = os.path.dirname(os.path.abspath(admin_tools.__file__))

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.abspath(PROJECT_PATH+'/static/'),
    os.path.abspath(ADMIN_TOOLS_PATH+'/media/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'coop.utils.cors.CORSMiddleware'
]


# Make this unique, and don't share it with anybody.
SECRET_KEY = '5d7f_()5wz&me=6l$r(vup6+jmmsgq69@@v*76#u+8^z0ka@5x'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'thess.urls'

TEMPLATE_DIRS = (
    os.path.abspath(PROJECT_PATH+'/templates/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    'django.core.context_processors.request',
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "thess.context_processors.site_settings",
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

INSTALLED_APPS = (
    # Admin tools
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    
    # contrib
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    
    'taggit',
    'taggit_templatetags',
    'django_extensions',
    'skosxl',
    'south',
)

TAGGIT_TAG_MODEL           = ('skosxl','Label')
TAGGIT_TAGGED_ITEM_MODEL   = ('skosxl','LabelledItem')
TAGGIT_TAG_FIELD_RELATED_NAME = 'skosxl_label_items'

TAGGIT_AUTOCOMPLETE_TAG_MODEL = 'skosxl.Label'


ADMIN_TOOLS_MENU = 'thess.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'thess.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'thess.dashboard.CustomAppIndexDashboard'
#ADMIN_TOOLS_THEMING_CSS = 'css/coop_theming.css'

SITE_AUTHOR = 'Collectif'
SITE_TITLE = 'Thesaurus ESS'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError, exp:
    pass
