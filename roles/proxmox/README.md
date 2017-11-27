Proxmox
========

Proxmox deployment tasks for debian systems.

Role Variables:

These variables are used for proxmox storage.
```
proxmox_mount_volumes:
  - server1: "{{ groups['glusterfs_nodes'][0] }}"
    server2: "{{ groups['glusterfs_nodes'][1] }}"
    name: gv51
    id: glusterfs_striped_storage
```
