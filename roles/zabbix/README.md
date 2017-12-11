Zabbix agent
============

Role Variables
--------------

Examples of variables used in this role:
```
---
zabbix_servers:
  - url: 172.17.172.47
    username: zabbix
    password: password
    hostname: "{{ ansible_hostname }}"
    visible_hostname:
    groups:
      - Linux Servers
    templates:
      - Template OS Linux
    interface:
      - type: 1           # 1 = zabbix_agent, 2 = SNMP, 3 = IPMI, 4 = JMX
        main: 1           # default
        useip: 1
        ip: "{{ hostvars[ansible_hostname]['ansible_default_ipv4']['address']}}"
#       dns:
        port: 10050
```
