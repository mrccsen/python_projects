import random

unlu_harfler = ["A","E","U","I","O","Ü","İ","Ö"]
unsuz_harfler=["R","T","Y","P","Ğ","S","D","F","G","H","J","K","L","Ş","Z","C","V","B","N","M","Ç"]

def isimolustur(random_sayi, random_sayi2):
    first_name = ""
    last_name = ""
    for i in range(random_sayi):
        random_unlu = random.choice(unlu_harfler)
        random_unsuz = random.choice(unsuz_harfler)
        first_name += random_unsuz + random_unlu
    for i in range(random_sayi2):
        random_unsuz = random.choice(unsuz_harfler)
        random_unlu = random.choice(unlu_harfler)
        last_name += random_unsuz + random_unlu
    return first_name, last_name

first_name, last_name = isimolustur(random.randint(1,4), random.randint(1,4))
print(first_name)
print(last_name)