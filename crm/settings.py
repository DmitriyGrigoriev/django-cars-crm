import os
from dotenv import load_dotenv
from pathlib import Path
from celery.schedules import crontab
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', default=False)

#ALLOWED_HOSTS = [".bottlecrm.com", ".localhost"]
ALLOWED_HOSTS = ["*"]

# Application definition
LOGIN_REDIRECT_URL = "/"

# LOGIN_URL = "/login/"
LOGIN_URL = "/auth/domain/"

DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",

    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPS = [
    "sass_processor",
    "simple_pagination",
    "telegram_django_bot",
    "django_htmx",
    "django_components",
    "crispy_forms",
    "crispy_bootstrap4",
    # "template_partials",
    "compressor",
    # 'haystack',
    "sorl.thumbnail",
    "phonenumber_field",
    "storages",
]
LOCAL_APPS = [
    "common",
    "accounts",
    "cases",
    "contacts",
    "emails",
    "leads",
    "opportunity",
    "planner",
    "marketing",
    "tasks",
    "invoices",
    "events",
    "teams",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "common.middleware.registry_errors.ExceptionMiddleware",
    "common.middleware.get_company.GetCompany",
]

ROOT_URLCONF = "crm.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates"),],
        # "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # "django.core.context_processors.request", # use in simple_pagination
                "common.context_processors.common.app_name",
                "django_settings_export.settings_export",
            ],
            'loaders':[(
                'django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    'django_components.template_loader.Loader',
                ]
            )],
            "builtins": ["django_components.templatetags.component_tags"],
            # "builtins": ["template_partials.templatetags.partials"],
            "debug": DEBUG,
        },
    },
]

WSGI_APPLICATION = "crm.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DBNAME"),
        "USER": os.getenv("DBUSER"),
        "PASSWORD": os.getenv("DBPASSWORD"),
        "HOST": os.getenv("DBHOST"),
        "PORT": os.getenv("DBPORT"),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "blog_app/static"),
    os.path.join(BASE_DIR, "components"),
]

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('ru', _('Russian')),
    ('en', _('English'))
]

# AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', )
AUTH_USER_MODEL = "common.User"

ENV_TYPE = os.getenv("ENV_TYPE", "dev")

if ENV_TYPE == "dev":
    DOMAIN_NAME = "localhost:8000"
    # SESSION_COOKIE_DOMAIN = "localhost:8000"

    # DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    # STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    # COMPRESS_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    MEDIA_URL = "/media/"

    STATIC_URL = "/static/"
    STATICFILES_DIRS = (BASE_DIR + "/static",)
    # COMPRESS_ROOT = BASE_DIR + "/static/"
    COMPRESS_ROOT = STATIC_ROOT

    ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"


elif ENV_TYPE == "live":
    from .server_settings import *

    SESSION_COOKIE_DOMAIN = ".bottlecrm.com"


# CORS_ORIGIN_ALLOW_ALL = True

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

# celery Tasks
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

CELERY_BEAT_SCHEDULE = {
    "runs-campaign-for-every-thiry-minutes": {
        "task": "marketing.tasks.run_all_campaigns",
        "schedule": crontab(minute=30, hour="*"),
    },
    "runs-campaign-for-every-five-minutes": {
        "task": "marketing.tasks.list_all_bounces_unsubscribes",
        "schedule": crontab(minute="*/5"),
    },
    "runs-scheduled-campaigns-for-every-one-hour": {
        "task": "marketing.tasks.send_scheduled_campaigns",
        "schedule": crontab(hour="*/1"),
    },
    "runs-scheduled-emails-for-accounts-every-one-minute": {
        "task": "accounts.tasks.send_scheduled_emails",
        "schedule": crontab(minute="*/1"),
    },
}

MAIL_SENDER = "AMAZON"
# INACTIVE_MAIL_SENDER = "MANDRILL"

AM_ACCESS_KEY = os.getenv("AWSACCESSKEYID", "")
AM_PASS_KEY = os.getenv("AWSSECRETACCESSKEY", "")
AWS_REGION = os.getenv("AWS_REGION", "")

# MGUN_API_URL = os.getenv("MGUN_API_URL", "")
# MGUN_API_KEY = os.getenv("MGUN_API_KEY", "")

# MANDRILL_API_KEY = os.getenv("MANDRILL_API_KEY", "")

# Marketing app related
# URL_FOR_LINKS = os.getenv("URLFORLINKS")

# GP_CLIENT_ID = os.getenv("GP_CLIENT_ID", False)
# GP_CLIENT_SECRET = os.getenv("GP_CLIENT_SECRET", False)
# ENABLE_GOOGLE_LOGIN = os.getenv("ENABLE_GOOGLE_LOGIN", False)

MARKETING_REPLY_EMAIL = os.getenv("MARKETING_REPLY_EMAIL")

PASSWORD_RESET_TIMEOUT_DAYS = 3

SENTRY_ENABLED = os.getenv("SENTRY_ENABLED", False)

if SENTRY_ENABLED and not DEBUG:
    if os.getenv("SENTRYDSN") is not None:
        RAVEN_CONFIG = {
            "dsn": os.getenv("SENTRYDSN", ""),
        }
        INSTALLED_APPS = INSTALLED_APPS + [
            "raven.contrib.django.raven_compat",
        ]
        MIDDLEWARE = [
            "raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware",
            "raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware",
        ] + MIDDLEWARE


# HAYSTACK_CONNECTIONS = {
#     'default': {
#         # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#         'ENGINE': 'marketing.search_backends.CustomElasticsearchSearchEngine',
#         'URL': 'http://127.0.0.1:9200/',
#         'INDEX_NAME': 'haystack',
#     },
# }

# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

# ELASTICSEARCH_INDEX_SETTINGS = {
#     "settings": {
#         "analysis": {
#             "analyzer": {
#                 "ngram_analyzer": {
#                     "type": "custom",
#                     "tokenizer": "custom_ngram_tokenizer",
#                     "filter": ["asciifolding", "lowercase"]
#                 },
#                 "edgengram_analyzer": {
#                     "type": "custom",
#                     "tokenizer": "custom_edgengram_tokenizer",
#                     "filter": ["asciifolding", "lowercase"]
#                 }
#             },
#             "tokenizer": {
#                 "custom_ngram_tokenizer": {
#                     "type": "nGram",
#                     "min_gram": 3,
#                     "max_gram": 12,
#                     "token_chars": ["letter", "digit"]
#                 },
#                 "custom_edgengram_tokenizer": {
#                     "type": "edgeNGram",
#                     "min_gram": 2,
#                     "max_gram": 12,
#                     "token_chars": ["letter", "digit"]
#                 }
#             }
#         }
#     }
# }

# HAYSTACK_DEFAULT_OPERATOR = 'AND'

APPLICATION_NAME = "CarCRM"


# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
#         "LOCATION": os.getenv("MEMCACHELOCATION"),
#     }
# }

PASSWORD_RESET_MAIL_FROM_USER = os.getenv("PASSWORD_RESET_MAIL_FROM_USER")

SETTINGS_EXPORT = ["APPLICATION_NAME"]
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

################################################################################
# Set crispy forms settings
################################################################################
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"
################################################################################
# Import Logging settings
################################################################################
from crm.logger import *

################################################################################
# Import EMAIL settings
################################################################################
from crm.email import *

################################################################################
# Import Compress settings
################################################################################
from crm.compres import *

################################################################################
# Import django-jazzmin settings
################################################################################
from crm.jazzmin import JAZZMIN_SETTINGS

################################################################################
# Import Telegram settings
################################################################################
from crm.telegram import *

