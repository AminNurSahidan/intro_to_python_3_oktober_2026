from src.Mobil import Mobil # pemanggilan class

if __name__ == "__main__":
    data_mobil = [
        {
        "category" : "Mobil",
        "merek" : "Toyota",
        "type" : "Supra MK4",
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
        "merek" : "Mitsubishi",
        "type" : "Lancer",
        "color" : "Merah"
        },
    ]

    for value in data_mobil:
        if value["category"] == "Mobil":
            data = Mobil(value['merek'],value['type'],value['color'])
            # data.velg = "Celong"
            data._cc_mobil = 7000 # ga bisa karena private variable nya
            data.getProfile()