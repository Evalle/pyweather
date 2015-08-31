import lizepy

ip = lizepy.get_ip()

geoip = lizepy.get_geoip(str(ip)) 

print geoip
