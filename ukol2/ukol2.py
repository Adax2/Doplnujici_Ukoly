def resi_osmi_damy() -> list[list[int]]:
    reseni = []
    umisteni = [-1] * 8

    def je_platne(radek: int, sloupec: int) -> bool:
        for i in range(radek):
            if umisteni[i] == sloupec:
                return False
            if abs(umisteni[i] - sloupec) == radek - i:
                return False
        return True

    def zpetne_hledani(radek: int):

        if radek == 8:
            reseni.append(umisteni.copy())
            return
        for sloupec in range(8):
            if je_platne(radek, sloupec):
                umisteni[radek] = sloupec
                zpetne_hledani(radek + 1)
                umisteni[radek] = -1

    zpetne_hledani(0)
    return reseni

if __name__ == "__main__":
    vse_reseni = resi_osmi_damy()
    print(f"celkem mame {len(vse_reseni)} řešení.")
    for cislo, reseni in enumerate(vse_reseni, start=1):
        print(f"{cislo:3d}: {reseni}")
