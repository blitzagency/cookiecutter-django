from django.conf import settings
from django.contrib.staticfiles.storage import CachedFilesMixin
from storages.backends.s3boto import S3BotoStorage


MEDIA_ROOT_LOCATION = getattr(settings, "MEDIA_ROOT_LOCATION", "uploads")


class OptimizedCachedS3BotoStorage(CachedFilesMixin, S3BotoStorage):
    pass


class OptimizedS3BotoStorage(S3BotoStorage):

    def __init__(self, *args, **kwargs):
        if hasattr(settings, "AWS_CLOUDFRONT_DOMAIN"):
            kwargs["custom_domain"] = settings.AWS_CLOUDFRONT_DOMAIN

        super(OptimizedS3BotoStorage, self).__init__(*args, **kwargs)


def MediaRootS3BotoStorage():
    return S3BotoStorage(location=MEDIA_ROOT_LOCATION)
