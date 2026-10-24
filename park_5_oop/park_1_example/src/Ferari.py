from src.Mobil import Mobil
class Ferari(Mobil):
    def __init__(self,merek,tipe_mobil,bahan_bakar):
        super().__init__(merek,tipe_mobil,"merah")
        self.bbm = bahan_bakar
    def getKelakson(self):
        print("Bunyi Kelason : Wooffffff!!!!!")