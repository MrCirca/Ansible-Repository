Mikrotik Radius Client
======================

RouterOS deployment tasks for Mikrotik Routers.

Role Variables

Examples of variables used in this role for Mikrotik Radius Clients:
```
mikrotik_radius_clients:
  - radius_server_address: 192.168.1.1
    radius_server_shared_secret: test_password
    radius_incoming: "yes"
    radius_incoming_port: 1700
```

Examples of variables used in this role for Mikrotik users:
```
mikrotik_users:
  - mikrotik_user: test_user
    mikrotik_user_password: test_pass
    mikrotik_user_group: full          
```

