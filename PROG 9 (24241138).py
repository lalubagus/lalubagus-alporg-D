# Suhu dalam Celcius
suhu_c = 38

# Konversi suhu menggunakan rumus
suhu_f = round((suhu_c * 1.8) + 32, 2)
suhu_k = round(suhu_c + 273.15, 2)
suhu_r = round(suhu_c * 0.8, 2)

# Menampilkan hasil konversi
print("Suhu dalam Fahrenheit:", suhu_f)
print("Suhu dalam Kelvin    :", suhu_k)
print("Suhu dalam Reamur    :", suhu_r)