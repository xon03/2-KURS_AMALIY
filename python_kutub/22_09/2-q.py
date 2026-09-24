matn=input("Matn kiriting: ").lower()
soz=input("So'zni kiriting: ").lower()
s=matn.find(soz)
if s==-1:
    print("Mavjud emas")
else:
    n=matn.count(soz)
    print(f"{n} marta kelgan")
    print(f"Indeksi: {s}")