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
    'CFBundleName':'HJKLPlugin',
    'CFBundleSignature':'????',
    'CFBundleGetInfoString':'HJKLPlugin 0.1',
    'CFBundleVersion':'0.1',
    'CFBundleShortVersionString':'0.1',
    'SupportedPluginCompatibilityUUIDs': [
        '225E0A48-2CDB-44A6-8D99-A9BB8AF6BA04',
        'B3F3FC72-315D-4323-BE85-7AB76090224D',
        '2610F061-32C6-4C6B-B90A-7A3102F9B9C8',
        '99BB3782-6C16-4C6F-B910-25ED1C1CB38B',
        '0CB5F2A0-A173-4809-86E3-9317261F1745',
        '2F0CF6F9-35BA-4812-9CB2-155C0FDB9B0F',
        'B842F7D0-4D81-4DDF-A672-129CA5B32D57',
        'E71BD599-351A-42C5-9B63-EA5C47F7CE8E',
        'BDD81F4D-6881-4A8D-94A7-E67410089EEB',
        '857A142A-AB81-4D99-BECC-D1B55A86D94E',
        '36555EB0-53A7-4B29-9B84-6C0C6BACFC23',
        '9049EF7D-5873-4F54-A447-51D722009310',
        '1C58722D-AFBD-464E-81BB-0E05C108BE06',
        '2DE49D65-B49E-4303-A280-8448872EFE87',
        '1146A009-E373-4DB6-AB4D-47E59A7E50FD',
        '6E7970A3-E5F1-4C41-A904-B18D3D8FAA7D',
        'EF59EC5E-EFCD-4EA7-B617-6C5708397D24',                 
        '4C286C70-7F18-4839-B903-6F2D58FA4C71',                 
        '608CE00F-4576-4CAD-B362-F3CCB7DE8D67',                 
        '758F235A-2FD0-4660-9B52-102CD0EA897F',                 
        '3335F782-01E2-4DF1-9E61-F81314124212',    
    ]
}
setup(
 plugin = ['HJKLPlugin.py'],
 options=dict(py2app=dict(extension='.mailbundle', plist=plist))
)
