import socket
import threading

MAX_CLIENTES = 10
clientes_ativos = 0
lock = threading.Lock()

def lidar_com_cliente(conexao, endereco):
    global clientes_ativos
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
        with lock:
            clientes_ativos -= 1
        conexao.close()
        print(f"[DESCONECTADO] {endereco}")

def iniciar_servidor(host='0.0.0.0', porta=12345):
    global clientes_ativos
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(5)  # Backlog de 5 conexões pendentes
    print(f"[INICIADO] Servidor escutando em {host}:{porta}")
    while True:
        conexao, endereco = servidor.accept()
        with lock:
            if clientes_ativos >= MAX_CLIENTES:
                print(f"[SERVIDOR CHEIO] Recusando conexão de {endereco}")
                conexao.close()
                continue
            clientes_ativos += 1
        thread = threading.Thread(target=lidar_com_cliente, args=(conexao, endereco))
        thread.start()
        print(f"[ATIVAS] Conexões ativas: {clientes_ativos}")

if __name__ == "__main__":
    iniciar_servidor()