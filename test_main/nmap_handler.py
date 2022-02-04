import nmap
from tkinter import messagebox as MessageBox


def scan_ip_port(ip, port):
    '''
    nmapScan = n.Nmap()
    result = nmapScan.scan_top_ports(ip)
    print("RESULT: ---------> ")
    print(result)
    return "Yes!"
    '''
#scan_ip_port("85.85.22.19", "123")

    nmScan = nmap.PortScanner()

    # scan localhost for ports in range 21-443
    nmScan.scan(ip, port)
    print ('KK: ' + ip + '-' + port)
    # run a loop to print all the found result about the ports
    for host in nmScan.all_hosts():
        print ('KK host:')
        print(host)
        for proto in nmScan[host].all_protocols():
            lport = nmScan[host][proto].keys()
            #lport.sort()
            print ('KK lport')
            print(lport)
            for port in lport:
                print ('Host: ' + host + '  Port: ' + str(port) + ' State: ' + nmScan[host][proto][port]['state'])
                #MessageBox.showinfo("Resultado nmap", 'Host: ' + host + '  Port: ' + str(port) + ' State: ' + nmScan[host][proto][port]['state'])
                return nmScan[host][proto][port]['state']
    return ""