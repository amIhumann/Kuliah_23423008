Analisa :

Soal nomor 1

✅ Perbedaan Persebaran Nilai Keabuan antara Ketiga Citra
a. Citra Asli

Persebaran nilai keabuan bergantung pada kondisi gambar awal.

Biasanya distribusinya tidak merata—bisa terkumpul di area gelap, cerah, atau campuran.

Histogram asli menunjukkan bagaimana intensitas piksel tersebar secara alami tanpa modifikasi.

Intinya: citra asli adalah baseline yang menunjukkan kondisi awal intensitas.

b. Citra Negatif

Transformasi negatif membalikkan intensitas:

Piksel gelap → terang

Piksel terang → gelap

Hasilnya, bentuk histogram terbalik/mirror terhadap histogram asli.

Puncak histogram bergeser:

Jika citra asli dominan gelap, histogram negatif jadi dominan terang.

Jika citra asli dominan terang, histogram negatif jadi dominan gelap.

Makna: persebaran intensitas tidak berubah secara jumlah, tetapi posisinya dibalik.

c. Citra Logaritmik

Fungsi logaritmik memperkuat intensitas rendah dan menekan intensitas tinggi.

Histogram gambar log biasanya:

Melebar pada area intensitas rendah (detail gelap menjadi lebih terlihat)

Lebih rapat pada area intensitas tinggi (highlight menjadi lebih lembut)

Distribusinya cenderung miring ke kanan (lebih banyak nilai sedang-terang akibat peningkatan piksel gelap).

Makna: log memperluas detail pada bagian gelap tanpa membuat piksel terang berlebihan.

📌Kesimpulan
Jenis Citra	Karakter Persebaran
Asli	Distribusi natural sesuai kondisi pencahayaan
Negatif	Distribusi dibalik secara simetris (mirror) dari citra asli
Logaritmik	Nilai gelap diperluas, nilai terang dipadatkan—lebih banyak detail di area gelap

✅ Kapan Transformasi Logaritmik Lebih Bermanfaat Dibanding Negatif?

Transformasi logaritmik lebih bermanfaat daripada negatif ketika:

a. Gambar Banyak Mengandung Area Gelap

Jika banyak detail kecil tersembunyi dalam bayangan/gelap, fungsi log membantu:

Mengangkat detail pada intensitas rendah

Membuat area gelap lebih jelas tanpa merusak bagian terang

Contoh:

Foto ruangan gelap

Foto rontgen/medis

Citra astronomi (bulan, bintang)

Citra mikroskop

b. Ketika ingin enhancement, bukan pembalikan

Negatif hanya membalik warna—baik untuk:

Analisis citra medis (kontras tertentu)

Kesan visual tertentu

Mendeteksi bentuk dengan kontras berlawanan

Tetapi negatif tidak meningkatkan detail.

Sebaliknya, transformasi log memperbaiki kualitas pada area gelap.

c. Saat intensitas piksel sangat tidak seimbang

Misalnya gambar yang:

Terlalu gelap tetapi memiliki highlight sangat terang,

Perbedaan intensitas terlalu ekstrem.

Logaritmik menyeimbangkan perbedaan itu.

📌 Kesimpulan

Transformasi logaritmik lebih bermanfaat untuk meningkatkan detail dan kontras pada area gelap, sedangkan transformasi negatif lebih cocok jika membutuhkan pembalikan warna atau menonjolkan objek dengan kontras kebalikan dari citra asli.