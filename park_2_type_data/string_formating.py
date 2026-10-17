import datetime as date
tanggal = date.datetime.now()
manager = "Budiono Siregar"
pt = "PT. Kapal Lawud"
alamat = "Jakarta Timur"

# String Formating Positional
print("=====POSITIONAL=====")
print("\t\t\t{0}\nYth. {1}\nManager SDM {2}\n{3}".format(tanggal, pt, manager, alamat))
# String Formating Keyword
print("=====KEYWORD=====")
print("\t\t\t{tanggal}\nYth. {manager}\nManager SDM {pt}\n{alamat}".format(tanggal=tanggal, manager=manager, pt=pt, alamat=alamat))
# String Formating F-String
print("=====SHORTCUT=====")
print(f"\t\t\t{tanggal}\nYth. {manager}\nManager SDM {pt}\n{alamat}")