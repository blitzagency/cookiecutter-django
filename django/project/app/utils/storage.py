from django.conf import settings
from django.contrib.staticfiles.storage import CachedFilesMixin
# from django.core.files.base import ContentFile

from storages.backends.s3boto import S3BotoStorage


class OptimizedCachedS3BotoStorage(CachedFilesMixin, S3BotoStorage):
    pass


class OptimizedS3BotoStorage(S3BotoStorage):

    def __init__(self, *args, **kwargs):
        if hasattr(settings, "AWS_CLOUDFRONT_DOMAIN"):
            kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
        super(OptimizedS3BotoStorage, self).__init__(*args, **kwargs)

MediaRootS3BotoStorage = lambda: S3BotoStorage(location='uploads')
