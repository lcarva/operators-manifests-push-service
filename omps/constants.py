#
# Copyright (C) 2019 Red Hat, Inc
# see the LICENSE file for license
#

ENV_CONF_FILE = 'OMPS_CONF_FILE'
ENV_CONF_SECTION = 'OMPS_CONF_SECTION'
ENV_DEVELOPER_ENV = 'OMPS_DEVELOPER_ENV'

DEFAULT_ZIPFILE_MAX_UNCOMPRESSED_SIZE = 1024 * 1024 * 20  # 20MB
DEFAULT_MAX_CONTENT_LENGTH = 1024 * 1024 * 2  # 2MB

DEFAULT_RELEASE_VERSION = '1.0.0'

ALLOWED_EXTENSIONS = {".zip", }

KOJI_OPERATOR_MANIFESTS_ARCHIVE_KEY = 'operator_manifests_archive'
