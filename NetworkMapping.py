from scapy.all import ARP, Ether, srp
import requests

def get_vendor(mac):
    try:
        url=f"https://api.macvendors.com/{mac}"
        response=requests.get(url,timeout=10)
        if response.status_code==200:
            return response.text
        return "Desconocido"
    except:
        return "Error en la consulta"


def scan_network(ip_range):
    print(f"Escaneando la red {ip_range}...")

    arp=ARP(pdst=ip_range)

    ether=Ether(dst="ff:ff:ff:ff:ff:ff")

    packet=ether/arp

    result=srp(packet, timeout=2, verbose=0)[0]

    clients=[]

    for sent,recived in result:

        clients.append({'ip': recived.psrc, 'mac': recived.hwsrc})
    return clients

red=input("Ingrese el rango de IP a escanear (ejemplo: 192.168.1.0/24): ")
dispositivos=scan_network(red)
print("\nDispositivos encontrados:")
print("-"*40)
print("IP\t\t\tMAC Address\t\t Fabricante")
print("-"*40)

for dev in dispositivos:
    vendor=get_vendor(dev['mac'])
    print(f"{dev['ip']}\t{dev['mac']}\t{vendor}")