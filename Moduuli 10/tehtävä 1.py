import random

class Hissi:
    def __init__(self, alin_kerros, ylimp_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylimp_kerros = ylimp_kerros

    def kerros_ylös(self):
        if self.kerros < self.ylimp_kerros:
            self.kerros += 1

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1

    def siirry_kerrokseen(self, kohdekerros):
        while self.kerros < kohdekerros:
            self.kerros_ylös()
        while self.kerros > kohdekerros:
            self.kerros_alas()
        return self.kerros

class Talo:
    def __init__(self, alin_kerros, ylimp_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylimp_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            hissi = self.hissit[hissin_numero]
            hissi.siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("{:<15} {:<15} {:<15} {:<15}".format("Auto", "Kuljettu matka (km)", "Nopeus (km/h)", "Tilanopeus (km/h)"))
        for auto in self.autot:
            print("{:<15} {:<15} {:<15} {:<15}".format(auto.rekisteritunnus, auto.kuljettu_matka, auto.tamanhetkinen_nopeus, auto.huippunopeus))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

if __name__ == "__main":
    # Hissien luominen
    talo = Talo(1, 10, 2)

    # Hissien siirtäminen
    talo.aja_hissiä(0, 7)
    talo.aja_hissiä(1, 3)

    # Tulostetaan hissien kerrosten tila
    for i, hissi in enumerate(talo.hissit):
        print(f"Hissi {i + 1} on kerroksessa {hissi.kerros}")

    # Palohälytys ja hissien siirtäminen pohjakerrokseen
    talo.palohälytys()
    for i, hissi in enumerate(talo.hissit):
        print(f"Hissi {i + 1} on kerroksessa {hissi.kerros} palohälytyksen jälkeen")

    # Kilpailun simulointi
    autot = [Auto(f"Auto-{i}", random.randint(100, 200)) for i in range(10)]
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        if tunti % 10 == 0:
            kilpailu.tulosta_tilanne()
        tunti += 1

    kilpailu.tulosta_tilanne()