from src.Mobil import Mobil
from src.Ferari import Ferari

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
