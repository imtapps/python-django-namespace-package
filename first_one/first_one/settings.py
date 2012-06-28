import sys
import os

VIRTUAL_NAMESPACE = ["sample", "main"]
local_package = os.path.abspath('/'.join(VIRTUAL_NAMESPACE))
__import__('.'.join(VIRTUAL_NAMESPACE))
sys.modules['.'.join(VIRTUAL_NAMESPACE)].__dict__["__path__"].insert(0, local_package)

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '.db',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'sample.main.one',
)
