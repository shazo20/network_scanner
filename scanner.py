import socket
import ipaddress
from colorama import Fore 
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

def scanner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        result = s.connect_ex((str(ip), port))
        if result == 0:
            print(Fore.GREEN + f"Ip: {ip} is available on port: {port}" + Fore.RESET)
            with lock:
                available_ips.append(ip)
        else: 
            print(Fore.YELLOW + f"Ip: {ip} is not available on port: {port}" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Fore.RESET)
    finally:
        s.close()

lock = Lock()
available_ips = []

try:
    ip = input("Please enter ip and subnet in this format (192.168.1.0/24): ")
    port = int(input("Please enter port: "))
    network = ipaddress.ip_network(ip,strict=False)
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda ip: scanner(ip, port), network.hosts())
    
    print(f"\nAvailable ips: {available_ips}")
except Exception as e:
    print(Fore.RED + f"Error: {e}" + Fore.RESET)