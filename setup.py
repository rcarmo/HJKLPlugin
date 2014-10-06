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
        '2183B2CD-BEDF-4AA6-AC18-A1BBED2E3354',
        '19B53E95-0964-4AAB-88F9-6D2F8B7B6037',
        '2B98D2DD-000B-4521-83EB-7BFCB9B161C8',
        '0941BB9F-231F-452D-A26F-47A43863C991',
        'FBE5B158-5602-4A6D-9CC5-8461B9B7054E',
        'DAFFB2B4-77BC-4C25-8CE1-2405E652D54B',
        '1CD40D64-945D-4D50-B12D-9CD865533506',
        '88ED2D4C-D384-4BF5-8E94-B533455E6AAF',
        'F4C26776-22B3-4A0A-96E1-EA8E4482E0B5',
        'D1EFE124-86FF-4751-BF00-80B2C0D6F2E4',
        'FBD91264-8866-4DEB-AFBF-F08505810056',
        'DAFFB2B4-77BC-4C25-8CE1-2405E652D54B'
    ]
}
setup(
 plugin = ['HJKLPlugin.py'],
 options=dict(py2app=dict(extension='.mailbundle', plist=plist))
)
