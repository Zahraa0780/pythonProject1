import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        if nopeuden_muutos > 0:
            uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
            self.tamanhetkinen_nopeus = min(uusi_nopeus, self.huippunopeus)
        elif nopeuden_muutos < 0:
            uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
            self.tamanhetkinen_nopeus = max(uusi_nopeus, 0)

    def kulje(self, tuntimäärä):
        matka = self.tamanhetkinen_nopeus * tuntimäärä
        self.kuljettu_matka += matka

if __name__ == "__main__":,
    # Luodaan yksi auto ja tulostetaan sen ominaisuudet
    auto1 = Auto("ABC-123", 142)
    print("Luodun auton tiedot:")
    print("Rekisteritunnus:", auto1.rekisteritunnus)
    print("Huippunopeus:", auto1.huippunopeus, "km/h")
    print("Tämänhetkinen nopeus:", auto1.tamanhetkinen_nopeus, "km/h")
    print("Kuljettu matka:", auto1.kuljettu_matka, "km")

    # Kiihdytetään ja tulostetaan nopeudet
    auto1.kiihdyta(30)
    auto1.kiihdyta(70)
    auto1.kiihdyta(50)
    print("\nAuton nopeus kiihdytysten jälkeen:", auto1.tamanhetkinen_nopeus, "km/h")

    # Hätäjarrutus ja uusi nopeus
    auto1.kiihdyta(-200)
    print("Nopeuden muutos hätäjarrutuksen jälkeen:", auto1.tamanhetkinen_nopeus, "km/h")

    # Kuljetaan autoa ja tulostetaan kuljettu matka
    auto1.kulje(1.5)
    print("Kuljetun matkan päivityksen jälkeen:", auto1.kuljettu_matka, "km")

    # Luodaan kymmenen autoa kilpailua varten
    autot = []
    for i in range(10):
        rekisteritunnus = f"ABC-{i + 1}"
        huippunopeus = random.randint(100, 200)
        auto = Auto(rekisteritunnus, huippunopeus)
        autot.append(auto)

    kilpailu_jatkuu = True
    tunti = 0

    while kilpailu_jatkuu:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)
            if auto.kuljettu_matka >= 10000:
                kilpailu_jatkuu = False
                break
        tunti += 1

    # Tulostetaan kilpailun tulokset
    print("\nKilpailun tulokset:")
    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format("Auto", "Rekisteritunnus", "Huippunopeus (km/h)", "Kuljettu matka (km)", "Nopeus (km/h)"))
    for auto in autot:
        print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(auto, auto.rekisteritunnus, auto.huippunopeus, auto.kuljettu_matka, auto.tamanhetkinen_nopeus