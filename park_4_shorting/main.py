import random

def generate_random_number(jumlah_angka):
    data = []
    for value in range(jumlah_angka):
        value_number = random.randint(1,100)
        data.append(value_number)
    return data

def bubble_short(data):
    jumlah_data = len(data)
    for index in range(jumlah_data):
        for value in range(0, jumlah_data-index-1):
            if data[value] > data[value+1]:
                tmp = data[value]
                data[value] = data[value+1]
                data[value+1] = tmp

def selection_sort(data):
    jumlah_data =  len(data)
    for index in range(jumlah_data):
        min_index = index
        for value in range(index + 1, jumlah_data):
            if data[value] < data[min_index]:
                min_index = value
        data[index], data[min_index] = data[min_index], data[index]

def insert_sort(data):
    for index in range(1,len(data)):
        value_min = data[index]
        value = index - 1
        while value >= 0 and value_min < data[value]:
            data[value + 1] = data[value]
            value -= 1
        data[value + 1] = value_min

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        data_kiri = data[:mid]
        data_kanan = data[mid:]

        merge_sort(data_kiri) # ini sebutannya recursif
        merge_sort(data_kanan)

        index = value = real_value = 0
        while index < len(data_kiri) and value < len(data_kanan):
            if data_kiri[index] < data_kanan[value]:
                data[real_value] = data_kiri[index]
                index += 1
            else:
                data[real_value] = data_kanan[value]
                value += 1
            real_value += 1

        while index < len(data_kiri):
            data[real_value] = data_kiri[index]
            index += 1
            real_value += 1

        while value < len(data_kanan):
            data[real_value] = data_kanan[value]
            value += 1
            real_value += 1

if __name__ == "__main__":
    jumlah_data =  int(input("Masukkan jumlah data :"))

    data = generate_random_number(jumlah_data)
    print("=====Before=====")
    print(data)
    input("Press Enter to next step")
    # bubble_short(data)
    # selection_sort(data)
    # insert_sort(data)
    merge_sort(data)
    print("=====After======")
    print(data)