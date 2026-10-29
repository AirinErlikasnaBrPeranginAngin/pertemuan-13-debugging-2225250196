def hitung_total(nilai):
    total = 0

    for x in nilai:
        total += x

    return total


data_nilai = [80, 60, 90]

hasil = hitung_total(data_nilai)

print("Total nilai:", hasil)