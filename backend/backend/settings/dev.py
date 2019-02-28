from backend.settings.common import Common


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
