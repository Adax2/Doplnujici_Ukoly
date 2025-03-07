import random
import time
from typing import List, Optional


def linearni_vyhledavani(pole: List[int], hledana_hodnota: int) -> Optional[int]:
    for i, hodnota in enumerate(pole):
        if hodnota == hledana_hodnota:
            return i
    return None


def binarni_vyhledavani(pole: List[int], hledana_hodnota: int) -> Optional[int]:
    leva = 0
    prava = len(pole) - 1
    while leva <= prava:
        stred = (leva + prava) // 2
        if pole[stred] == hledana_hodnota:
            return stred
        elif pole[stred] < hledana_hodnota:
            leva = stred + 1
        else:
            prava = stred - 1
    return None


def generuj_serazene_pole(pocet: int, minimalni: int = 0, maximalni: int = 1000000) -> List[int]:
    pole = [random.randint(minimalni, maximalni) for _ in range(pocet)]
    pole.sort()
    return pole


if __name__ == "__main__":

    pocet_prvku = 1000000
    test_hodnoty = [random.randint(0, 1000000) for _ in range(10)]  #

    pole = generuj_serazene_pole(pocet_prvku)

    print("test vyhledavani v poli o velikosti:", pocet_prvku)
    for hledana_hodnota in test_hodnoty:
        print(f"\nhledaná hodnota: {hledana_hodnota}")

        start = time.perf_counter()
        index_linear = linearni_vyhledavani(pole, hledana_hodnota)
        end = time.perf_counter()
        cas_linear = (end - start) * 1000

        start = time.perf_counter()
        index_binarni = binarni_vyhledavani(pole, hledana_hodnota)
        end = time.perf_counter()
        cas_binarni = (end - start) * 1000

        print(f"  lineární vyhledávání: index = {index_linear}, čas = {cas_linear:.4f} ms")
        print(f"  Binární vyhledávání:  index = {index_binarni}, čas = {cas_binarni:.4f} ms")

    print("\nAnalýza:")
    print("  - lineární vyhledávání prochází každý prvek zvlášt, což může být pomalé u velkých polí.")
    print("  - binární vyhledávání pracuje se seřazeným polem a dělí hledaný interval na poloviny,")
    print("    což je mnohem rychlejší.")
