from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'ambition_metadata_rules'


if settings.APP_NAME == 'ambition_metadata_rules':
    from edc_metadata.apps import AppConfig as MetadataAppConfig

    class EdcMetadataAppConfig(MetadataAppConfig):
        reason_field = {'ambition_metadata_rules.subjectvisit': 'reason'}
