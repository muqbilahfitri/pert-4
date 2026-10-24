angka = []
while True:
    i = int(input("Masukkan angka kedalam list. \n(Ketik '-999' jika dirasa sudah cukup)\n:"))
    if i == -999 :
        break
    angka.append(i)
print("Final list anda adalah {angka}")

if len(angka) == 0 :
    print("List anda kosong. Tolong isi beberapa")
else:
    angka_terbesar = angka[0]
    for i in angka:
        if i > angka_terbesar:
         angka_terbesar = i
    print(f"Angka terbesar adalah {angka_terbesar}")