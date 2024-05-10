# Temel sınıf Hayvan
class Hayvan:
    def __init__(self, isim):
        self.isim = isim

    def ses_cikar(self):
        return "Hayvan sesi"


# Türetilmiş sınıf Kopek
class Kopek(Hayvan):
    def __init__(self, isim, cins):
        super().__init__(isim)
        self.cins = cins

    def ses_cikar(self):
        return "Hav hav!"


# Türetilmiş sınıf Kedi
class Kedi(Hayvan):
    def __init__(self, isim, tur):
        super().__init__(isim)
        self.tur = tur

    def ses_cikar(self):
        return "Miyav miyav"


# Hayvan sınıfından bir örnek oluşturma
genel_hayvan = Hayvan("Genel bir hayvan")
print(genel_hayvan.ses_cikar())

# Kopek sınıfından bir örnek oluşturma
benim_kopek = Kopek("Karabaş", "Golden")
print(benim_kopek.ses_cikar())
print(f"İsim: {benim_kopek.isim}, Cins: {benim_kopek.cins}")

# Kedi sınıfından bir örnek oluşturma
benim_kedi = Kedi("Mırmır", "Van Kedisi")
print(benim_kedi.ses_cikar())
print(f"İsim: {benim_kedi.isim}, Tür: {benim_kedi.tur}")
