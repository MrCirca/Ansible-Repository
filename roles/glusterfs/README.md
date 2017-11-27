GlusterFS
==========

Role Variables
--------------

Examples of variables used in this role:
```
glusterfs_volumes:   
    - name: gv51
      stripes: 2
      bricks:
        - /mnt/bricks_striped/brick_0

or

glusterfs_volumes:   
    - name: gv52
      replicas: 2
      bricks:
        - /mnt/bricks_striped/brick_1
```
