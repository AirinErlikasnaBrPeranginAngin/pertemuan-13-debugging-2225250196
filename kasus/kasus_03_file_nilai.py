def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]

    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x

    return tertinggi


data_nilai = [80, 60, 90, 70]
print("Nilai tertinggi:", nilai_tertinggi(data_nilai))