#!/usr/bin/python
import json
import subprocess
import xml.etree.ElementTree as ET
import sys

volume_name = sys.argv[1]

gluster_volumes_xml = subprocess.check_output('gluster --xml volume status ' + volume_name, shell=True)

root  = ET.fromstring(gluster_volumes_xml)

#def volumeNames():
#    volumes = root.find('volStatus').find('volumes').findall('volume')
#    
#    for volume_name in volumes:
#                            gluster_volume_name = volume_name.find('volName').text
#                                    gluster_volume_info.append({"#VOLUME_NAME": gluster_volume_name})
#
#                                        return json.dumps({'data': gluster_volume_info})
#
#                                    test = sys.argv[1]
#
#                                    if test == "volumes":
#                                            print(volumeNames())

