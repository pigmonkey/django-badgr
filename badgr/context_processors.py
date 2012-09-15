import flickrapi

from django.core.cache import cache
from badgr import settings


def flickr(request):
    """Return the most recent photos for user."""
    # Check the cache for a badge. If it exists, return it.
    flickr_badge = cache.get('flickr_badge')
    if flickr_badge:
        return {'flickr_badge': flickr_badge}

    flickr_badge = []

    # Register with the API.
    flickr = flickrapi.FlickrAPI(settings.FLICKR_APIKEY)

    # Attempt to get the most recent photos for the user.
    try:
        pool = flickr.photos_search(user_id=settings.FLICKR_USERID,
                                    per_page=settings.FLICKR_NUMPHOTOS)
    except:
        flickr_badge = None
    else:
        # If the API returned successfully, append each photo to the badge.
        if pool.get('stat') == 'ok':
            for photo in pool[0]:
                # Build the filename for the image.
                filename = '%s_%s' % (photo.get('id'), photo.get('secret'))
                if settings.FLICKR_IMAGESIZE:
                    filename += '_%s' % settings.FLICKR_IMAGESIZE
                filename += '.jpg'
                # Build the URL for the image and the flickr page.
                photo.set('image', ('http://farm%s.static.flickr.com/%s/%s'
                                    % (photo.get('farm'),
                                       photo.get('server'),
                                       filename)))
                photo.set('url', 'http://www.flickr.com/photos/%s/%s' %
                                 (photo.get('owner'), photo.get('id')))
                flickr_badge.append(photo.attrib)

        # Add the badge to the cache.
        cache.set('flickr_badge', flickr_badge, settings.FLICKR_TIMEOUT)

    return {'flickr_badge': flickr_badge}
