#!/usr/bin/env python
from pymodbus.constants import Defaults
from pymodbus.constants import Endian
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder

Defaults.Timeout = 25
Defaults.Retries = 5
client = ModbusClient('ipaddress.of.venus', port='502')
result = client.read_input_registers(806, 2)
# If you get this error: "unexpected keyword argument 'endian'" try replacing
# `endian=Endian.Big`
#with
# `byteorder=Endian.Big`
# on this line:
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
relay1=decoder.decode_16bit_uint()
relay2=decoder.decode_16bit_uint()
print("Relay1: %d, Relay2: %d" % (relay1, relay2))
