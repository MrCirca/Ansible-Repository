Freeradius
=============

Freeradius deployment tasks for debian systems

Role Variables

Examples of variables used in this role:
```
ldap_server: ldap-server
ldap_server_port: 636
ldap_server_identitydd: "cn=admin,dc=example,dc=gr"(optional)
ldap_server_password: any_password_you_want (optional)
ldap_server_base_dn: "dc=example,dc=gr"
ldap_user_password_attribute: userPassword
ldap_people_group: "ou=People,dc=example,dc=gr"
ldap_branch_group: "ou=Groups,dc=example,dc=gr"
```
For Radius Clients
```
freeradius_clients:
  - name: radius_client_name
    ip_address: 192.168.1.0/24
    secret: password
    nastype: other
```
For Radius Users - Groups
```
ldap_groups:
  - ldap_group_name: "cn=employees,ou=Groups,dc=example,dc=gr"
    vlan_number: 2
  - ldap_group_name: "cn=support,ou=Groups,dc=example,dc=gr"
    vlan_number: 3
  - ldap_group_name: "cn=wireless,ou=Groups,dc=example,dc=gr"
    wireless_vlan_number: 21
```
