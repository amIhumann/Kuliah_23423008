import socket

HOST = "127.0.0.1"   # IP server
PORT = 5050

# Buat socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hubungkan ke server
client_socket.connect((HOST, PORT))

# Kirim pesan
pesan = "Tes Koneksi"
client_socket.sendall(pesan.encode())

# Terima echo dari server
data = client_socket.recv(1024)
print("[CLIENT] Balasan dari server:", data.decode())

client_socket.close()
