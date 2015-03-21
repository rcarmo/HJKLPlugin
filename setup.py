#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for HJKLPlugin

Created by: Rui Carmo
License: MIT (see LICENSE for details)
"""
from distutils.core import setup
import py2app

plist = {
    'NSPrincipalClass':'HJKLPlugin',
    'CFBundleInfoDictionaryVersion':'6.0',
    'CFBundlePackageType':'APPL',
    'CFBundleIdentifier':'com.taoofmac.mail.plugins.HJKLPlugin',
    'CFBundleName':'HJKLPlugin',
    'CFBundleSignature':'????',
    'CFBundleGetInfoString':'HJKLPlugin 0.2.2',
    'CFBundleVersion':'0.2.2',
    'CFBundleShortVersionString':'0.2.2',
    'SupportedPluginCompatibilityUUIDs': open('compatibility_UUIDs.txt').read().split(),
}
setup(
 plugin = ['HJKLPlugin.py'],
 options=dict(py2app=dict(extension='.mailbundle', plist=plist))
)
