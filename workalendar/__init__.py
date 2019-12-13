import pkg_resources
import gettext

# Load gettext locale files from the package wheel
locale_path = pkg_resources.resource_filename('workalendar', 'locales')
gettext.find('workalendar', localedir=locale_path)

#: Module version, as defined in PEP-0396.
__version__ = pkg_resources.get_distribution(__package__).version
