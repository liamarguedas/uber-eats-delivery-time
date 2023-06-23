import logging
from config.core import PACKAGE_ROOT, config

logging.getLogger(config.app_config.package_name).addHandler(logging.NullHandler())

with open(PACKAGE_ROOT / "VERSION") as version_file:

    __version__ = version_file.read().strip()