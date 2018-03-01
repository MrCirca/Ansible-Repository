Mikrotik Radius Client
======================

Mikrotik Radius Client deployment tasks for Mikrotik Routers.

Role Variables

Examples of variables used in this role:
```
mikrotik_radius_clients:
  - radius_server_address: 192.168.1.1
    radius_server_shared_secret: test_password
    radius_incoming: "yes"
    radius_incoming_port: 1700
```