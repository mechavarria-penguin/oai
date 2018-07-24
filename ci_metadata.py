#!/usr/bin/python

import sys
import os
from cobbler import api

# Connect to Cobbler API, get installed system info
cobbler_api = api.BootAPI()
systems = cobbler_api.systems()
box = systems.find(sys.argv[1])
hostname = box.hostname
instance_id = box.uid

# Set metadata variables
metadata_dir = "/var/www/cobbler/localmirror/mds/"
metadata_filename = "meta-data"
userdata_filename = "user-data"
ssh_key = "ssh-rsa xxxxxxxxxxxxxxxxxxxxxxxxxxx"

metadata_dir = metadata_dir + hostname + "/"

# Check if metadata dir exists.
# If it doesn't, create it.
if not os.path.exists(metadata_dir):
    try:
        os.makedirs(metadata_dir)
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

metadata_filename = metadata_dir + metadata_filename
userdata_filename = metadata_dir + userdata_filename

# Write metadata files
md_file = open(metadata_filename, "w")
md_file.write('instance-id: {0}\nlocal-hostname: {1}'.format(instance_id, hostname))
md_file.close()

ud_file = open(userdata_filename, "w")
ud_file.write('#cloud-config\nusers:\n  - name: demo\n    groups: sudo\n    shell: /bin/bash\n    sudo: [\'ALL=(ALL) NOPASSWD:ALL\']\n    ssh-authorized-keys:\n      - {0}'.format(ssh_key))
ud_file.close()
