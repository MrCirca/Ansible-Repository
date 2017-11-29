DRBD
========

Tasks for deploying a DRBD node.

You also have to use LVM role.


Role Variables

--------------

Examples of variables used in this role:
```
lvm_volume_groups:
  drbdpool:
    physical_volumes:
      - /dev/vda

lvm_logical_volumes:
  drbdthinpool:
    vg: drbdpool
    size: 15G

proxmox_drbd_storage:
  - storage_name: drbdstorage
    redudancy: "{{ groups['drbd_nodes'] | count }}"
```
