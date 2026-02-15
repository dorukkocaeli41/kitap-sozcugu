import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Şifre Uzunluğunu Giriniz: "))
sifre = ""
for i in range(uzunluk):
 print (random.choice(karakterler))