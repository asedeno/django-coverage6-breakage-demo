from django.conf import settings

# This is just an example of getting something from django settings.
# If django is initialized, it works; if not it raises.
is_debug = getattr(settings, 'DEBUG', False)
