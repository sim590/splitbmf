#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools
import splitbmf

setuptools.setup(
    name             = splitbmf.__name__,
    version          = splitbmf.__version__,
    packages         = setuptools.find_packages(),
    entry_points     = {
        'console_scripts': [ 'splitbmf = splitbmf.splitbmf:main' ]
    },
    # metadata to display on PyPI
    author           = splitbmf.__author__,
    author_email     = splitbmf.__email__,
    description      = splitbmf.__description__,
    license          = splitbmf.__license__,
    keywords         = "split big media file mp3 ogg youtube",
    url              = "https://github.com/sim590/splitbmf",
    project_urls     = {
        "Source Code": "https://github.com/sim590/splitbmf",
    }
)

#  vim: set sts=4 ts=8 sw=4 tw=120 et :

