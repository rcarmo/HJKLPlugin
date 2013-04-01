#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mail.app HJKL movement plugin

Created by: Rui Carmo
License: MIT (see LICENSE for details)
"""

from AppKit import *
from Foundation import *
from ScriptingBridge import *
from Quartz.CoreGraphics import * # CGEvent
import objc
import email
import subprocess
from HTMLParser import HTMLParser

class HREFParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            if attrs['href'].startswith('http'):
                self.hrefs.append(attrs['href'])


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


def view_first_link():
    try:
        mail_app = SBApplication.applicationWithBundleIdentifier_("com.apple.Mail")
        source = mail_app.selection()[0].source()
    except Exception, e:
        NSLog('Could not obtain source of message. %s' % e)
        return

    p = HREFParser()
    msg = email.message_from_string(source.encode('utf-8'))
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            payload = part.get_payload(None, True).replace('\r','')
            p.feed(payload)
            if len(p.hrefs):
                subprocess.call("open '%s'" % p.hrefs[0], shell=True)
                return


orthodox_keymap = {
    4:  123, # h maps to cursor left
    37: 124, # l maps to cursor right
    38: 125, # j maps to cursor up
    40: 126, # k maps to cursor down
    7:  51   # x maps to backspace
}


list_keymap = {
    # message list
    4:  123, # h maps to cursor left
    37: 124, # l maps to cursor right
    38: 125, # j maps to cursor down
    40: 126, # k maps to cursor up
    7:  51   # x maps to backspace
}


msg_keymap = {
    # message view, when sorting messages in decreasing date order
    4:  115, # h maps to Fn + cursor left
    37: 119, # l maps to Fn + cursor right
    38: 124, # j maps to cursor left  - next message 
    40: 123, # k maps to cursor right - previous message
    7:  51   # x maps to backspace
}


def change_keyCode_(self, original, event, keymap):
    code = event.keyCode()
    #NSLog('Handling key %d' % code)
    if code == 9: # v
        view_first_link()
    elif code in keymap.keys():
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
