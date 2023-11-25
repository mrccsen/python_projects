def hesaplama(*args,**kwargs):
    if b == "+":
        sonuc = a + c
        print(sonuc)
    elif b == "-":
        sonuc = a - c
        print(sonuc)
    elif b == "/":
        if c == 0:
            print("Sıfıra Bölme Hatası.")
        else:
            sonuc = a / c
            print(sonuc) 
    elif b == "*":
       sonuc = a * c,
       print(sonuc)

while True:
            try:
                a = int(input("Lütfen ilk değeri giriniz."))
                b = input("Lütfen kullanacağınız operatörü giriniz.")
                c = int(input("Lütfen İkinci değeri giriniz."))
                hesaplama(a,b,c)
            except ValueError:
                print("Hatalı Giriş Yaptınız. Tekrar Deneyiniz.")
                continue        
            
            devam = input("Başka bir işlem yapmak ister misiniz ? (E/H)")
            if devam == "h":
                break
            elif devam == "e":
                continue