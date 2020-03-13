import pkg_resources
import gettext as std_gettext

# Load gettext locale files from the package wheel
locale_path = pkg_resources.resource_filename('workalendar', 'locales')
trans = std_gettext.translation(
    'workalendar', localedir=locale_path, fallback=True
)
gettext = trans.gettext


#: Module version, as defined in PEP-0396.
__version__ = pkg_resources.get_distribution(__package__).version
