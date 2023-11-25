import random

y = 0
x = random.randint(100,1000)
print(x)
kullanici_tahmini = int(input("Lütfen 100 ile 1000 arasında sayı tahmin ediniz."))

while y == 0:
    
    if x == kullanici_tahmini:
        print("Tebrikler!!! doğru bildiniz.")
        y = 1
    elif x > kullanici_tahmini:
        print(f"Sayınız tahmin etmeniz gereken sayıdan küçük.")
        kullanici_tahmini = int(input("Tekrar tahmin ediniz."))
    else:
        print("Sayınız tahmin etmeniz gereken sayıdan büyük.")
        kullanici_tahmini = int(input("Tekrar tahmin ediniz."))