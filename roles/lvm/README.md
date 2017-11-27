LVM
========

LVM deployment tasks for debian systems.

Role Variables

Examples of variables used in this role:
```
lvm_volume_groups:
  gluster_vg_1:
    physical_volumes:
      - /dev/vda

lvm_logical_volumes:
  glusterfs_storage:
    vg: gluster_vg_1
    size: 15G
```
