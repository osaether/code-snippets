#!/usr/bin/python -u

from functools import partial
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gobject

ontemp = 45
offtemp = 35

def track(conn, value):
    currval = int(conn.get_object("com.victronenergy.system",
            "/Relay/1/State").GetValue())
    temp = int(value["Value"]) 
    if (temp >= ontemp) and (currval == 0):
	conn.get_object("com.victronenergy.system",
            "/Relay/1/State").SetValue(1)
    if (temp <= offtemp) and (currval == 1):
        conn.get_object("com.victronenergy.system",
            "/Relay/1/State").SetValue(0)

def main():
    DBusGMainLoop(set_as_default=True)
    conn = dbus.SystemBus()

    conn.add_signal_receiver(partial(track, conn),
            dbus_interface='com.victronenergy.BusItem',
            signal_name='PropertiesChanged',
            path="/Temperature",
            bus_name="com.victronenergy.temperature.builtin_adc5")

    gobject.MainLoop().run()


if __name__ == "__main__":
    main()