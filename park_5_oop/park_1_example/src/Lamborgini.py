from src.Mobil import Mobil
class Lamborgini(Mobil):
    def __init__(self,merek,tipe_mobil,bahan_bakar):
        super().__init__(merek,tipe_mobil,"merah")
        self.bbm = bahan_bakar
    def getKelakson(self):
        print("Bunyi Kelason : Neeetnoott")
    # override
    def getProfile(self):
        print(f"Bahan Bakar\t: {self.bbm}")
        super().getProfile()