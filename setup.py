import sys
from setuptools import setup

long_description = ''
if 'upload' in sys.argv or 'register' in sys.argv:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')

setup(
    name='django-bootstrap-datepicker',
    packages=['pretty_bootstrap_datepicker'],
    package_data={
        'pretty_bootstrap_datepicker': [
            'static/css/*.css',
            'static/js/*.js',
            'static/js/locales/*.js',
            'templates/*',
        ]
    },
    install_requires=[
        'django>=2',
        'django-filter>=1.1.0',
        'django-bootstrap-daterangepicker>=1.0.1',
    ],
    include_package_data=True,
    version='1.2.3',
    description='Bootstrap 3/4 compatible datepicker for Django projects.',
    long_description=long_description,
    author='Paul Bucher, Shivam Sharma',
    author_email='paulb@lctcb.org sharma.shivam0611@gmail.com',
    url='https://github.com/sharma0611/django-bootstrap-datepicker',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
