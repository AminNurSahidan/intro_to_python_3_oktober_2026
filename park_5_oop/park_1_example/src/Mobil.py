class Mobil:
    # Object
    merek = "default"
    tipe_mobil = "default"
    warna = "default"
    # Property
    veleg = "T34" # public
    _cc_mobil = 1500 #private
    __kursi = "Abu-abu" #protected

    # Constructor
    def __init__(self,merek,tipe_mobil,warna):
        self.merek = merek
        self.tipe_mobil = tipe_mobil
        self.warna = warna
    # Method atau fungsi
    # Enkapsulasi
    # get and set
    # get di untuk ambil data
    def getProfile(self):
        print(f"Merek\t\t: {self.merek}")
        print(f"Type\t\t: {self.tipe_mobil}")
        print(f"CC Mobil\t: {self._cc_mobil} cc")
        print(f"Warna\t\t: {self.warna}")
        print(f"Interior\t: {self.__kursi}")
        print(f"Veleg\t\t: {self.veleg}")
        print("===========")
    # set di gunakan untuk merubah data
    def setCC_Mobil(self,new_cc):
        self._cc_mobil = new_cc
    def getKelakson(self):
        print("Belum ada data")
