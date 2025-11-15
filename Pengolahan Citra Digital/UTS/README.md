# Analisis

## Soal nomor 1

## Analisis Perbedaan Persebaran Nilai Keabuan pada Ketiga Jenis Citra

### a. Citra Asli

Citra asli merepresentasikan distribusi nilai keabuan sebagaimana
kondisi pencahayaan dan karakteristik objek pada saat citra diperoleh.
Histogram citra asli umumnya menunjukkan persebaran intensitas yang
tidak merata, yang dapat terfokus pada area gelap, area terang, atau
tersebar pada rentang intensitas tertentu.\
Secara konseptual, citra asli berfungsi sebagai representasi dasar
(baseline) untuk membandingkan perubahan persebaran intensitas setelah
diterapkan transformasi.

### b. Citra Negatif

Transformasi negatif merupakan operasi titik (point operation) yang
membalikkan nilai intensitas setiap piksel menurut persamaan:

\[ s = L - 1 - r \]

Transformasi ini menghasilkan distribusi histogram yang bersifat
simetris terhadap histogram citra asli. Distribusi intensitas tidak
berubah dalam hal jumlah piksel pada setiap level intensitas, namun
posisinya dibalik secara keseluruhan.

### c. Citra Logaritmik

Transformasi logaritmik memodifikasi intensitas piksel menggunakan
fungsi logaritma:

\[ s = c . log(1 + r) \]

Transformasi ini memperkuat nilai intensitas rendah dan mereduksi
pertumbuhan nilai intensitas tinggi. Histogram citra logaritmik umumnya
melebar pada rentang intensitas rendah dan memadat pada rentang
intensitas tinggi.

### Kesimpulan Perbandingan Persebaran Intensitas

  -----------------------------------------------------------------------
  Jenis Citra  Karakteristik Persebaran Intensitas
  ------------ ----------------------------------------------------------
  Citra Asli   Distribusi alami sesuai kondisi pengambilan citra

  Citra        Distribusi intensitas dibalik secara simetris terhadap
  Negatif      citra asli

  Citra        Intensitas rendah diperluas dan intensitas tinggi
  Logaritmik   dipadatkan
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Kondisi di Mana Transformasi Logaritmik Lebih Efektif

### a. Citra dengan Dominasi Intensitas Rendah

Transformasi logaritmik efektif untuk citra yang memiliki banyak area
gelap atau detail tersembunyi. Teknik ini mengamplifikasi informasi
visual sehingga struktur dan tekstur menjadi lebih terlihat.

### b. Situasi yang Memerlukan Peningkatan Kualitas Citra

Transformasi negatif hanya membalik intensitas dan tidak meningkatkan
kualitas citra. Sebaliknya, transformasi logaritmik bertujuan
meningkatkan visibilitas detail pada area gelap.

### c. Citra dengan Rentang Intensitas Tidak Seimbang

Transformasi logaritmik membantu menyeimbangkan dynamic range, terutama
ketika citra memiliki campuran area sangat gelap dan sangat terang.

------------------------------------------------------------------------

## Kesimpulan Umum

Transformasi logaritmik unggul untuk meningkatkan detail visual pada
intensitas rendah dan memberikan peningkatan kualitas citra secara
keseluruhan. Transformasi negatif lebih cocok untuk representasi
alternatif berbasis kontras terbalik. Pemilihan metode harus disesuaikan
dengan tujuan analisis citra.


## Soal Nomor 2

# Analisis Konvolusi Filter Spasial dan Hubungannya dengan Domain Frekuensi

Dokumen ini menganalisis hasil dari penerapan tiga kernel konvolusi yang berbeda—*Low Pass Filter* (LPF), *High Pass Filter* (HPF), dan *Band Pass Filter* (BPF) untuk penajaman—pada sebuah citra *grayscale*.

---

## Perbandingan Visual dan Nilai Piksel Rata-rata

Analisis ini membandingkan efek visual dan properti statistik (nilai piksel rata-rata) dari setiap citra hasil. Nilai piksel rata-rata (rata-rata dari semua nilai piksel dalam citra) adalah indikator yang baik untuk **kecerahan (brightness) global** dari sebuah citra.

### ### Citra Original
* **Visual:** Sebagai referensi. Memiliki keseimbangan antara area halus (frekuensi rendah) dan detail/tepi (frekuensi tinggi).
* **Piksel Rata-rata:** Menjadi nilai dasar (kita sebut saja $B_{\text{original}}$).

### ### Hasil 1: Low Pass Filter (LPF)
* **Kernel:** `(1/9) * [[1,1,1],[1,1,1],[1,1,1]]`
* **Analisis Visual:** Citra terlihat **kabur (blur)** atau **lebih halus (smoothed)**. Detail-detail tajam, tekstur, dan noise menjadi berkurang atau hilang. Ini terjadi karena setiap piksel baru dihitung sebagai rata-rata dari 9 piksel (termasuk dirinya sendiri) di sekitarnya. Perbedaan nilai yang drastis (tepi) menjadi "diratakan" dengan tetangganya.
* **Analisis Piksel Rata-rata:**
    * Jumlah dari semua elemen kernel LPF adalah $(1/9) \times 9 = 1$.
    * Kernel yang jumlahnya 1 (disebut juga *unity-gain filter*) memiliki properti **mempertahankan kecerahan global** (DC-preserving).
    * **Hasil:** Nilai piksel rata-rata $B_{\text{lpf}}$ akan **hampir identik** dengan $B_{\text{original}}$. Filter ini hanya mendistribusikan ulang intensitas secara lokal tanpa mengubah *brightness* keseluruhan.

