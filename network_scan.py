import nmap

scanner = nmap.PortScanner()
scanner.scan('192.168.1.165', arguments='-p 22,80,443,3389 --open')

for host in scanner.all_hosts():
    print(f"Hôte : {host}")
    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()
        print(f"  Ports ouverts ({proto}) : {list(ports)}")
