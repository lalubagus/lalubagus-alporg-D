# Data Mahasiswa
nama = "Lalu Bagus Adi Kusuma Wijaya"
nim = "24241138"
asal = "Lombok Timur"  

# 2 digit pertama dan 2 digit Nim terakhir
nim_awal = int(nim[:2])
nim_akhir = int(nim[-2:])
nomor_keberuntungan = nim_awal + nim_akhir

# Output
print(f"Nama saya adalah {nama}")
print(f"NIM saya adalah {nim}")
print(f"Saya berasal dari {asal}")
print(f"Nomor keberuntungan saya adalah: {nim_awal} + {nim_akhir} = {nomor_keberuntungan}")