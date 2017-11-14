# Ansible Glusterfs Proxmox roles
It's a deployment that automates the installation of Glusterfs and Proxmox stack. This project, has 3 main roles.
1. Proxmox role: Exchanging hosts ssh public keys and create cluster.
2. LVM role: Prepare volumes which will be used for GlusterFS
3. Glusterfs role: Create Glusterfs cluster and create gluster volume

## Getting Started
You should clone the repository
```
https://github.com/MrCirca/ansible-glusterfs-proxmox.git
```
### Prepare your deployment
In directory group_vars you can configure volume_group names, physical_volumes, size, logical volumes, mountpoint etc.

### group_vars / host_vars structure
```
---
lvm_volume_groups:
  gluster_vg_0:
    physical_volumes:
      - /dev/vda

lvm_logical_volumes:
  glusterfs_storage:
    vg: gluster_vg_0
    size: 10G



#Glusterfs brick's directories
bricks:
  brick_0:
   path: /mnt/bricks/brick_0

filesystems:
  - device: /dev/gluster_vg_0/glusterfs_storage
    mountpoint: /mnt/bricks
    fs: ext4

replication_volume:
  name: gv50
  bricks:
    - /mnt/bricks/brick_0
```
