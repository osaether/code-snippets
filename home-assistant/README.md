# readtemps.py

This script is used to read the nvme, hdd, cpu and nic temperatures of a linux machine and post them to a Home Assistant (HA) server. I have uploaded it here in case somebody might find it useful.

The script is meant to be executed on a Linux machine. To use it on your machine you need to change a few things.

* Change ha_ipaddress, ha_port and ha_access_token at the top of the script so it matches your HA installation. The access token can be generated at the bottom of your user profile in
  HA (click your username at the bottom of the left side bar).

* Replace the device names inside the http_post calls.

* Change the sensor name at the end of the first line of the http_post function. The default is proxmox.<device_name>_temp.

NOTE: If you get an error that "sensors" is not found you need to install lm-sensors:

```
sudo apt update
sudo apt install lm-sensors
```
