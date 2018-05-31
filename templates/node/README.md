## template: github.com/grimpy/0-debug/node/0.0.1

### Description:
So you got yourself a production mode Zero-OS which you want to debug withouth rebooting?
Just add this repo and enable ports and run commands on the node

### Actions
- `system`: Execute system command
- `bash`: Execute bash script
- `open_port`: Opens port in the firewall
- `add_github_user`: Adds the github public ssh key to the root user

#### How to use:

```python
api = j.clients.zrobot.robots['main']
# add this repo
api.templates.add_repo('http://github.com/grimpy/0-debug')
# create debug node service
serv = api.services.create('github.com/grimpy/0-debug/node/0.0.1', 'debugme')
# open ssh port
serv.schedule_action('open_port', args={'port': 22}).wait()
# add ssh key
serv.schedule_action('add_github_user', args={'user': 'grimpy'}).wait()
# get ip info
print(serv.schedule_action('system', args={'command': 'ip a s dev eth0'}).wait(die=True).result['stdout'])

#2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq state UP group default qlen 1000
#    link/ether 54:4f:60:e6:2f:01 brd ff:ff:ff:ff:ff:ff
#    inet 192.168.58.50/25 scope global eth0
#       valid_lft forever preferred_lft forever
```