### ### Hasil 2: High Pass Filter (HPF)
* **Kernel:** `[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]`
* **Analisis Visual:** Citra hasil akan terlihat **dominan gelap (mendekati hitam)**, dengan hanya **tepi-tepi (edges)** atau area dengan perubahan intensitas drastis yang muncul sebagai garis-garis terang. Area yang seragam (homogen) akan bernilai nol atau mendekati nol (hitam).
* **Analisis Piksel Rata-rata:**
    * Jumlah dari semua elemen kernel HPF adalah $(-1 \times 8) + 8 = 0$.
    * Kernel yang jumlahnya 0 **menghilangkan komponen DC** (komponen frekuensi nol, yang merepresentasikan kecerahan rata-rata).
    * **Hasil:** Nilai piksel rata-rata $B_{\text{hpf}}$ akan **mendekati nol**. Ini sesuai secara visual, di mana sebagian besar citra menjadi gelap karena *brightness* globalnya telah dihilangkan, dan hanya menyisakan informasi *perubahan* (tepi).

### ### Hasil 3: Band Pass Filter (BPF) / Penajaman
* **Kernel:** `[[0,-1,0],[-1,5,-1],[0,-1,0]]`
* **Analisis Visual:** Citra terlihat **lebih tajam (sharper)** dan **lebih jernih** dibandingkan citra aslinya. Tepi-tepi objek tampak lebih tegas dan kontras lokal meningkat.
* **Analisis Piksel Rata-rata:**
    * Jumlah dari semua elemen kernel BPF adalah $(-1 \times 4) + 5 = 1$.
    * Sama seperti LPF, kernel ini memiliki jumlah 1. Ini **mempertahankan kecerahan global**.
    * **Hasil:** Nilai piksel rata-rata $B_{\text{bpf}}$ akan **hampir identik** dengan $B_{\text{original}}$.
    * **Mengapa Menajamkan?** Kernel ini dapat didekomposisi menjadi:
        $ \begin{bmatrix} 0 & -1 & 0 \\ -1 & 5 & -1 \\ 0 & -1 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix} + \begin{bmatrix} 0 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 0 \end{bmatrix} $
        Ini berarti: **Hasil = Citra Original + (Hasil High Pass Filter)**.
        Secara intuitif, filter ini mengambil citra asli dan *menambahkan* detail tepi (yang didapat dari HPF) padanya, sehingga membuat tepi tersebut "menonjol" dan menghasilkan efek penajaman.

---

## Hubungan Domain Spasial dan Domain Frekuensi

**Domain Spasial** adalah ruang di mana kita melihat gambar (matriks piksel x, y). Operasi konvolusi dengan kernel adalah operasi di domain spasial.
**Domain Frekuensi** (diakses melalui Transformasi Fourier) merepresentasikan citra sebagai jumlahan dari gelombang-gelombang sinus dengan frekuensi berbeda.

* **Frekuensi Rendah:** Merepresentasikan area yang perubahannya lambat dan mulus (misalnya, warna kulit, langit). Ini adalah struktur utama dan *brightness* global.
* **Frekuensi Tinggi:** Merepresentasikan area yang perubahannya cepat (misalnya, tepi, garis, tekstur, noise). Ini adalah detail.

Setiap filter di domain spasial memiliki efek komplementer di domain frekuensi:

### ### Low Pass Filter (LPF)
* **Domain Spasial:** Melakukan **averaging (rata-rata)**. Operasi ini menghaluskan (smoothes) perubahan nilai piksel yang drastis.
* **Domain Frekuensi:** Karena "menghaluskan" berarti "menghilangkan detail tajam", filter ini secara efektif **meredam (attenuates) komponen frekuensi tinggi** (detail, noise) dan **meloloskan (passes) komponen frekuensi rendah** (area mulus). Inilah asal mula namanya: *Low Pass*.

### ### High Pass Filter (HPF)
* **Domain Spasial:** Melakukan **diferensiasi (pencarian perbedaan)**. Kernel Laplacian ini (varian dari `kernel_hpf`) menghitung perbedaan antara piksel pusat dan tetangganya. Jika tidak ada perbedaan (area datar), hasilnya nol. Jika perbedaannya besar (tepi), hasilnya bernilai tinggi.
* **Domain Frekuensi:** Karena hanya "merespons" pada perubahan cepat (tepi), filter ini secara efektif **meredam (attenuates) komponen frekuensi rendah** (area mulus, *brightness* global) dan **meloloskan (passes) komponen frekuensi tinggi** (detail, tepi).

### ### Band Pass Filter (BPF) / Penajaman
* **Domain Spasial:** Seperti dianalisis, ini adalah **Original + HPF**. Operasi ini mengambil citra asli dan "meningkatkan" (boosts) detail tepinya.
* **Domain Frekuensi:**
    * Citra Original = Meloloskan semua frekuensi (rendah dan tinggi).
    * HPF = Meloloskan *hanya* frekuensi tinggi.
    * **Hasil (Original + HPF):** Filter ini **meloloskan frekuensi rendah** (dari citra asli) dan **meningkatkan (boosts) frekuensi tinggi** (dari penjumlahan HPF). Efek *boosting* pada frekuensi tinggi inilah yang secara perseptual kita lihat sebagai penajaman (sharpening).