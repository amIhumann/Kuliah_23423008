import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5050))
server.listen(1)

print("Server menunggu koneksi...")

client, addr = server.accept()
print("Client terhubung:", addr)

# Server hanya menerima tapi TIDAK mengirim balasan
while True:
    data = client.recv(1024)
    if not data:
        break
    print("Server menerima:", data.decode())
