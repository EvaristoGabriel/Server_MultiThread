import socket
import threading

def lidar_com_cliente(conexao, endereco):
    print(f"[NOVA CONEXÃO] {endereco} conectado.")
    try:
        while True:
            dados = conexao.recv(1024)
            if not dados:
                break
            mensagem = dados.decode('utf-8')
            print(f"[{endereco}] {mensagem}")
            conexao.sendall(f"{mensagem}".encode('utf-8'))
    except Exception as e:
        print(f"[ERRO] {endereco} - {e}")
    finally:
        conexao.close()
        print(f"[DESCONECTADO] {endereco}")

def iniciar_servidor(host='0.0.0.0', porta=12345):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()
    print(f"[INICIADO] Servidor escutando em {host}:{porta}")
    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=lidar_com_cliente, args=(conexao, endereco))
        thread.start()
        print(f"[ATIVAS] {threading.active_count() - 1} conexões")

if __name__ == "__main__":
    iniciar_servidor()
