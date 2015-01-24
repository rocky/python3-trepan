#!/usr/bin/env python3

copyright   = '''Copyright (C) 2013 Rocky Bernstein <rocky@gnu.org>.'''
classifiers =  ['Development Status :: 4 - Beta',
                'Environment :: Console',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Software Development :: Debuggers',
                'Topic :: Software Development :: Libraries :: Python Modules',
                ]

# The rest in alphabetic order
author             = "Rocky Bernstein"
author_email       = "rocky@gnu.org"
ftp_url            = None
install_requires   = ['columnize >= 0.3.4',
                      'import-relative >= 0.2.1',
                      'pyficache >= 0.2.2',
                      'pygments',
                      'tracer >= 0.3.1']
license            = 'GPL'
mailing_list       = 'python-debugger@googlegroups.com'
modname            = 'trepan'
namespace_packages = [
    'trepan',
    'trepan.bwprocessor',
    'trepan.interfaces',
    'trepan.io',
    'trepan.lib',
    'trepan.processor',
    'trepan.processor.command',
#    'trepan.processor.command.ipython_magic',
    'trepan.processor.command.info_subcmd',
    'trepan.processor.command.set_subcmd',
    'trepan.processor.command.show_subcmd'
]
packages           = namespace_packages
py_modules         = None
short_desc         = 'GDB-like Python3 Debugger in the Trepan family'

import os
import os.path, sys
from import_relative import get_srcdir

# VERSION.py sets variable VERSION.
me = os.path.join(os.path.dirname(__file__), 'trepan', 'VERSION.py')
exec(compile(open(me).read(), me, 'exec'))
version            = VERSION
web                = 'http://code.google.com/p/trepan/'

# tracebacks in zip files are funky and not debuggable
zip_safe = False

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()
long_description   = ( read("README.txt") + '\n\n' +  read("NEWS") )

__import__('pkg_resources')
from setuptools import setup

setup(
       author             = author,
       author_email       = author_email,
       classifiers        = classifiers,
       description        = short_desc,
      entry_points = {
       'console_scripts': [
           'trepan3k  = trepan.cli:main',
           'trepan3k-client = trepan.client:main',
       ]},
       install_requires   = install_requires,
       license            = license,
       long_description   = long_description,
       py_modules         = py_modules,
       name               = modname,
       namespace_packages = namespace_packages,
       packages           = packages,
       test_suite         = 'nose.collector',
       url                = web,
       setup_requires     = ['nose>=1.0'],
       version            = VERSION,
       zip_safe           = zip_safe)
