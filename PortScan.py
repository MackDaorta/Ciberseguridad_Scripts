import socket
from concurrent.futures import ThreadPoolExecutor 
def scan_target(ip,port):
    try: 
        sock = socket.socket()
        sock.settimeout(1)
        result= sock.connect_ex((ip,port))
        if result == 0:
            sock.send(b"HEAD / HTTP/1.1\r\nHost: {ip}\r\n\r\n")
            banner = sock.recv(1024).decode(errors='ignore')
            print(f"Puero {port} esta abierto en {ip}")
            if banner:
                print(f"Info: {banner[:50]}...")

        sock.close()    
        
    except:
        pass 
    finally:
        sock.close()

print('Ingrese la dirección IP a escanear: ')
ip_router = input()

puertos=range(1,8001)
print(f"Escaneando {ip_router} en los puertos {puertos[0]}-{puertos[-1]}")

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(lambda p: scan_target(ip_router,p), puertos)

print ("Escaneo completado")