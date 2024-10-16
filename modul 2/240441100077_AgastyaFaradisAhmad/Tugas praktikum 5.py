nama = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))

if usia < 18:
    print("Maaf usia anda belum mencukupi.")
else:

    total_belanja = float(input("Masukkan total belanja: Rp"))
    kartu_member = input("Apakah pembeli memiliki kartu member? (ya/tidak): ")

    diskon = 0

    if kartu_member.lower() == "ya":
        diskon += 15 

    if total_belanja > 500000:
        diskon += 10  

    total_diskon = total_belanja * (diskon / 100)
    total_harga_setelah_diskon = total_belanja - total_diskon

    print(f"\nNama Pembeli: {nama}")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga sebelum diskon: Rp{total_belanja:.2f}")
    print(f"Total harga setelah diskon: Rp{total_harga_setelah_diskon:.2f}")
