#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mail.app HJKL movement plugin

Created by: Rui Carmo
License: MIT (see LICENSE for details)
"""

from AppKit import *
from Foundation import *
from Quartz.CoreGraphics import * # CGEvent
import objc

def swizzle(*args):
    """ Brilliant piece of coding from http://klep.name/programming/python/ """
    cls, SEL = args
    def decorator(func):
        oldIMP      = cls.instanceMethodForSelector_(SEL)
        def wrapper(self, *args, **kwargs):
            return func(self, oldIMP, *args, **kwargs)
        newMethod   = objc.selector(wrapper, 
                                    selector  = oldIMP.selector,
                                    signature = oldIMP.signature)
        objc.classAddMethod(cls, SEL, newMethod)
        return wrapper
    return decorator

orthodox_keymap = {
    4:  123, # h maps to cursor left
    37: 124, # l maps to cursor right
    38: 125, # j maps to cursor up
    40: 126  # k maps to cursor down
}

my_keymap = { # when sorting messages in decreasing date order
    4:  115, # h maps to Fn + cursor left
    37: 119, # l maps to Fn + cursor right
    38: 124, # j maps to cursor left  - next message 
    40: 123  # k maps to cursor right - previous message
}

@swizzle(MessagesTableView, 'keyDown:')
def keyDown_(self, original, event):
    code = event.keyCode()
    NSLog('Handling key %d' % code)
    if code in my_keymap.keys():
        NSLog("Changing key %d to %d" % (code, my_keymap[code]))
        original(self, NSEvent.eventWithCGEvent_(CGEventCreateKeyboardEvent(None,my_keymap[code],True)));
    original(self, event)

NSLog("HJKLPlugin: Attempting MVMailBundle lookup...")
MVMailBundle = objc.lookUpClass('MVMailBundle')
class HJKLPlugin(MVMailBundle):

    def initialize (cls):
        NSLog("HJKLPlugin: Attempting to register bundle...")
        MVMailBundle.registerBundle()
        NSLog("HJKLPlugin: Registered with Mail")

    initialize = classmethod(initialize)
