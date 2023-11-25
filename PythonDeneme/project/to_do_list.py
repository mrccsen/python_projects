yapilacaklar = []

def liste_goster():
    sayi = 1
    for deger in yapilacaklar:
        print(f"{sayi}. : {deger}")
        sayi += 1
def liste_sil(i):
    deger = yapilacaklar.pop(i - 1)

while True:
    kullanici_yapilacak = input("Lütfen yapmak istediğinizi yazınız.(Eklemek için: K / Silmek İçin: S / Listenizi Görmek İçin: L) \n")
    if kullanici_yapilacak == "k":
        kullanici_input = input("Ne eklemek İstersiniz ?\n")
        yapilacaklar.append(kullanici_input)
    elif kullanici_yapilacak == "s":
        liste_goster()
        kullanici_deger = int(input("Hangi Yapılacak Listesini Silmek İstiyorsunuz? (Seçiminizi 1, 2, 3 Olarak Yapınız.)\n"))
        liste_sil(kullanici_deger)
    elif kullanici_yapilacak == "l":
        liste_goster()

