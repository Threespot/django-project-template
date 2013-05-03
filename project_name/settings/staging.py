from .base import *


"""
Staging version for running a semi-private version of the site on a production server.
This is where managers and clients should be looking before your work is moved to production.
"""

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES['default']['USER'] = get_env_variable("DB_USER")
DATABASES['default']['PASSWORD'] = get_env_variable("DB_PASSWORD")


# If using Heroku, Parse database configuration from $DATABASE_URL:
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()

# If using Dotcloud:
#DATABASES['default']['USER'] = get_env_variable('DOTCLOUD_DB_SQL_LOGIN')
#DATABASES['default']['PASSWORD'] = get_env_variable('DOTCLOUD_DB_SQL_PASSWORD')
#DATABASES['default']['HOST'] = get_env_variable('DOTCLOUD_DB_SQL_HOST')
#DATABASES['default']['PORT'] = str(get_env_variable('DOTCLOUD_DB_SQL_PORT'])


INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
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

# Turn Django compressor off.
COMPRESS_ENABLED = False