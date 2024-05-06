from abc import ABC, abstractmethod
from datetime import datetime


class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def leiras(self):
        pass


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=100, szobaszam=szobaszam)

    def leiras(self):
        return f"Egyágyas szoba {self.szobaszam} számmal. Ár: {self.ar} Ft."


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=150, szobaszam=szobaszam)

    def leiras(self):
        return f"Kétágyas szoba {self.szobaszam} számmal. Ár: {self.ar} Ft."


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in self.foglalasok:
                    if foglalas[0] == szoba and foglalas[1] == datum:
                        print("A szoba már foglalt ezen a napon.")
                        return None
                ar = szoba.ar
                self.foglalasok.append((szoba, datum))
                return ar
        print("Nincs ilyen szoba.")
        return None

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas[0].szobaszam == szobaszam and foglalas[1] == datum:
                self.foglalasok.remove(foglalas)
                print("Foglalás sikeresen törölve.")
                return
        print("Nincs ilyen foglalás.")

    def listaz_foglalasokat(self):
        for foglalas in self.foglalasok:
            print(f"Foglalás a(z) {foglalas[0].szobaszam} szobára, dátum: {foglalas[1].strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    szalloda = Szalloda(nev="Példa Szálloda")

    egyagyas_szoba1 = EgyagyasSzoba(szobaszam=101)
    egyagyas_szoba2 = EgyagyasSzoba(szobaszam=102)
    ketagyas_szoba1 = KetagyasSzoba(szobaszam=201)
    szalloda.uj_szoba(egyagyas_szoba1)
    szalloda.uj_szoba(egyagyas_szoba2)
    szalloda.uj_szoba(ketagyas_szoba1)

    foglalas_datum = datetime(2024, 5, 6)
    szalloda.foglalas(szobaszam=101, datum=foglalas_datum)
    szalloda.foglalas(szobaszam=102, datum=foglalas_datum)
    szalloda.foglalas(szobaszam=201, datum=foglalas_datum)

    szalloda.listaz_foglalasokat()

    szalloda.lemondas(szobaszam=101, datum=foglalas_datum)

    szalloda.listaz_foglalasokat()
