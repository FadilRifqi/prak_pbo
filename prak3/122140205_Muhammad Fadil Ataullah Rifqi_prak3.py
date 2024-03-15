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

    def __del__(self):
        print(f'{self.get_nama()} dihapus dari toko')
        Dagangan.jumlah_barang -= 1
    
    def get_nama(self):
        return self.__nama
    
    def get_stok(self):
        return self.__stok
    
    def get_harga(self):
        return self.__harga
    
    @classmethod
    def lihat_barang(cls):
        print(f'Jumlah barang dagangan pada toko: {cls.jumlah_barang} buah' )
        for barang in cls.list_barang:
            print(f'{barang.get_nama()} seharga Rp {barang.get_harga()} (stok: {barang.get_stok()})')

Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()
del Dagangan1
Dagangan.lihat_barang()