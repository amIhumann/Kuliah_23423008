import socket
import threading

HOST = "0.0.0.0"
PORT = 5050

# daftar client yang sedang terhubung
clients = []

def broadcast(pesan, sender_socket):
    """Kirim pesan ke semua client kecuali pengirim"""
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(pesan)
            except:
                clients.remove(client)

def handle_client(client_socket, addr):
    print(f"[SERVER] Client terhubung: {addr}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            pesan = data.decode()
            print(f"[SERVER] Dari {addr}: {pesan}")

            # broadcast ke semua client lain
            broadcast(data, client_socket)

        except ConnectionResetError:
            break

    print(f"[SERVER] Client terputus: {addr}")
    clients.remove(client_socket)
    client_socket.close()


# ---------------------------
# MAIN SERVER
# ---------------------------
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"[SERVER] Menunggu koneksi di port {PORT} ...")

while True:
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)

    # buat thread baru untuk client
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()

    print(f"[SERVER] Total client: {len(clients)}")
