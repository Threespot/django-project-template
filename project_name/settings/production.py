from .base import *


"""
This is the settings file used by your live production server(s).
(That is, the server(s) that host the real live website.)
This file contains production-level settings only. Debug mode will *always*
be turned off here.
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


# Turn Django compressor on.
COMPRESS_ENABLED = True
