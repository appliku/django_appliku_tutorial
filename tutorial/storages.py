from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'
