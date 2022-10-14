import socket
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI


results = DNSDumpsterAPI().search('iiitd.edu.in')
dns = []

for i in results["dns_records"]["host"]:
    dns.append(i["domain"])


for d in dns:
    try:
        s = socket.getaddrinfo(d,0,0,0,0)
        print(f"{d}[{s[0][4][0]}]")
    except:
        pass
    
