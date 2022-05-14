![Alt text](/docs/logo/full_logo.png?raw=true)

---
A library for mass execution of ssh commands on remote machines fleet. 

## Hosts file format

You need to specify hosts and their groups. Groups so far can store only simple SSH configurations (username, password and port). Each host can override these values by specifying certain fields.

```yaml
hosts:
- ip: 192.168.0.2
  groups: 
  - office
- ip: 192.168.0.3
  ssh:
    username: user  # overrides group value
  groups:
  - office

groups:
  office:
    ssh:
      username: root
      password: toor
      port: 22

```

## Strategy file format

Strategy is a set of orders to execute via SSH. The format is pretty simple:

```yaml
- name: List all directories
  command: ls

- name: Current path
  command: pwd
```

## Running strategy

TODO: Instruction here after finishing CLI