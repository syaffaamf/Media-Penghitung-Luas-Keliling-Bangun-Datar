#modulfungsi
def kelilingjargen(jmlsihor,jmlsiver):
    kelilingJG=jmlsihor+jmlsiver
    return kelilingJG
def luasjargen(alas,tinggi):
    luasJG=alas*tinggi
    return luasJG
def kelilinglingkaran(phi,d):
    kelilingLing=phi*d
    return kelilingLing
def luaslingkaran(phi,r):
    luasLing=phi*r*r
    return luasLing
#programutama
print("MENGHITUNG LUAS DAN KELILING")
pilihan=1
while pilihan !=0:
    print("1. K jajar genjang")
    print("2. L jajar genjang")
    print("3. K lingkaran")
    print("4. L lingkaran")
    print("5. exit")
    print("")
    print("")
    print("")
    pilihan=int(input("masukkan pilihan anda :"))
    print("")
    print("")
    
    if pilihan ==1:
        print("KELILING JAJAR GENJANG")
        jmlsihor=float(input("masukkan jumlah nilai sisi horizontal :"))
        jmlsiver=float(input("masukkan jumlah nilai sisi vertikal :"))
        print("keliling jajar genjang adalah :", kelilingjargen(jmlsihor,jmlsiver))
        print("")
        print("")
        print("")
    elif pilihan==2:
        print("LUAS JAJAR GENJANG")
        alas=float(input("masukkan nilai alas :"))
        tinggi=float(input("masukkan nilai tinggi :"))
        print("luas jajar genjang adalah :", luasjargen(alas,tinggi))
        print("")
        print("")
        print("")
    elif pilihan==3:
        print("KELILING LINGKARAN")
        phi=float(input("masukkan nilai phi :"))
        d=float(input("masukkan nilai diameter :"))
        print("keliling lingkaran adalah :", kelilinglingkaran(phi,d))
    elif pilihan==4:
        print("LUAS LINGKARAN")
        phi=float(input("masukkan nilai phi :"))
        r=float(input("masukkan nilai jari-jari :"))
        print("luas lingkaran adalah :", luaslingkaran(phi,r))
    elif pilihan==5:
        print("====================EXIT======================")
        break
    else:
        print("pilihan yang anda masukan salah, silahkan masukan angka yang anda pilih lagi")
        print("")
        print("")
        print("")
