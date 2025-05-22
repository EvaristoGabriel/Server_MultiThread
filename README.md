Grupo:

- Gabriel Evaristo Carlos - 201965034B
- Iago Mazzoni Santos - 202065568C


# Estrutura do Código do Servidor (server_a)
- Função lidar_com_cliente(conexao, endereco):

    - Responsabilidade: Gerenciar a comunicação com um cliente específico.

    - Fluxo:

        Recebe dados do cliente e envia um eco da mensagem de volta.

        Se a conexão for encerrada pelo cliente (if not dados), o loop é interrompido.

        Em caso de erro, fecha a conexão e registra o evento.

- Função iniciar_servidor(host, porta)

    - Responsabilidade: Configurar o servidor e aceitar conexões de clientes.

    - Passos:

        Cria um socket TCP (SOCK_STREAM) e associa ao endereço e porta especificados.

        Entra em modo de escuta (servidor.listen()).

        Aceita conexões em loop infinito.

        Para cada cliente, cria uma nova thread (threading.Thread) e a inicia.

        Exibe o número de threads ativas (subtraindo a thread principal).

- Threads Dinâmicas

    - Cada cliente é atendido por uma thread dedicada.

    - Ao finalizar a comunicação, a thread é automaticamente encerrada (thread.start() finaliza após a função lidar_com_cliente terminar).


# Estrutura do Código do Servidor (server_b)
- Variáveis Globais

    - MAX_CLIENTES: Define o número máximo de threads/clientes simultâneos (10).

    - clientes_ativos: Contador de clientes conectados.

    - lock: Garante sincronização no acesso ao contador clientes_ativos (evita condições de corrida).

- Função lidar_com_cliente(conexao, endereco)

    - Similar ao server_a, mas decrementa clientes_ativos ao finalizar (usando lock para sincronização).

- Função iniciar_servidor(host, porta)

    - odificações:

    - Define um backlog de 5 conexões pendentes (servidor.listen(5)).

    - Antes de criar uma thread, verifica se há slots disponíveis (clientes_ativos < MAX_CLIENTES).

    - Se o limite for atingido:

        Fecha a conexão do cliente.

        Exibe uma mensagem de servidor cheio.

- Pool de Threads Fixo

    - As 10 threads são criadas sob demanda (não previamente alocadas).

    - O contador clientes_ativos garante que nunca exceda o limite definido.
