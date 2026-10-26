from src.Mobil import Mobil
from src.Ferari import Ferari
from src.Lamborgini import Lamborgini

def getKelakson(Mobil):
    Mobil.getKelakson()

if __name__ == "__main__":
    data_mobil = [
        {
        "category" : "Mobil",
        "merek" : "Toyota",
        "type" : "Supra",
        "color" : "Orange"
        },
        {
        "category" : "Mobil",
        "merek" : "Honda",
        "type" : "Civic",
        "color" : "Hitam"
        },
        {
        "category" : "Mobil",
        "merek" : "Mitsubisi",
        "type" : "Lancer",
        "color" : "Merah"
        },
    ]

    for value in data_mobil:
        
        if value["category"] == "Mobil":
            data = Mobil(value['merek'],value['type'],value['color'])
            # data.veleg = "Celong"
            if value['type'] == "Lancer":
                data.setCC_Mobil(25000)
            data.getProfile()
          
        print("======Inheritance======")
        data = Ferari("Ferari","testarossa","Bensin")
        data.getProfile()
        print("======Polymopisme======")
        mobil_1 = Ferari("Ferari", "testarossa", "Bensin")
        mobil_2 = Lamborgini("Lamborgini", "aventador", "Bensin")
        for value in range(1, 3):
            getKelakson(globals()[f"mobil_{value}"])
