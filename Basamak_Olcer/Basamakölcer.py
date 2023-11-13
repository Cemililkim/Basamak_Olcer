# 1. Programı başlat.
# 2. Sayaç'ı 1 olarak başlat.
sayac = 1

# 3. Kullanıcıdan S değerini oku.
S = int(input("S değerini girin: "))

while S < 0:
    S = S * -1
    
# 4. S'yi 10'a böl.
# 5. Sayaç'ı bir arttır.
while S > 10:
    S = S / 10
    sayac += 1

# 7. B değerini Sayaç olarak al.
B = sayac

# 8. B'yi yazdır.
print("B:", B)

# 9. Programı bitir.
