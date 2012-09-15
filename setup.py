from setuptools import setup, find_packages

setup(
    name='django-badgr',
    packages=find_packages(),
    version='1.0',
    description='A resuable Django application used to display a Flickr badge.',
    author='Peter Hogg',
    author_email='peter@havenaut.net',
    url='https://github.com/pigmonkey/django-badgr',
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
    ],
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['flickrapi'],
)
