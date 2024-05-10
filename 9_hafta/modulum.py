# hayvanlar.py

class Hayvan:
    def __init__(self, isim):
        self.isim = isim

    def ses_cikar(self):
        return "Hayvan sesi"


class Kopek(Hayvan):
    def __init__(self, isim, cins):
        super().__init__(isim)
        self.cins = cins

    def ses_cikar(self):
        return "Hav hav!"


class Kedi(Hayvan):
    def __init__(self, isim, tur):
        super().__init__(isim)
        self.tur = tur

    def ses_cikar(self):
        return "Miyav miyav"
