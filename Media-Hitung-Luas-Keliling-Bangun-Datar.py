#Fungsi
def LuasBujurSangkar(sisi):
    luasBJ = sisi*sisi
    return luasBJ
def KelilingBujurSangkar(sisi):
    kelilingBJ  = 4 * sisi
    return kelilingBJ
def LuasPersegiPanjang(panjang, lebar):
    luasPP = panjang * lebar
    return luasPP
def KelilingPersegiPanjang(panjang, lebar):
    kelilingPP = panjang + panjang + lebar + lebar
    return kelilingPP
def LuasSegitiga(alas,tinggi):
    luasS = 0.5 * alas * tinggi
    return luasS
def KelilingSegitiga(sisiA, sisiB, sisiC):
    kelilingS = sisiA + sisiB + sisiC
    return kelilingS
def LuasLingkaran(jarijari):
    luasL = 3.14 * jarijari * jarijari
    return luasL
def KelilingLingkaran(jarijari):
    kelilingL = 3.14 * jarijari
    return kelilingL 
def LuasJajarGenjang(alas,tinggi):
    luasJG = alas * tinggi
    return luasJG
def KelilingJajarGenjang(alasA,tinggiB):
    kelilingJG = (alasA + tinggiB) * 2
    return kelilingJG

#PROGRAM UTAMA
pilihan = 1
while pilihan != 0:
    print("========================================== Perhitungan Luas & Keliling Bangun Datar =======================================")
    print("1. Luas Persegi")
    print("2. Keliling Persegi")
    print("3. Luas Persegi Panjang")
    print("4. Keliling Persegi Panjang")
    print("5. Luas Segitiga")
    print("6. Keliling Segitiga")
    print("7. Luas Lingkaran")
    print("8. Keliling Lingkaran")
    print("9. Luas Jajar Genjang")
    print("10.Keliling Jajar Genjang")
    print("0. Exit")
    print("============================================================================================================")

    pilihan = int(input("Masukkan Pilihan Anda:"))
    print('')

    if pilihan == 1:
        print("Luas Bujur Sangkar")
        print('')
        sisi = int(input("Masukkan Sisi: "))
        print('')
        print("Luas Bujur Sangkar adalah ", LuasBujurSangkar(sisi))
        print('')
    elif pilihan == 2:
        print("Keliling Bujur Sangkar")
        print('')
        sisi = int(input("Masukkan Sisi: "))
        print('')
        print("Keliling Bujur Sangkar adalah ", KelilingBujurSangkar(sisi))
    elif pilihan == 3:
        print("Luas Persegi Panjang")
        print('')
        panjang = int(input("Masukkan Panjang : "))
        lebar = int(input("Masukkan Lebar : "))
        print('')
        print("Luas Persegi Panjang Adalah  ", LuasPersegiPanjang(panjang,lebar))
        print('')
    elif pilihan == 4:
        print("Keliling Persegi Panjang")
        print('')
        panjang = int(input("Masukkan Panjang : "))
        lebar = int(input("Masukkan Lebar : "))
        print('')
        print("Keliling Persegi Panjang Adalah  ", KelilingPersegiPanjang(panjang,lebar))
        print('')
    elif pilihan == 5:
        print("Luas Segitiga")
        print('')
        alas = int(input("Masukkan Alas : "))
        tinggi = int(input("Masukkan Tinggi : "))
        print('')
        print("Luas Segitiga Adalah ", LuasSegitiga(alas,tinggi))
        print('')
    elif pilihan == 6:
        print("Keliling Segitiga")
        print('')
        sisiA = int(input("Masukkan Sisi A : "))
        sisiB = int(input("Masukkan Sisi B : "))
        sisiC = int(input("Masukkan Sisi C : "))
        print('')
        print("Keliling Segitiga Adalah ", KelilingSegitiga(sisiA,sisiB,sisiC))
        print('')
    elif pilihan == 7:
        print("Luas Lingkaran")
        print('')
        jarijari = float(input("Masukkan Jari - Jari : "))
        print('')
        print("Luas Lingkaran Adalah  ", LuasLingkaran(jarijari))
    elif pilihan == 8:
        print("Keliling Lingkaran")
        print('')
        jarijari2 = float(input("Masukkan Diameter : "))
        print('')
        print("Keliling Lingkaran Adalah ", KelilingLingkaran(jarijari))
        print('')
    elif pilihan == 9:
        print("Luas Jajar Genjang")
        print('')
        alas = int(input("Masukkan Alas : "))
        tinggi = int(input("Masukkan Tinggi : "))
        print('')
        print("Luas Jajar Genjang Adalah : ", LuasJajarGenjang(alas,tinggi))
        print('')
    elif pilihan == 10:
        print("Keliling Jajar Genjang")
        print('')
        alasA = int(input("Masukkan Alas : "))
        tinggiB = int(input("Masukkan Sisi  : "))
        print('')
        print("Keliling Jajar Genjang Adalah ", KelilingJajarGenjang(alasA,tinggiB))
        print('')
        print('')
    elif pilihan == 0:
        print("============================================= EXIT =============================================")
        print('')
        print('')
        break
    else :
        print("INPUT YANG ANDA MASUKKAN SALAH!")
        print('')
        print('')
