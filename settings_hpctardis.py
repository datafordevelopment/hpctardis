from os import path
import djcelery

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (('bob', 'bob@bobmail.com'), )

MANAGERS = ADMINS

# Dictionary containing the settings for all databases to be used.
# The DATABASES setting must configure a default database;
# any number of additional databases may also be specified.
DATABASES = {
    'default': {
        # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Name of the database to use. For SQLite, it's the full path.
        'NAME': 'db.sqlite3',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Celery queue uses Django for persistence
BROKER_TRANSPORT = 'django'

# A dictionary containing the settings for all caches to be used with
# Django. The CACHES setting must configure a default cache; any
# number of additional caches may also be specified.  Once the cache
# is set up, you'll need to add
# 'django.middleware.cache.UpdateCacheMiddleware' and
# 'django.middleware.cache.FetchFromCacheMiddleware'
# to your MIDDLEWARE_CLASSES setting below

#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:11211',
#    }
#}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.

TIME_ZONE = 'Australia/Melbourne'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.

USE_I18N = True

# Make this unique, and don't share it with anybody.

SECRET_KEY = 'ij!%7-el^^rptw$b=iol%78okl10ee7zql-()z1r6e)gbxd3gl'

# once the cache is set up, you'll need to add
# 'django.middleware.cache.UpdateCacheMiddleware' and
# 'django.middleware.cache.FetchFromCacheMiddleware'
MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'tardis.tardis_portal.logging_middleware.LoggingMiddleware',
    'tardis.tardis_portal.auth.AuthorizationMiddleware',
    'django.middleware.transaction.TransactionMiddleware')

ROOT_URLCONF = 'tardis.hpctardis.urls'

TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.request',
                               'django.core.context_processors.static',
                               'django.contrib.auth.context_processors.auth',
                               'django.core.context_processors.debug',
                               'django.core.context_processors.i18n',
                                'tardis.tardis_portal.context_processors.single_search_processor',
                                'tardis.tardis_portal.context_processors.tokenuser_processor',
                                )

TEMPLATE_LOADERS = (
    'tardis.hpctardis.templates.loaders.app_specific.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
)


TEMPLATE_DIRS = (
    
    path.join(path.dirname(__file__),
    'hpctardis/publish/').replace('\\', '/'),

    path.join(path.dirname(__file__),
    'hpctardis/templates/').replace('\\', '/'),

                 
    path.join(path.dirname(__file__),
    'tardis_portal/publish/').replace('\\', '/'),                 
    
    path.join(path.dirname(__file__),
    'tardis_portal/templates/').replace('\\', '/'),

    '.',

                     
)


# Temporarily disable transaction management until everyone agrees that
# we should start handling transactions
DISABLE_TRANSACTION_MANAGEMENT = False

STATIC_DOC_ROOT = path.join(path.dirname(__file__),
                               'tardis_portal/site_media').replace('\\', '/')

def get_admin_media_path():
    import pkgutil
    package = pkgutil.get_loader("django.contrib.admin")
    return path.join(package.filename, 'media')

ADMIN_MEDIA_STATIC_DOC_ROOT = get_admin_media_path()

FILE_STORE_PATH = path.abspath(path.join(path.dirname(__file__),
    '../var/store/')).replace('\\', '/')
STAGING_PATH = path.abspath(path.join(path.dirname(__file__),
    '../var/staging/')).replace('\\', '/')
STAGING_PROTOCOL = 'localdb'
STAGING_MOUNT_PREFIX = 'smb://localhost/staging/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = STATIC_DOC_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media'

# Static content location
STATIC_URL = '/static'

# Used by "django collectstatic"
STATIC_ROOT = path.abspath(path.join(path.dirname(__file__),'..','static'))

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + '/admin/'

STATICFILES_DIRS = (
    ('admin', ADMIN_MEDIA_STATIC_DOC_ROOT),
)

# A tuple of strings designating all applications that are enabled in
# this Django installation.
TARDIS_APP_ROOT = 'tardis.apps'
INSTALLED_APPS = (
    TARDIS_APP_ROOT+'.equipment',
    'tardis.hpctardis',
    'django_extensions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'tardis.template.loaders',
    'tardis.tardis_portal',
    'tardis.tardis_portal.templatetags',
    'registration',
    'south',
    'django_jasmine',
    'djcelery',
    'djkombu',
    )

JASMINE_TEST_DIRECTORY = path.abspath(path.join(path.dirname(__file__),
                                                'tardis_portal',
                                                'tests',
                                                'jasmine'))

USER_PROVIDERS = ('tardis.tardis_portal.auth.localdb_auth.DjangoUserProvider',
)

GROUP_PROVIDERS = ('tardis.tardis_portal.auth.localdb_auth.DjangoGroupProvider',
                    'tardis.tardis_portal.auth.token_auth.TokenGroupProvider',
                   'tardis.tardis_portal.auth.ip_auth.IPGroupProvider'

)

# AUTH_PROVIDERS entry format:
# ('name', 'display name', 'backend implementation')
#   name - used as the key for the entry
#   display name - used as the displayed value in the login form
#   backend implementation points to the actual backend implementation
# We will assume that localdb will always be a default AUTH_PROVIDERS entry

AUTH_PROVIDERS = (
    ('localdb', 'Local DB', 'tardis.tardis_portal.auth.localdb_auth.DjangoAuthBackend'),
)

# default authentication module for experiment ownership user during
# ingestion? Must be one of the above authentication provider names
DEFAULT_AUTH = 'localdb'

AUTH_PROFILE_MODULE = 'tardis_portal.UserProfile'

ACCOUNT_ACTIVATION_DAYS = 3

# Email Configuration

EMAIL_LINK_HOST = "http://127.0.0.1:8000"

