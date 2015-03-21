#!/bin/sh
echo "Cleaning up..."
rm -rf dist/ build/
echo "Checking compatibility UUIDs..."
python check_for_compatibility_uuids.py
if [ $? -ne 0 ]; then
	echo "Install stopped"
	exit 1
fi

echo "Building plugin..."
python setup.py py2app > /dev/null
echo "Removing any previous version of it"
rm -rf ~/Library/Mail/Bundles/HJKLPlugin.mailbundle
echo "Code signing with '$1'..."
export CERT=$1
find dist -print | egrep .so$ | xargs codesign -fv -s "$CERT" > /dev/null
find dist -print | egrep -i python$ | xargs codesign -fv -s "$CERT" > /dev/null
echo "Installing new version"
mv dist/HJKLPlugin.mailbundle ~/Library/Mail/Bundles
echo "Removing build files."
rm -rf dist/ build/ > /dev/null
echo "Done. Quit Mail.app and restart it to load plugin. Watch the console for errors."
