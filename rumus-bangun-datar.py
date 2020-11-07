#RUMUS BANGUN DATAR
def LuasPersegi(sisi):
    luasP = sisi*sisi
    return luasP
def KelilingPersegi(sisi):
    kelilingP  = 4 * sisi
    return kelilingP
def LuasPersegiPanjang(panjang, lebar):
    luasPP = panjang * lebar
    return luasPP
def KelilingPersegiPanjang(panjang, lebar):
    kelilingPP = 2 * panjang  + 2 * lebar
    return kelilingPP
def LuasSegitiga(alas,tinggi):
    luasS = 0.5 * alas * tinggi
    return luasS
def KelilingSegitiga(sisiA, sisiB, sisiC):
    kelilingS = sisiA + sisiB + sisiC
    return kelilingS