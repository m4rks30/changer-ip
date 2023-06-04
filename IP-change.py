import time
import subprocess

ips = ['ip-list'] #ip-list
while True:
    for ip in ips:
        subprocess.call(['netsh', 'interface', 'ipv4', 'set', 'address', 'Ethernet', 'static', ip, '255.255.255.0', '192.168.2.254', '1'])
        time.sleep(2) 
