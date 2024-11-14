import ast

def anamenu():
    print("╔═══════════════════════════════╗")
    print("║     GEZİ REHBERİ              ║")
    print("║═══════════════════════════════║")
    print("║  1-Rehbere Ekle               ║")
    print("║  2-Gezilecek Yerler Listesi   ║")
    print("║  3-İçerik Düzenle             ║")
    print("║  4-İçerik Silme               ║")
    print("║  5-Yer Ara                    ║")
    print("║  Seçiminiz Nedir:             ║")
    print("║                               ║")
    print("╚═══════════════════════════════╝")

    secim = input("")

    if secim == "1":
        rehber_ekle()
        anamenu()
    elif secim == "2":
        rehber_listele()
        anamenu()
    elif secim == "3":
        rehber_duzelt()
        anamenu()
    elif secim == "4":
        rehber_sil()
        anamenu()
    elif secim == "5":
        rehber_ara()
        anamenu()

def rehber_ekle():

    print("╠════════════╣ YENİ YER EKLE ╠════════════╣")

    ad = input("Kaydedilecek Yer Bilgisi : ")

    try:
        with open("gezirehberi.txt", "r") as dosya:
            okunan = dosya.read()
            if okunan.strip(): 
                yerler = ast.literal_eval(okunan)
            else:
                yerler = []
    except FileNotFoundError:
        yerler = []

    yerler.append({"yeradi": ad})

    with open("gezirehberi.txt", "w") as dosya:
        dosya.write(str(yerler))
    
    print("Yer başarıyla eklendi!")
    anamenu()

def rehber_listele():
    try:
        with open("gezirehberi.txt", "r") as dosya:
            okunan = dosya.read()

        print("╠════════════╣ YER LİSTELEME ╠════════════╣")

        if okunan.strip():
            yerler = ast.literal_eval(okunan)
            for yer in yerler:
                print(yer)
        else:
            print("Hiç yer eklenmemiş!")
    except FileNotFoundError:
        print("Gezirehberi dosyası bulunamadı!")

    anamenu()

def rehber_duzelt():
    try:
        with open("gezirehberi.txt", "r") as dosya:
            okunan = dosya.read()
            yerler = ast.literal_eval(okunan)
        
        print("╠════════════╣ YER DÜZELTME ╠════════════╣")
        aranan = input("Düzeltilecek isim nedir? ")

        for yer in yerler:
            if yer["yeradi"] == aranan:
                print(f"Bulunan Yer: {yer}")
                yeniAd = input("Yeni ad nedir? ")
                yer["yeradi"] = yeniAd
                break
        else:
            print("Yer bulunamadı!")

        with open("gezirehberi.txt", "w") as dosya:
            dosya.write(str(yerler))

        print("Yer başarıyla güncellendi!")
    except FileNotFoundError:
        print("Gezirehberi dosyası bulunamadı!")

    anamenu()

def rehber_sil():
    try:
        with open("gezirehberi.txt", "r") as dosya:
            okunan = dosya.read()
            yerler = ast.literal_eval(okunan)

        print("╠════════════╣ YER SİLME ╠════════════╣")
        print("Mevcut Yerler:")
        for idx, yer in enumerate(yerler, 1):
            print(f"{idx}. {yer['yeradi']}")

        silinecek = int(input("Hangi kayıt silinecek (numarasını girin): ")) - 1

        if 0 <= silinecek < len(yerler):
            print(f"Silinecek Yer: {yerler[silinecek]}")
            yerler.pop(silinecek)

            with open("gezirehberi.txt", "w") as dosya:
                dosya.write(str(yerler))

            print("Yer başarıyla silindi!")
        else:
            print("Geçersiz seçim!")
    except FileNotFoundError:
        print("Gezirehberi dosyası bulunamadı!")

    anamenu()

def rehber_ara():
    try:
        with open("gezirehberi.txt", "r") as dosya:
            okunan = dosya.read()
            yerler = ast.literal_eval(okunan)

        print("╠════════════╣ YER ARAMA ╠════════════╣")
        aranan = input("Aranan Yer Nedir? ")

        found = False
        for yer in yerler:
            if yer["yeradi"] == aranan:
                print(f"Bulunan Yer: {yer}")
                found = True
                break
        
        if not found:
            print("Yer bulunamadı!")

    except FileNotFoundError:
        print("Gezirehberi dosyası bulunamadı!")

    anamenu()

anamenu()
