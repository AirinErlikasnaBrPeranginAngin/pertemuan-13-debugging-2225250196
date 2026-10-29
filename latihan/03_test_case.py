def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


test_case = [
    (80, "Lulus"),
    (60, "Lulus"),
    (59, "Tidak lulus"),
]

for nilai, hasil_harapan in test_case:
    hasil_aktual = status(nilai)

    print("Nilai:", nilai)
    print("Expected:", hasil_harapan)
    print("Actual:", hasil_aktual)

    if hasil_aktual == hasil_harapan:
        print("Status: PASS")
    else:
        print("Status: FAIL")

    print("-" * 25)