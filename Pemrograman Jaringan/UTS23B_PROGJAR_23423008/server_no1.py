import socket

HOST = "0.0.0.0"   # listen ke semua interface
PORT = 5050

# Buat socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke host dan port
server_socket.bind((HOST, PORT))

# Listen koneksi
server_socket.listen(1)
print(f"[SERVER] Menunggu koneksi di port {PORT} ...")

# Terima koneksi dari client
conn, addr = server_socket.accept()
print(f"[SERVER] Terhubung dengan {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break  # jika client tutup koneksi

    pesan = data.decode()
    print(f"[SERVER] Pesan diterima: {pesan}")

    # kirim balik (echo)
    conn.sendall(data)

conn.close()
server_socket.close()
