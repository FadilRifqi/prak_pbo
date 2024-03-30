# 1. Buatlah kelas induk Hewan dengan atribut nama dan jenis kelamin metode bersuara(),
# makan(), dan minum(). Kemudian buat dua kelas anak (turunannya) Kucing dan Anjing
# yang mewarisi metode dari kelas Hewan. Metode menghasilkan masing-masing output
# yang berbeda.
# Contoh output:
# hewan1 = Kucing("Kiki", “Betina”)
# hewan2 = Anjing("Ichi", “Jantan”)
# print(hewan1.nama) # Output: Kiki
# print(hewan2.nama) # Output: Ichi
# hewan1.bersuara() # Output: Kucing Kiki bersuara: Meong!
# hewan1.bersuara() # Output: Kucing Kiki sedang makan: tulang
# hewan2.bersuara() # Output: Anjing Ichi bersuara: Guk Guk!
# hewan2.bersuara() # Output: Anjing Ichi sedang makan: tulang

class Hewan:
    def __init__(self,nama,jenis_kelamin):
        self.nama = nama
        self.__jenis_kelamin = jenis_kelamin
        self._makan_count = 0


class Anjing(Hewan):
    def __init__(self, nama, jenis_kelamin):
        super().__init__(nama, jenis_kelamin)
        self.__jenis_hewan = "Anjing"
        self.suara = "Guk Guk"
    def bersuara(self):
        if self._makan_count == 0:
            print(f'{self.__jenis_hewan} {self.nama} bersuara: {self.suara}!')
            self._makan_count = self._makan_count + 1
        else:
            print(f'{self.__jenis_hewan} {self.nama} sedang makan: tulang')
            self._makan_count = 0
class Kucing(Hewan):
    def __init__(self, nama, jenis_kelamin):
        super().__init__(nama, jenis_kelamin)
        self.__jenis_hewan = "Kucing"
        self.suara = "Meong"
    def bersuara(self):
        if self._makan_count == 0:
            print(f'{self.__jenis_hewan} {self.nama} bersuara: {self.suara}!')
            self._makan_count = self._makan_count + 1
        else:
            print(f'{self.__jenis_hewan} {self.nama} sedang makan: tulang')
            self._makan_count = 0

hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")
print(hewan1.nama) 
print(hewan2.nama) 
hewan1.bersuara() 
hewan1.bersuara() 
hewan2.bersuara() 
hewan2.bersuara()
