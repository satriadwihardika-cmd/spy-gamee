# SPY GAME V4 - TANPA EMOJI

def intro():
    print("=== SPY GAME ===")
    print("Kamu adalah agen rahasia yang sedang menjalankan misi.")
    print("Jawab semua pertanyaan dengan A, B, atau C.")
    print("Setiap pilihan akan menentukan akhir cerita.\n")


def pilih_rute():
    print("Cara masuk ke markas:")
    print("A. Ventilasi")
    print("B. Pintu depan")
    print("C. Terowongan bawah tanah")
    return input("Pilihan: ").upper()


def pertanyaan(teks, a, b, c):
    print("\n" + teks)
    print("A.", a)
    print("B.", b)
    print("C.", c)
    return input("Jawaban: ").upper()


def gameplay():
    skor = 0
    rahasia = 0

    # Rute awal
    rute = pilih_rute()
    if rute == "A":
        skor += 1
    elif rute == "C":
        rahasia += 1
    else:
        skor -= 1

    # Soal 1
    q1 = pertanyaan(
        "Kamu melihat kamera keamanan.",
        "Hack sistem kamera",
        "Hancurkan kamera",
        "Lewat perlahan tanpa suara"
    )

    if q1 == "A":
        skor += 1
    elif q1 == "C":
        rahasia += 1
    else:
        skor -= 1

    # Soal 2
    q2 = pertanyaan(
        "Ada penjaga yang sedang patroli.",
        "Sembunyi di balik kotak",
        "Serang penjaga",
        "Alihkan perhatian dengan suara"
    )

    if q2 == "A":
        skor += 1
    elif q2 == "C":
        rahasia += 1
    else:
        skor -= 1

    # Soal 3
    q3 = pertanyaan(
        "Kamu menemukan ruang server terkunci.",
        "Hack pintu elektronik",
        "Tinggalkan ruangan",
        "Cari kartu akses cadangan"
    )

    if q3 == "A":
        skor += 1
    elif q3 == "C":
        rahasia += 1
    else:
        skor -= 1

    # Soal 4
    q4 = pertanyaan(
        "Alarm hampir aktif.",
        "Matikan sistem alarm",
        "Langsung kabur",
        "Bersembunyi dan tunggu"
    )

    if q4 == "A":
        skor += 1
    elif q4 == "C":
        rahasia += 1
    else:
        skor -= 1

    # Soal 5
    q5 = pertanyaan(
        "Kamu menemukan dokumen misterius.",
        "Ambil dokumen",
        "Abaikan dan fokus misi",
        "Foto dokumen diam-diam"
    )

    if q5 == "A":
        rahasia += 1
    elif q5 == "B":
        skor += 1
    else:
        skor -= 1

    # Soal 6
    q6 = pertanyaan(
        "Jalur keluar terhalang.",
        "Cari jalur alternatif",
        "Terobos paksa",
        "Gunakan lorong rahasia"
    )

    if q6 == "A":
        skor += 1
    elif q6 == "C":
        rahasia += 1
    else:
        skor -= 1

    return skor, rahasia


def ending(skor, rahasia):
    print("\n=== HASIL MISI ===")

    if rahasia >= 4:
        print("Kamu menemukan konspirasi besar dan menghilang tanpa jejak.")
        print("SECRET ENDING")

    elif skor >= 5:
        print("Misi berhasil. Data berhasil dibawa keluar dengan aman.")
        print("GOOD ENDING")

    elif skor <= 0:
        print("Misi gagal total. Kamu tertangkap di dalam markas.")
        print("BAD ENDING")

    else:
        print("Misi tidak sepenuhnya berhasil.")
        print("BAD ENDING")


# PROGRAM UTAMA
intro()
skor, rahasia = gameplay()
ending(skor, rahasia)
