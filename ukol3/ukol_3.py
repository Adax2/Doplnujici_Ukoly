from collections import deque
from typing import List, Tuple, Optional


class Bludiste:
    def __init__(self, cesta: str) -> None:
        self.pole: List[List[str]] = []
        self.start: Optional[Tuple[int, int]] = None
        self.cil: Optional[Tuple[int, int]] = None

        with open(cesta, encoding="utf-8") as f:
            for r, radek in enumerate(f):
                radek = radek.rstrip("\n")
                self.pole.append(list(radek))
                for c, znak in enumerate(radek):
                    if znak == 'A':
                        self.start = (r, c)
                    elif znak == 'B':
                        self.cil = (r, c)

        if self.start is None or self.cil is None:
            raise ValueError("bludiště musí obsahovat start A a cil B")

    def vykresli(self) -> None:
        for radek in self.pole:
            print("".join(radek))

    def oznac_cestu(self, cesta: List[Tuple[int, int]]) -> None:

        kopie = [radek.copy() for radek in self.pole]
        for r, c in cesta:
            if kopie[r][c] not in ('A', 'B'):
                kopie[r][c] = '.'
        for radek in kopie:
            print("".join(radek))


class Planovac:
    def __init__(self, bludiste: Bludiste) -> None:
        self.bludiste = bludiste

    def najdi_cestu(self) -> Optional[List[Tuple[int, int]]]:
        start = self.bludiste.start
        cil = self.bludiste.cil
        if start is None or cil is None:
            return None
        smery = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        navstivene = set()
        navstivene.add(start)
        predkovi = {}
        fronta = deque([start])

        while fronta:
            pozice = fronta.popleft()
            if pozice == cil:
                cestovni_seznam = []
                while pozice != start:
                    cestovni_seznam.append(pozice)
                    pozice = predkovi[pozice]
                cestovni_seznam.append(start)
                cestovni_seznam.reverse()
                return cestovni_seznam

            r, c = pozice
            for dr, dc in smery:
                nova_pozice = (r + dr, c + dc)
                if nova_pozice in navstivene:
                    continue
                if 0 <= nova_pozice[0] < len(self.bludiste.pole) and 0 <= nova_pozice[1] < len(self.bludiste.pole[0]):
                    znak = self.bludiste.pole[nova_pozice[0]][nova_pozice[1]]
                    if znak != '#':
                        navstivene.add(nova_pozice)
                        predkovi[nova_pozice] = pozice
                        fronta.append(nova_pozice)
        return None


if __name__ == "__main__":
    cesta_k_souboru = "bludiste.txt"
    try:
        bludiste = Bludiste(cesta_k_souboru)
    except Exception as e:
        print("chyba při načítání bludiště:", e)
        exit(1)

    print("bludiště:")
    bludiste.vykresli()

    planovac = Planovac(bludiste)
    cesta = planovac.najdi_cestu()
    if cesta is None:
        print("cestu se nepodařilo najít.")
    else:
        print("\nnejkratší cesta nalezena:")
        print(cesta)
        print("\nbludiště s řešením:")
        bludiste.oznac_cestu(cesta)
