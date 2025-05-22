import socket

def main():
    HOST = '127.0.0.1'
    PORT = 12345

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("[*] Conectado ao servidor")
            while True:
                msg = input("Mensagem (ou 'sair'): ")
                if msg.lower() == "sair":
                    break
                s.sendall(msg.encode())
                data = s.recv(1024)
                if not data:
                    print("[ERRO] Conexão encerrada pelo servidor")
                    break
                print("Eco:", data.decode())
    except ConnectionRefusedError:
        print("[ERRO] Servidor cheio ou não disponível.")
    except Exception as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()