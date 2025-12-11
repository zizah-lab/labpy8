print("=== KALKULATOR AMAN ===")

try:
    # Input angka
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    # Input operator
    operator = input("Masukkan operator (+, -, *, /): ")

    # Proses perhitungan
    if operator == "+":
        hasil = angka1 + angka2

    elif operator == "-":
        hasil = angka1 - angka2

    elif operator == "*":
        hasil = angka1 * angka2

    elif operator == "/":
        try:
            hasil = angka1 / angka2
        except ZeroDivisionError:
            print("Error: Tidak bisa membagi dengan nol.")
            exit()

    else:
        # Jika operator tidak valid → raise error
        raise Exception("Operator tidak valid! Gunakan +, -, *, atau /.")

    # Cetak hasil
    print(f"Hasil: {angka1} {operator} {hasil}")

except ValueError:
    print("Error: Input harus berupa angka!")

except Exception as e:
    print("Error:", e)
