

class canlılar:

    def __init__(self, id):
        self.id = id

    def solunum(self):
        print("solunum yapılır")

    def hucresel_yapi(self):
        print("hücre yapısına sahibim")

    def beslenme(self, besin_türü):
        self.besin_turu = besin_türü
        print(f"{besin_türü} şeklinde beslenir.")

class cok_hucreli_canlılar(canlılar):
    def __init__(self, id):
        super().__init__(id)

kedi = cok_hucreli_canlılar(1)
kedi.beslenme("kedi maması")

print(kedi.besin_turu)