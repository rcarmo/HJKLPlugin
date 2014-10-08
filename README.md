HJKLPlugin
==========

A plugin for vim key bindings in Mac OS X Mail

## Mac OS X 10.10/10.9 (Yosemite/Mavericks) Compatibility Note

> Last version tested: Mail Version 8.0 (1988) / OS X Version 10.10 (14A386b)

This is currently compatible with 10.9+ _provided you're willing to sign the plugin yourself_. This is because Apple now requires code signatures (you can, however, use a self-signed certificate).

## So what does this do?

It's a simple plugin that lets you use `vim` keybindings in Mac OS X's Mail.app (up to and including version 6.6, which ships with 10.8.5, 7.3, which ships with 10.9.4, and 8.0, which ships with 10.10)

At the moment, it only works on the message view pane (to navigate all messages in a given thread) and in the message list (to move the selection up or down and to expand/collapse threads).

It also allows you to hit `x` to delete a message and `v` to open the _first_ URL in an HTML message in the browser (useful if, like me, you miss Google Reader)

## How do I install it?

If you're brave enough, you can try out a pre-built bundle from the [releases page](https://github.com/rcarmo/HJKLPlugin/releases) - just drop the `.bundle` to your `~/Library/Mail/Bundles` folder and restart Mail.

### Before installing

Before installing the plug-in, you'll need to make sure that Mail.app's plug-in support is turned on by running the following two commands in Terminal.app:

    defaults write com.apple.mail EnableBundles -bool true
    defaults write com.apple.mail BundleCompatibilityVersion 3

### Doing it from source

If you're running an older version of Mac OS X, run `sh install.sh` under your own account (i.e., do *not* use `sudo`, under any circumstances!).

For installing in Mavericks (10.9) or Yosemite (10.10), you'll also need to have a self-signed certificate in your `login` keychain. To create one, follow [this Mac Developer Library article][mdl].

Then run `sh install_signed.sh "<certificate name>"` under your own account.

That will build, `codesign` and deploy the `.bundle` to your `~/Library/Mail/Bundles` folder.

## What manner of dark magic is this?

It's a bit of Python that swizzles Objective-C methods and handles keypresses, mapping them to the codes Mail.app expects. The whole codebase fits in a screenful, and you can tweak it to your liking with minimal effort.

## References

* [vim keybindings for Lion Mail.app](http://the.taoofmac.com/space/blog/2011/08/13/2110)
* [Making your mail sit up and beg](http://the.taoofmac.com/space/blog/2011/08/11/2240)

## In case of Mac OS X Upgrades

Whenever Apple updates Mail.app, you need to update the compatibility UUIDs in `setup.py` and rebuild the plugin. To figure out the required UUIDs, you need to issue these  commands:

    # For Mac OS X 10.8.x
    defaults read /Applications/Mail.app/Contents/Info PluginCompatibilityUUID
    defaults read /System/Library/Frameworks/Message.framework/Resources/Info PluginCompatibilityUUID

    # For Mac OS X 10.9.x/10.10.x
    defaults find UUID | grep MailCompatibility
    defaults find UUID | grep MessageCompatibility

Add the new UUIDs to `setup.py` and reinstall.

Of course, Apple can change Mail.app's UI as they please. In that case, you'll need to figure out which Cocoa views are involved and refactor the method swizzling.

In either case, feel free to fork this project and send me a pull request. I am unlikely to upgrade all my machines to bleeding edge versions, so you'll likely be ahead of me and able to help out others.

[mdl]: https://developer.apple.com/library/mac/documentation/Security/Conceptual/CodeSigningGuide/Procedures/Procedures.html#//apple_ref/doc/uid/TP40005929-CH4-SW2
