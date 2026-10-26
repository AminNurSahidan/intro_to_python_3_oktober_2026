open_file = open("../write/data_user.txt", "r")
data = open_file.read()
print(data)
open_file.seek(0)

for line in open_file.readlines():
    print(line.strip())
    break