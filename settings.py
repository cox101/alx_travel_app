import environ

env = environ.Env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
    }
}
