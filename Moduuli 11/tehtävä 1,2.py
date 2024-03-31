class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        pass

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}\nPäätoimittaja: {self.paatoimittaja}")

if __name__ == "__main__":
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti_nro_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    print("Julkaisujen tiedot:")
    aku_ankka.tulosta_tiedot()
    print("\n")
    hytti_nro_6.tulosta_tiedot()

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, tunti):
        self.matkamittari += self.huippunopeus * tunti

    def tulosta_matkamittari(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}\nMatkamittari: {self.matkamittari} km")

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def aja(self, tunti):
        self.matkamittari += min(self.huippunopeus, self.akkukapasiteetti) * tunti
        self.akkukapasiteetti -= min(self.huippunopeus, self.akkukapasiteetti) * tunti / self.huippunopeus

    def tulosta_matkamittari(self):
        super().tulosta_matkamittari()
        print(f"Akkukapasiteetti: {self.akkukapasiteetti} kWh")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def aja(self, tunti):
        self.matkamittari += self.huippunopeus * tunti
        self.bensatankin_koko -= self.huippunopeus * tunti / 10

    def tulosta_matkamittari(self):
        super().tulosta_matkamittari()
        print(f"Bensatankin koko: {self.bensatankin_koko} l")

if __name__ == "__main__":
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sähköauto.aja(3)
    polttomoottoriauto.aja(3)

    print("Sähköauto:")
    sähköauto.tulosta_matkamittari()
    print("\nPolttomoottoriauto:")
    polttomoottoriauto.tulosta_matkamittari()