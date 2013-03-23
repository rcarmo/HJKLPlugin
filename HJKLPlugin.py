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


list_keymap = {
    # message list
    4:  123, # h maps to cursor left
    37: 124, # l maps to cursor right
    38: 125, # j maps to cursor down
    40: 126  # k maps to cursor up
}


msg_keymap = {
    # message view, when sorting messages in decreasing date order
    4:  115, # h maps to Fn + cursor left
    37: 119, # l maps to Fn + cursor right
    38: 124, # j maps to cursor left  - next message 
    40: 123  # k maps to cursor right - previous message
}


def change_keyCode_(self, original, event, keymap):
    code = event.keyCode()
    #NSLog('Handling key %d' % code)
    if code in keymap.keys():
        #NSLog("Changing key %d to %d" % (code, keymap[code]))
        original(self, NSEvent.eventWithCGEvent_(CGEventCreateKeyboardEvent(None,keymap[code],True)));
        return None # kill original event
    original(self, event)


@swizzle(MailTableView, 'keyDown:')
def keyDown_(self, original, event):
    #NSLog("RichTableCellView")
    change_keyCode_(self, original, event, list_keymap)


@swizzle(MessagesTableView, 'keyDown:')
def keyDown_(self, original, event):
    #NSLog("MessagesTableView")
    change_keyCode_(self, original, event, msg_keymap)


MVMailBundle = objc.lookUpClass('MVMailBundle')
class HJKLPlugin(MVMailBundle):

    def initialize (cls):
        MVMailBundle.registerBundle()
        NSLog("Loaded HJKLPlugin Bundle")

    initialize = classmethod(initialize)
