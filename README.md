# Ansible Glusterfs Proxmox roles
It's a deployment that automates the installation of Glusterfs and Proxmox stack. This project, has 3 main roles.
1. Proxmox role: Exchange ssh public keys between hosts and create cluster.
2. LVM role: Prepare volume groups and logical volumes which will be used for GlusterFS
3. Glusterfs role: Create Glusterfs cluster and create gluster volume

## Getting Started
You should clone the repository
```
https://github.com/MrCirca/ansible-glusterfs-proxmox.git
```
### Prepare your deployment
In directory group_vars you can configure volume_group names, physical_volumes, size, logical volumes, mountpoint etc.

### Inventory and Executing
In /etc/ansible/hosts inventory i defined group with hosts like this
```
[test_glusterfs_nodes] # test is the target world which you define( -e target=test) when you execute the playbook
test1.in.modulus.gr 
test2.in.modulus.gr

```
Executing
```
ansible-playbook --private-key=path_of_your_private_key -u root main.yml -e target=test
```

### group_vars / host_vars structure
```
---
lvm_volume_groups:
  gluster_vg_0: # Name of volume group.
    physical_volumes:
      - /dev/vda #List of physical devices.

lvm_logical_volumes:
  glusterfs_storage: #Name of logical volume.
    vg: gluster_vg_0 #Name of volume group which is already defined.
    size: 10G #Size of logical volume.

filesystems:
  - device: /dev/gluster_vg_0/glusterfs_storage #Path of the logical volume.
    mountpoint: /mnt/bricks # Path where logical volume will do mount.
    fs: ext4 # Type of filesystem.

replication_volume:
  name: gv50 # Name of gluster replication volume
  bricks: # List of bricks
    - /mnt/bricks/brick_0
```
ansible-playbook --private-key=path_of_your_private_key -u root main.yml -e target=name_of_group
