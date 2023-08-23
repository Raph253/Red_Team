import socket
import concurrent.futures

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    sock.close()
    if result == 0:
        print(f"Porta {port} está aberta")

def main():
    target = input("Digite o endereço IP do servidor alvo: ")

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for port in range(1000, 5001):
            executor.submit(scan_port, target, port)

if __name__ == "__main__":
    main()
