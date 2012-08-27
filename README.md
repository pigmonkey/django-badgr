django-badgr
===========

A resuable [Django](http://www.djangoproject.com) application to display a [Flickr](http://www.flickr.com) badge.

django-badgr uses the [Flickr API](http://www.flickr.com/services/api/) to [search](http://www.flickr.com/services/api/flickr.photos.search.html) Flickr and return a user's most recent photos. The results are cached and stored in the Django context. The photo pool is then accessible as a template variable.


Requirements
------------

* [flickrapi](http://stuvel.eu/flickrapi) is used to interface with the Flickr API.


Installation
------------

1. Put the `badgr` directory somewhere inside your Python path (like in your Django project folder).
2. Add `badgr.context_processors.flickr` to your `settings.TEMPLATE_CONTEXT_PROCESSORS`.

   A good way to do this with overriding all of Django's default context processors is to first import the variable from the global settings and then append to it:

        from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

        TEMPLATE_CONTEXT_PROCESSORS += (
            'badgr.context_processors.flickr',
        )


### Optional

If you want to take advantage of django-badgr's default template, add `badgr` to your `settings.INSTALLED_APPS`.


Usage
-----

After installing, the `flickr_badge` variable will be available to all templates. This is a list of dictionaries, each containing all information returned by the Flickr API for each photo. In addition, the URL both to the image itself and to the associated Flickr badge have been prebuilt and are included in the dictionary.

If you have added `badgr` to your `settings.INSTALLED_APPS`, django-badgr's default template will be available for use. This outputs a list of images, each linked to the corresponding Flickr page. To use it, simply include the template in your desired location.

    {% include 'badgr/photos.html' %}


Settings
--------

django-badgr includes a few settings that you may define in your project's main `settings` file.

### `FLICKR_APIKEY`

The Flickr API key to use. This can be acquired at http://www.flickr.com/services/api/keys/

### `FLICKR_USERID`

The Flickr user ID to use. This is the ugly string on characters, not the pretty name you may have set for your account. If you do not know your user ID, you may find it at http://idgettr.com/

### `FLICKR_NUMPHOTOS`

The number of photos to pull. This defaults to 12. Flickr's maximum is 500.

### `FLICKR_TIMEOUT`

For how long should the photo pool be stored in the cache. The default is 5 minutes. Flickr requests that an application not make more than 3600 requests per API key per hour.

### `FLICKR_IMAGESIZE`

The size of the image you wish to build the URL for. The default is medium (500 on the longest side). Available options are:

* 's': small square 75x75
* 'q': large square 150x150
* 't': thumbnail, 100 on longest side
* 'm': small, 240 on longest side
* 'n': small, 320 on longest side
* '' : medium, 500 on the longest side
* 'z': medium, 640 on longest side
* 'c': medium, 800 on longest side
* 'b': large 1024 on longest side