EMAIL_PORT = 587

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'bob@bobmail.com'

EMAIL_HOST_PASSWORD = 'bob'

EMAIL_USE_TLS = True

# Post Save Filters
#POST_SAVE_FILTERS = [
#    ("tardis.tardis_portal.filters.exif.make_filter",
#     ["EXIF", "http://exif.schema"]),  # this filter requires pyexiv2
#                                       # http://tilloy.net/dev/pyexiv2/
#    ]

# Post Save Filters
#POST_SAVE_FILTERS = [
#    ("tardis.tardis_portal.filters.diffractionimage.make_filter",
#     ["DIFFRACTION", "http://www.tardis.edu.au/schemas/trdDatafile/1",
#      "/Users/steve/Desktop/diffdump"]),  #  requires ccp4 diffdump binary
#    ]

# logging levels are: DEBUG, INFO, WARN, ERROR, CRITICAL
SYSTEM_LOG_LEVEL = 'DEBUG'
MODULE_LOG_LEVEL = 'DEBUG'

SYSTEM_LOG_FILENAME = 'request.log'
MODULE_LOG_FILENAME = 'tardis.log'

# Rollover occurs whenever the current log file is nearly maxBytes in length;
# if maxBytes is zero, rollover never occurs
SYSTEM_LOG_MAXBYTES = 0
MODULE_LOG_MAXBYTES = 0

# Uploadify root folder path, relative to STATIC root
UPLOADIFY_PATH = '%s/%s' % (STATIC_URL, 'js/lib/uploadify')

# Upload path that files are sent to
UPLOADIFY_UPLOAD_PATH = '%s/%s' % (MEDIA_URL, 'uploads')

# Settings for the single search box
# Set HAYSTACK_SOLR_URL to the location of the SOLR server instance
SINGLE_SEARCH_ENABLED = False
HAYSTACK_SITECONF = 'tardis.search_sites'
HAYSTACK_SEARCH_ENGINE = 'solr'
HAYSTACK_SOLR_URL = 'http://127.0.0.1:8080/solr'
if SINGLE_SEARCH_ENABLED:
    INSTALLED_APPS = INSTALLED_APPS + ('haystack',)
else:
    HAYSTACK_ENABLE_REGISTRATIONS = False

DEFAULT_INSTITUTION = "Monash University"

#Are the datasets ingested via METS xml (web services) to be immutable?
IMMUTABLE_METS_DATASETS = True

TOKEN_EXPIRY_DAYS = 30
TOKEN_LENGTH = 30
TOKEN_USERNAME = 'tokenuser'

# RIF-CS Settings
OAI_DOCS_PATH = path.abspath(path.join(path.dirname(__file__), '../var/oai'))
RIFCS_PROVIDERS = ('tardis.tardis_portal.publish.provider.rifcsprovider.RifCsProvider',)
RIFCS_TEMPLATE_DIR = path.join(path.dirname(__file__),
    'tardis_portal/templates/tardis_portal/rif-cs/profiles/')
RIFCS_GROUP = "MyTARDIS Default Group"
RELATED_INFO_SCHEMA_NAMESPACE = 'http://www.tardis.edu.au/schemas/related_info/2011/11/10'
RELATED_OTHER_INFO_SCHEMA_NAMESPACE = 'http://www.tardis.edu.au/schemas/experiment/annotation/2011/07/07'

DOI_ENABLE = False
DOI_XML_PROVIDER = 'tardis.tardis_portal.ands_doi.DOIXMLProvider'
#DOI_TEMPLATE_DIR = path.join(TARDIS_DIR, 'tardis_portal/templates/tardis_portal/doi/')
DOI_TEMPLATE_DIR = path.join('tardis_portal/doi/')
DOI_APP_ID = ''
DOI_NAMESPACE = 'http://www.tardis.edu.au/schemas/doi/2011/12/07'
DOI_MINT_URL = 'https://services.ands.org.au/home/dois/doi_mint.php'
DOI_RELATED_INFO_ENABLE = False
DOI_BASE_URL='http://mytardis.example.com'
COLLECTION_SUBJECTS = None


PUBLISH_PROVIDERS = (
                 #   'tardis.tardis_portal.publish.rif_cs_profile.'
                 #   + 'rif_cs_PublishProvider.rif_cs_PublishProvider',
                    'tardis.hpctardis.publish.rif_cs_profile.'
                    + 'rif_cs_PublishProvider.rif_cs_PublishProvider',
                    )
 
GROUP = "Acme University"
GROUP_ADDRESS = "Acme University, Coimbatore, India"
ACCESS_RIGHTS= "Contact the researchers/parties associated with this dataset"
RIGHTS= "Terms and conditions applies as specified by the researchers"

# Post Save Filters
POST_SAVE_FILTERS = []
tmp = list(POST_SAVE_FILTERS)
tmp.append(("tardis.hpctardis.filters.metadata.make_filter", ["",""]))
POST_SAVE_FILTERS = tuple(tmp)

# Add Middleware
tmp = list(MIDDLEWARE_CLASSES)
tmp.append(
    'tardis.tardis_portal.filters.FilterInitMiddleware'
)
MIDDLEWARE_CLASSES = tuple(tmp)
# HPCTardis Media
HPC_STATIC_URL_ROOT = '/static'
HPC_STATIC_DOC_ROOT = path.join(path.dirname(__file__),
                               'hpctardis/static').replace('\\', '/')


# Email Configuration

EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'bob@bobmail.com'
EMAIL_HOST_PASSWORD = 'bob'
EMAIL_USE_TLS = True
EMAIL_LINK_HOST = "http://127.0.0.1:8000"

PRIVATE_DATAFILES = False               


djcelery.setup_loader()
