import weakref

class Dagangan:
    jumlah_barang = 0
    list_barang = weakref.WeakSet()
    
    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.list_barang.add(self)
        Dagangan.jumlah_barang += 1
    
    def get_nama(self):
        return self.__nama
    
    def get_stok(self):
        return self.__stok
    
    def get_harga(self):
        return self.__harga
    
    @classmethod
    def lihat_barang(self):
        print("Jumlah barang dagangan pada toko:",self.jumlah_barang,"buah")
        for idx,dagangan in enumerate(self.list_barang,start=1):
            print(f"{idx}. {dagangan.get_nama()} seharga Rp {dagangan.get_harga()} (stok:{dagangan.get_stok()})")

    def __del__(self):
        Dagangan.jumlah_barang-=1
        for dagangan in Dagangan.list_barang:
            if self.get_nama() in dagangan.get_nama():
                dagangan.list_barang.remove(dagangan)
                print(f"{dagangan.__nama} dihapus dari toko!")
                break  
     
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()
del Dagangan1
Dagangan.lihat_barang()