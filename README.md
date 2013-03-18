HJKLPlugin
==========

A plugin for vim keybindings in Mac OS X Mail

# So what does this do?

It's a simple plugin that lets you use `vim` keybindings in Mac OS X's Mail.app.

At the moment, it only works on the message view pane (to navigate all messages in a given thread) and in the message list (to move the selection up or down and to expand/collapse threads).

# How do I install it?

Run `install.sh`. That will build and deploy the `.bundle` to your `~/Library/Mail/Bundles` folder.

# What sort of magic is this?

It's a bit of Python that swizzles Objective-C methods and handles keypresses, mapping them to the codes Mail.app expects.

# References

* [vim keybindings for Lion Mail.app](http://the.taoofmac.com/space/blog/2011/08/13/2110)
* [Making your mail sit up and beg](http://the.taoofmac.com/space/blog/2011/08/11/2240)
