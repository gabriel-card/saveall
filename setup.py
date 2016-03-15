import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-saveall',
    version='0.1.5',
    packages=['saveall'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app that adds a custom django-admin command for saving model instances throughout a project.',
    long_description=README,
    url='https://github.com/gabriel-card/saveall',
    author='Gabriel Cardoso',
    author_email='gabriel.cardoso@corp.globo.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 1.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite='runtests.runtests',
)
