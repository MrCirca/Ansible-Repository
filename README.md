# Ansible repository
It's an Ansible repository.
1. Proxmox role: Exchange ssh public keys between hosts and create Proxmox cluster.
2. Filesystem role: Has tasks for filesystem creation
3. LVM role: Prepare volume groups and logical volumes which will be used for GlusterFS storage
4. Glusterfs role: Create Glusterfs cluster and create gluster volume
5. DRBD9 role: Create DRBD9 cluster

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
or
```
[drbd_nodes]
test1.in.modulus.gr
test2.in.modulus.gr
```
### Deploying
```
$ ansible-playbook --private-key=path_of_your_private_key -u root drbd/glusterfs.yml -e storage_type="drbd/glusterfs"
```
Each role has README.md about variables that will be used.

