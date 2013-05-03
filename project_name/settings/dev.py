from .base import *


"""
This is the settings file that you use when you’re working on the project locally.
Local development-specific settings include DEBUG mode, log level, and activation
of developer tools like django-debug-toolbar.
"""


DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ('127.0.0.1',)


DATABASES['default']['USER'] = get_env_variable("DB_USER")
DATABASES['default']['PASSWORD'] = get_env_variable("DB_PASSWORD")


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '/tmp/{{ project_name }}_cache/'
    }
}

INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
    'django_extensions',
    'django_coverage',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# This function is used to determine when the debug toolbar should be
# displayed: when the user is logged in and not in the admin.
def _ddt_check(request):
    if request.path.startswith("/admin/"):
        return False
    if request.user.is_authenticated():
        return True
    return False

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': _ddt_check
}

# Log sent emails to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Turn Django compressor off.
COMPRESS_ENABLED = False