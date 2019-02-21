#!/usr/bin/env python
from pymodbus.constants import Defaults
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

Defaults.Timeout = 25
Defaults.Retries = 5
client = ModbusClient('ipaddress.of.venus', port='502')
client.write_register(806, 0)
