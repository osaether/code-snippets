ControlByWeb temperature reading python script
==============================================

This python script reads the temperature data from a Xytronix ControlByWeb (CBW) device.
The script is tested on a CBW X-300 but will most likely work on other CBW units as well.

Usage
=====

To use the script you must edit the host name on line 5:

`conn = httplib.HTTPConnection("yourcbw.dyndns.org:8000")`

If a control password is enabled on your CBW unit, you need to encode it in Base64.
ControlByWeb has a utility for this:
<https://www.controlbyweb.com/encoder/>

Type in your password and press the encode button and replace "bm9uZTpMb2w=" with your
encoded password on this line:

`conn.request("GET", "/state.xml HTTP/1.1\r\nAuthorization: Basic bm9uZTpMb2w=\r\n", "", headers)`

To run the script type

`python cbwtemp1.py`