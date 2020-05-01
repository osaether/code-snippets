#!/usr/bin/python -u

from functools import partial
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gobject
import urllib2

ip_address = "192.168.1.9"

def track(conn, value):
    if value["Value"] < 24.5:
       response = urllib2.urlopen('http://%s/cm?cmnd=Power2%%20ON' % ip_address)

def main():
    DBusGMainLoop(set_as_default=True)
    conn = dbus.SystemBus()

    conn.add_signal_receiver(partial(track, conn),
            dbus_interface='com.victronenergy.BusItem',
            signal_name='PropertiesChanged',
            path="/Dc/Battery/Voltage",
            bus_name="com.victronenergy.system")

    gobject.MainLoop().run()

if __name__ == "__main__":
    main()