from .common import *

DEBUG = False

ALLOWED_HOSTS = [*]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER':'root',
        'PASSWORD':'root',
    }
}

AWS_S3_FILE_OVERWRITE = False

AWS_IS_GZIPPED = True
AWS_S3_SECRET_ACCESS_KEY = 'xxxxxxxxx'
AWS_S3_ACCESS_KEY_ID = 'xxxxxxxx'
AWS_STORAGE_BUCKET_NAME = 'bucket-name'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_CLOUDFRONT_DOMAIN ='cdn_url'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'starter.aws_s3_storages.MediaStorage'
MEDIA_URL = "https://%s/%s/" % (AWS_CLOUDFRONT_DOMAIN, MEDIAFILES_LOCATION)
