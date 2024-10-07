# Algoritma Pencarian Linear

## Deskripsi

Jadi, algoritma ini digunakan buat mencari nama teman di dalam daftar. Misalnya, kita mau tahu apakah teman kita yang bernama "Doni" ada di dalam daftar mahasiswa. Kita bakal lihat satu-satu namanya, dan kalau ketemu, kita bilang "Oh, ini dia!" Tapi kalau sudah lihat semua nama dan ternyata tidak ada, kita bilang "Eh, tidak ada di sini."

## Langkah-langkah Algoritma

1. **Mulai**: Siapkan sebuah variabel yang kita sebut `ditemukan`, awalnya kita bilang `False`, artinya kita belum menemukan apa-apa.
2. **Cek satu-satu**: Lihat satu per satu nama di daftar mahasiswa.
   - Jika nama yang kita cari sama dengan nama yang ada, ubah `ditemukan` jadi `True` dan berhenti cari.
3. **Cek hasilnya**:
   - Kalau `ditemukan` jadi `True`, kita bilang "Mahasiswa [nama] ada di daftar!"
   - Kalau masih `False`, berarti kita belum menemukan namanya, jadi kita bilang "Mahasiswa [nama] tidak ada di daftar."

## Contoh Kode

# Algoritma Pencarian Linear: Mencari Nama Mahasiswa dalam Daftar Acak

def cari_mahasiswa(daftar_mahasiswa, nama):
    """
    Fungsi untuk mencari mahasiswa dalam daftar kelas.

    Argumen:
    daftar_mahasiswa -- List yang berisi nama-nama mahasiswa
    nama -- Nama mahasiswa yang ingin dicari

    Mengembalikan:
    String hasil apakah mahasiswa ditemukan atau tidak.
    """
    # Mulai dengan bilang belum ketemu
    ditemukan = False

    # Proses pencarian nama mahasiswa dalam daftar_mahasiswa
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa == nama:
            ditemukan = True
            break  # Hentikan pencarian kalau sudah ketemu
    
    # Mengembalikan hasil pencarian
    if ditemukan:
        return f"Mahasiswa {nama} ditemukan dalam daftar."
    else:
        return f"Mahasiswa {nama} tidak ditemukan dalam daftar."

# Contoh penggunaan

    # Daftar nama mahasiswa acak
    daftar_mahasiswa = ["Siti", "Rahmat", "Dian", "Fajar", "Tika", "Doni", "Bintang", "Salsa", "Rian", "Anita"]
    
    # Nama yang akan dicari
    nama_target = "Doni"  # Nama ini bisa diganti sama nama lain

    hasil = cari_mahasiswa(daftar_mahasiswa, nama_target)
    print(hasil)
