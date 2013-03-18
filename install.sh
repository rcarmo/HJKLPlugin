#!/bin/sh
echo "Cleaning up..."
rm -rf dist/ build/
echo "Building plugin..."
python setup.py py2app
echo "Removing any previous version of it"
rm -rf ~/Library/Mail/Bundles/HJKLPlugin.mailbundle
echo "Installing new version"
mv dist/HJKLPlugin.mailbundle ~/Library/Mail/Bundles
echo "Done. Quit Mail.app and restart it to load plugin. Watch the console for errors."
