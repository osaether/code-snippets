#! /usr/bin/env python3

import re
import subprocess
import json
from requests import post

ha_ipaddress = "192.168.0.4"
ha_port = "8123"
ha_access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ8.eyJpc3MiOiI3OThiYjFhZTExZDA0MzdlODM2ODNlNDQ3ODNlYWE5NiIsImlhdCI6MTY0MDIxMTcy1CwiZXhwIjoxOTU1NTcxNzI4fQ.T8-5XIpbei6UO262NkJnaUj3I_f_Tda4pkSjDqIVPCc"

def nvme_temp(dev):
    res = subprocess.getoutput(f'/usr/sbin/smartctl -A {dev:s}')
    match = re.search("Temperature:[\t ]+([0-9]+)", res)
    return int(match.group(1))

def hdd_temp(dev):
    res = subprocess.getoutput(f'/usr/sbin/smartctl -A {dev:s}')
    match = re.search("Temperature_Celsius.+Always[ \t]*-[ \t]*([0-9]+)", res)
    return int(match.group(1))

headers = {
  "Authorization": f"Bearer {ha_access_token:s}",
  "content-type": "application/json"
}

def http_post(k, v):
    url = f"http://{ha_ipaddress:s}:{ha_port:s}/api/states/proxmox.{k:s}_temp"
    data = '{"state": %d}' % v
    response = post(url, headers=headers, data=data, verify=False)

http_post("nvme0", nvme_temp("/dev/nvme0"))
http_post("nvme1", nvme_temp("/dev/nvme1"))
http_post("sda", hdd_temp("/dev/sda"))
http_post("sdb", hdd_temp("/dev/sdb"))
http_post("sdc", hdd_temp("/dev/sdc"))
http_post("sdd", hdd_temp("/dev/sdd"))

result = subprocess.getoutput("/usr/bin/sensors")
match = re.search("Package id 0:[\t ]+\+([0-9]+\.[0-9]+)", result)
http_post("cpu", int(float(match.group(1))))

match = re.search("PHY Temperature:[\t ]+\+([0-9]+\.[0-9]+)", result)
http_post("nic", int(float(match.group(1))))

