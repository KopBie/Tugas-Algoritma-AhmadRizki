total_hari = int(input("Masukkan jumlah hari: "))

tahun = total_hari // 365

sisa_hari_setelah_tahun = total_hari % 365
bulan = sisa_hari_setelah_tahun // 30
hari = sisa_hari_setelah_tahun % 30

print(f"Hasil konversi: {tahun} tahun, {bulan} bulan, {hari} hari")