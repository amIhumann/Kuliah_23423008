import socket

# Buka Host yang pertama jika ingin mengetes koneksi timeout saat connect
# HOST = "10.255.255.1"

# Host kedua untuk mengetes koneksi timeout saat menerima pesan
HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -----------------------------
# 1. Timeout 3 detik saat connect
# -----------------------------
client.settimeout(3)

try:
    print("Menghubungkan ke server...")
    client.connect((HOST, PORT))
    print("Berhasil terhubung!")

except socket.timeout:
    print("Koneksi timeout! (saat connect)")
    client.close()
    exit()

# -----------------------------
# 2. Timeout 2 detik saat membaca data
# -----------------------------
client.settimeout(2)

try:
    # kirim pesan
    client.sendall("Tes timeout".encode())

    # baca balasan (2 detik)
    data = client.recv(1024)
    print("Balasan:", data.decode())

except socket.timeout:
    print("Koneksi timeout! (saat membaca data)")
finally:
    client.close()
