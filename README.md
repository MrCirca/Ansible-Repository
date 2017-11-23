# Ansible Glusterfs Proxmox roles
It's a deployment that automates the installation of Glusterfs and Proxmox stack. This project, has 4 main roles.
1. Proxmox role: Exchange ssh public keys between hosts and create Proxmox cluster.
2. Common role: Has tasks for filesystem creation
3. LVM role: Prepare volume groups and logical volumes which will be used for GlusterFS storage
4. Glusterfs role: Create Glusterfs cluster and create gluster volume

## Getting Started
You should clone the repository
```
https://github.com/MrCirca/ansible-glusterfs-proxmox.git
```
### Prepare your deployment
In directory group_vars you can configure volume_group names, physical_volumes, size, logical volumes, mountpoint etc.

### Inventory and Executing
In /etc/ansible/hosts inventory is defined group with hosts like this
```
[glusterfs_nodes] 
test1.in.modulus.gr 
test2.in.modulus.gr

```
Executing
```
$ ansible-playbook --private-key=path_of_your_private_key -u root main.yml
```

### group_vars / host_vars Structure
```yaml
lvm_volume_groups:
  gluster_vg_0:  # Volume group name
    physical_volumes:
      - /dev/vda  # Physical device (partitions or disks)

lvm_logical_volumes:
  glusterfs_storage:
    vg: gluster_vg_0  # Volume group name
    size: 10G  # Logical volume size

filesystems:
  - device: /dev/volume_group_name/logical_volume_name
    mountpoint: /mnt/bricks
    fs: ext4

glusterfs_volumes:
    - name: gv50
      replicas: 2  # If you want replicated or distributed replicated volume you should define number_of_replicas
      stripes: 0  # If you want striped or distributed striped volume you should define number_of_stripes
      bricks:
        - /mnt/bricks/brick_0
proxmox_mount_volumes:
  - server1: "{{ groups['glusterfs_nodes'][0] }}"  # The first node in group is always the Leader node
    server2: "{{ groups['glusterfs_nodes'][1] }}"
    name: gv50
    id: glusterfs_storage
```

