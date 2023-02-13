import httplib, urllib
import xml.etree.ElementTree as et

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = httplib.HTTPConnection("yourcbw.dyndns.org:8000")
conn.request("GET", "/state.xml HTTP/1.1\r\nAuthorization: Basic bm9uZTpMb2xMb2w=\r\n", "", headers)
response = conn.getresponse()
resp = et.parse(response)
root = resp.getroot()
temp1 = root.find("sensor1temp")
temp2 = root.find("sensor2temp")
conn.close()
print "sensor1temp=", temp1.text
print "sensor2temp=", temp2.text