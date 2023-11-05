import math

# π/5 değerini hesaplayalım
x = math.pi / 5

# Tek terimli Taylor serisi hesaplama
tek_terimli_deger = 1

# İki terimli Taylor serisi hesaplama
iki_terimli_deger = 1 - (x**2) / 2

# Gerçek değeri hesaplama
gercek_deger = math.cos(x)

# Kesme hatası hesaplama
tek_terimli_hata = abs(gercek_deger - tek_terimli_deger)
iki_terimli_hata = abs(gercek_deger - iki_terimli_deger)

print(f"Gerçek Değer: {gercek_deger}")
print(f"Tek Terimli Yaklaşık Değer: {tek_terimli_deger}")
print(f"İki Terimli Yaklaşık Değer: {iki_terimli_deger}")
print(f"Tek Terimli Kesme Hatası: {tek_terimli_hata}")
print(f"İki Terimli Kesme Hatası: {iki_terimli_hata}")