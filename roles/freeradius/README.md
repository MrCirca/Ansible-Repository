Freeradius
=============

Freeradius deployment tasks for debian systems

Role Variables

Examples of variables used in this role:
```
ldap_server: ldap-server
ldap_server_port: 636
ldap_server_identity: "cn=admin,dc=example,dc=gr"
ldap_server_password: any_password_you_want
ldap_server_base_dn: "dc=example,dc=gr"
ldap_user_password_attribute: userPassword
ldap_people_group: "ou=People,dc=example,dc=gr"
ldap_branch_group: "cn=support,ou=Groups,dc=example,dc=gr"
ca_pub_path: /home/myCA.pem
```
For Radius Clients
```
freeradius_clients:
  - name: radius_client_name
    ip_address: 192.168.1.0/24
    secret: password
```
For Radius Users
```
freeradius_users:
  - name: mike
    password: test_password
    auth_type: Accept
```
