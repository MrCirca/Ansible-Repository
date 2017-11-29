Proxmox
========

Proxmox deployment tasks for debian systems.

Role Variables:

These variables are used for proxmox storage.

For GlusterFS
```
proxmox_mount_volumes:
  - server1: "{{ groups['glusterfs_nodes'][0] }}"
    server2: "{{ groups['glusterfs_nodes'][1] }}"
    name: gv51
    id: glusterfs_striped_storage
```

For DRBD
```
drbd:drbdstorage
       redudancy: {{ groups['drbd_nodes'] | count }}
       content images,rootdir,iso

```
