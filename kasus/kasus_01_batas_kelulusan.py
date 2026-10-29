def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


print("Nilai 80:", status(80))
print("Nilai 60:", status(60))
print("Nilai 59:", status(59))