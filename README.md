# Notasi-Kalimat-Deskriptif-pada-algoritma-
Tugas Algoritma dan pemrograman 

# Algoritma Pencarian Linear: Mencari Nama dengan Santai

## Selamat datang!

Di sini kita bakal ngobrolin tentang algoritma pencarian linear. Kalian tahu kan, kadang kita butuh cari nama teman di daftar. Nah, algoritma ini adalah cara simpel buat nyari nama dalam daftar mahasiswa. Jadi, kita akan membandingkan setiap nama satu per satu. Kalau ketemu, kita bakal senang! Tapi kalau enggak, ya sudah, kita bisa move on.

## Langkah-langkah Pencarian

1. **Persiapan**: Kita mulai dengan ngatur sebuah variabel yang kita sebut `ditemukan`. Awalnya kita anggap, "Eh, nama ini belum ketemu!"
2. **Mulai Cek**: Kita bakal cek satu per satu nama di daftar. 
   - Jika kita menemukan nama yang dicari, kita bilang, "Yeay! Ketemu!" dan langsung berhenti cek.
3. **Cek Hasil**:
   - Kalau `ditemukan` jadi `True`, kita kasih tahu, "Nama ini ada di daftar, lho!"
   - Tapi, kalau sampai akhir nama di daftar dan tetap enggak ketemu, kita bilang, "Maaf, nama ini nggak ada."

## Kode yang Bisa Dipakai

```python
# Algoritma Pencarian Linear: Nyari Nama Mahasiswa dengan Santai

def cari_mahasiswa(daftar_mahasiswa, nama):
    """
    Fungsi ini buat nyari nama mahasiswa di daftar.

    Argumen:
    daftar_mahasiswa -- Daftar nama mahasiswa
    nama -- Nama yang mau dicari

    Kembalikan:
    Pesan apakah mahasiswa ditemukan atau tidak.
    """
    # Set variabel ditemukan jadi False
    ditemukan = False

    # Proses pencarian nama mahasiswa
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa == nama:
            ditemukan = True
            break  # Berhenti cek jika nama ketemu
    
    # Kembalikan hasil pencarian
    if ditemukan:
        return f"Mahasiswa {nama} ditemukan dalam daftar."
    else:
        return f"Mahasiswa {nama} tidak ditemukan dalam daftar."

# Contoh penggunaan
if __name__ == "__main__":
    # Daftar nama mahasiswa acak
    daftar_mahasiswa = ["Siti", "Rahmat", "Dian", "Fajar", "Tika", "Doni", "Bintang", "Salsa", "Rian", "Anita"]
    
    # Nama yang mau dicari
    nama_target = "Doni"  # Bisa ganti dengan nama lain sesuai keinginan

    hasil = cari_mahasiswa(daftar_mahasiswa, nama_target)
    print(hasil)
