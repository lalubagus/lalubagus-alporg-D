# Program Pengecekan Rentang Angka
print("<===== RENTANG ANGKA =====>")
nim = "24241138"
nim_awal =   24
nim_akhir =  38

print(f"Masukkan angka antara {nim_awal} dan {nim_akhir}: ", end="")
angka = int(input("Angka: "))

if nim_awal <= angka <= nim_akhir:
    print("Angka berada dalam rentang!")
else:
    print("Angka di luar rentang!")

# Operasi logika berdasarkan angka yang dimasukkan
print("\nOperasi logika:")
print(f"Jika {angka} di OR-kan dengan True maka: {angka | True}")
print(f"Jika {angka} di OR-kan dengan False maka: {angka | False}")
print(f"Jika {angka} di AND-kan dengan True maka: {angka & True}")
print(f"Jika {angka} di AND-kan dengan False maka: {angka & False}")
print(f"Jika {angka} di XOR-kan dengan True maka: {angka ^ True}")
print(f"Jika {angka} di XOR-kan dengan False maka: {angka ^ False}")