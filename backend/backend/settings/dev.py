from .common import Common


class Dev(Common):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'jobops',
            'USER': 'tklarryonline',
            'PASSWORD': 'asdfg12345',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }

    # we whitelist localhost:3000 because that's where frontend will be served
    CORS_ORIGIN_WHITELIST = (
        'localhost:3000/'
    )

    @property
    def INSTALLED_APPS(self):
        return super(Dev, self).INSTALLED_APPS + [
            'django_extensions',
        ]
