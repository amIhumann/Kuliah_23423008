import socket
import threading

HOST = "127.0.0.1"
PORT = 5050


def terima_pesan(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print("\nPesan masuk:", data.decode())
        except:
            break


# ---------------------------
# MAIN CLIENT
# ---------------------------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# thread penerima pesan
thread = threading.Thread(target=terima_pesan, args=(client,))
thread.daemon = True
thread.start()

print("Terhubung ke Chat Server.")
print("Ketik pesan lalu tekan ENTER.")

while True:
    pesan = input()
    if pesan.lower() == "exit":
        break
    client.sendall(pesan.encode())

client.close()
