# prxtemps.py

This script is used to read the nvme, sdd, CPU and NIC temperatures of my Proxmox machine and post them to my Home Assistant (HA) server. I haved uploaded it here in case sdomebody might find use for it.

The script is ment to be executed on a Linux machine. To use it on your machine you need to change a few things.

* Replace the IP-address, port number and access token at the top of the script so it matches your HA installation. The access token can be generated at the bottom of your user profile in
  HA (click your username at the bottom of the left side bar)

* Replace the device names inside the http_post calls.

* Change the sensor name at the end of the first line of the http_post function. The default is proxmox.<device_name>_temp.

NOTE: If you get an error that "sensors" is not found you need to install lm-sensors:

sudo apt update
sudo apt install lm-sensors