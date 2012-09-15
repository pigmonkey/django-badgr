"""
These Flickr settings should not be edited directly.
Instead, overwrite them in the main project's setting file.
"""
from django.conf import settings
from django.core.cache import cache

# The Flickr API key.
# http://www.flickr.com/services/api/keys/
FLICKR_APIKEY = getattr(settings, 'FLICKR_APIKEY', None)

# The Flickr user ID. You can find your ID here:
# http://idgettr.com/
FLICKR_USERID = getattr(settings, 'FLICKR_USERID', None)

# The number of photos to pull. Defaults to 12. Max is 500.
FLICKR_NUMPHOTOS = getattr(settings, 'FLICKR_NUMPHOTOS', 12)

# The number of seconds for which tweets should be stored in the cache.
# Defaults to the Django cache timeout, which defaults to 300 seconds.
FLICKR_TIMEOUT = getattr(settings, 'FLICKR_TIMEOUT', cache.default_timeout)

# The size of the image that you wish to build the URL for.
# Defaults to medium (500 on the longest side). The available options are:
#       's': small square 75x75
#       'q': large square 150x150
#       't': thumbnail, 100 on longest side
#       'm': small, 240 on longest side
#       'n': small, 320 on longest side
#       '' : medium, 500 on the longest side
#       'z': medium, 640 on longest side
#       'c': medium, 800 on longest side
#       'b': large 1024 on longest side
FLICKR_IMAGESIZE = getattr(settings, 'FLICKR_IMAGESIZE', '')
