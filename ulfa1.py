print("===== APOTEK BUNDA =====")
print("DAFTAR 10 JENIS OBAT")

obat = {
    1: ("Paracetamol", 5000, 20),
    2: ("Vitamin C", 8000, 15),
    3: ("Promag", 9000, 10),
    4: ("Antasida", 6000, 8),
    5: ("Ibuprofen", 10000, 12),
    6: ("OBH", 15000, 5),
    7: ("Amoxicillin", 12000, 18),
    8: ("Betadine", 18000, 0),
    9: ("Oralit", 3000, 25),
    10: ("CTM", 4000, 7)
}

for nomor, data in obat.items():
    print(nomor, ".", data[0])

pilihan = int(input("\nPilih nomor obat: "))

if pilihan >= 1 and pilihan <= 10:
    nama, harga, stok = obat[pilihan]

    print("\nNama obat:", nama)
    print("Harga: Rp", harga)
    print("Stok:", stok)

    jumlah = int(input("Masukkan jumlah pembelian: "))

    if stok == 0:
        print("Maaf, obat sedang habis.")
    elif jumlah <= 0:
        print("Jumlah pembelian tidak valid.")
    elif jumlah > stok:
        print("Stok obat tidak mencukupi.")
    else:
        total = harga * jumlah
        print("Pembelian berhasil.")
        print("Total harga: Rp", total)

        if total >= 50000:
            print("Kategori: Pembelian besar")
        else:
            print("Kategori: Pembelian biasa")
else:
    print("Nomor obat tidak ditemukan.")