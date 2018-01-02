#!/usr/bin/python
import json
import subprocess
import xml.etree.ElementTree as ET
import sys
import re

volume_name = sys.argv[1]
vol_info = sys.argv[2]
gluster_volumes_xml = subprocess.check_output('gluster --xml volume status ' + volume_name + ' detail', shell=True)

gluster_volumes_heal_xml = subprocess.check_output('gluster --xml volume heal ' + volume_name + ' info', shell= True)

root  = ET.fromstring(gluster_volumes_xml)
root_heal = ET.fromstring(gluster_volumes_heal_xml)
def glusterVolumeInfo():
    gluster_volumes = root.find('volStatus').find('volumes').findall('volume')    
    for gluster_node in gluster_volumes:
        gluster_volume_bricks = gluster_node.findall('node')
        gluster_node_info = []
        for info in gluster_volume_bricks:
            gluster_brick_hostname = info.find('hostname').text
            gluster_brick_status = info.find('status').text
            gluster_brick_sizetotal = info.find('sizeTotal').text
            gluster_brick_sizefree = info.find('sizeFree').text
            if vol_info == "hostname":
                gluster_node_info.append({"#BRICK_HOSTNAME": gluster_brick_hostname})
            elif vol_info == "status":
                gluster_node_info.append({"#BRICK_STATUS": gluster_brick_status})
            elif vol_info == "sizetotal":
                gluster_node_info.append({"#BRICK_SIZETOTAL": gluster_brick_sizetotal})
            elif vol_info == "sizefree":
                gluster_node_info.append({"#BRICK_SIZEFREE": gluster_brick_sizefree})
            else:
                print("No valid argument")
        return json.dumps({'data': gluster_node_info})

def glusterVolumeHealInfo():
    volumes = root_heal.find('healInfo').find('bricks')
    gluster_heal_info = []
    for volume_brick in volumes:
        gluster_volume_bricks = volume_brick.findall('.')
        for gluster_brick_heal_info in gluster_volume_bricks:
            if vol_info == "heal_noe":
                gluster_heal_info.append({"#BRICK_HEAL_NUMBER_OF_ENTRIES": gluster_volume_brick_numberofentries})
            elif vol_info == "heal_status":
                gluster_volume_brick_status = gluster_brick_heal_info.find('status').text
            else:
                print("No valid argument")
    return json.dumps({'data': gluster_heal_info})

print(glusterVolumeInfo())
#print(glusterVolumeHealInfo())
