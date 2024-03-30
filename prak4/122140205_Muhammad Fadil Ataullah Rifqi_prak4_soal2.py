# Buatlah dua kelas Persegi dan Lingkaran dengan metode hitungLuas(). Gunakan konsep
# polimorfisme agar kita dapat menghitung luas dari objek berbentuk persegi atau lingkaran
# tanpa memeriksa jenis objek secara eksplisit.
# Contoh output:
# persegi = Persegi(5)
# lingkaran = Lingkaran(3)
# print(f"Luas Persegi: {persegi.hitungLuas()}") # Output: Luas Persegi: 25
# print(f"Luas Lingkaran: {lingkaran.hitungLuas()}") # Output: Luas Lingkaran:
# 28.274333882308138


class Bentuk:
    def hitungLuas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
        self.pi = 3.14159265358979323846

    def hitungLuas(self):
        return self.pi * self.jari_jari ** 2

persegi = Persegi(5)
lingkaran = Lingkaran(3)

print(f"Luas Persegi: {persegi.hitungLuas()}") 
print(f"Luas Lingkaran: {lingkaran.hitungLuas()}") 
