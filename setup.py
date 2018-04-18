import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-exchange-maploom',
    version='1.5.129',
    author='GeoNode Development Team - Prominent Edge, Terranodo, Boundless Spatial',
    author_email='exchange@boundlessgeo.com',
    url='https://github.com/boundlessgeo/django-exchange-maploom',
    download_url="https://github.com/boundlessgeo/django-exchange-maploom",
    description="Use MapLoom in your django projects.",
    long_description=open(os.path.join(here, 'README.md')).read(),
    license='See LICENSE file.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=['Topic :: Utilities',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Intended Audience :: Developers',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Development Status :: 1 - Planning',
                 'Programming Language :: Python :: 2.7'],
)
