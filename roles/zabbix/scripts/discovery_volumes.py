#!/usr/bin/python
import subprocess
import xml.etree.ElementTree as ET

gluster_volumes_xml = subprocess.check_output('gluster --xml volume status all detail', shell=True)

#print(gluster_volumes_xml)
root  = ET.fromstring(gluster_volumes_xml)

volumes = root.find('volStatus').find('volumes').findall('volume')

for node in volumes:
    for info in node.findall('node'):
        print(info.find('hostname').text)
        print(info.find('path').text)
        print(info.find('status').text)

