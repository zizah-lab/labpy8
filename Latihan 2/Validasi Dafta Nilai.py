print("=== VALIDASI DAFTAR NILAI ===")

nilai = [80, 90, 'A', 70, 100, 'B']
total = 0
jumlah_valid = 0

for item in nilai:
    try:
        angka = float(item)   # mencoba mengubah ke angka
        total += angka
        jumlah_valid += 1
    except ValueError:
        print(f"Data '{item}' dilewati (bukan angka).")

if jumlah_valid > 0:
    rata_rata = total / jumlah_valid
    print(f"\nRata-rata nilai valid: {rata_rata}")
else:
    print("Tidak ada data nilai yang valid.")
