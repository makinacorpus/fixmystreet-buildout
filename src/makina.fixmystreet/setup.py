#!/usr/bin/env python
# -*- coding: utf-8 -
from setuptools import setup, find_packages

name = 'makina.fixmystreet' 
setup(
    name=name,
    namespace_packages=[         'makina', 
         'makina.fixmystreet',],  

    version = '1.0',
    description = 'Project makina.fixmystreet',
    long_description = '' ,
    author = 'kiorky <kiorky@localhost>',
    author_email = 'kiorky@localhost',
    license = 'GPL',
    keywords = '',
    url='http://www.generic.com',
    install_requires = [],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    # Make setuptools include all data files under version control,
    # svn and CVS by default
    include_package_data=True,
    zip_safe=False,
    extras_require={'test': ['IPython', 'zope.testing', 'mocker']},
    entry_points = {
        'console_scripts': [
            'fixmystreet-manage = makina.fixmystreet.fixmystreet:main' ,
        ],
    }
)


