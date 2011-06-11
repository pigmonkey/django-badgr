from setuptools import setup, find_packages

setup(
    name = 'django-badgr',
    version = '0.1',
    description = 'A resuable Django application to display a Flickr badge.',
    long_description = open('README.md').read(),
    url = 'https://github.com/pigmonkey/django-badgr',
    author = 'Pig Monkey',
    author_email = 'pm@pig-monkey.com',

    packages = find_packages(),
    zip_safe=False,
)
