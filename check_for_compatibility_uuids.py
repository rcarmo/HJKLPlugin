import subprocess
import os
import re
import sys

compatibility_UUIDs = open('compatibility_UUIDs.txt').read().split()

# have to launch another shell to get defaults not from the root user
UUID_data = os.popen('sh -c "defaults find UUID"').read()
necessary_UUIDs = []
necessary_UUIDs += re.findall(r'MailCompatibilityUUID = "(.*)"', UUID_data)
necessary_UUIDs += re.findall(r'MessageCompatibilityUUID = "(.*)"', UUID_data)

for uuid in necessary_UUIDs:
    if not uuid in compatibility_UUIDs:
        print "Error: the UUID %s is not present in compatibility_UUIDs.txt, Mail may not want to run the plugin" % uuid
        print "to fix this please add the UUID to compatibility_UUIDs.txt."
        sys.exit(1)
