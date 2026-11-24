import math
from itertools import combinations


def masofa_hisobla(nuqta1: tuple, nuqta2: tuple) -> float:
    x1, y1 = nuqta1
    x2, y2 = nuqta2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def shaharlar_tahlili(shaharlar: dict):
    shahar_nomlari = list(shaharlar.keys())
    eng_uzoq_juftlik = None
    maks_masofa = -1.0

    for shahar1, shahar2 in combinations(shahar_nomlari, 2):
        masofa = masofa_hisobla(shaharlar[shahar1], shaharlar[shahar2])
        print(f"{shahar1} va {shahar2}: {masofa:.1f}")

        if masofa > maks_masofa:
            maks_masofa = masofa
            eng_uzoq_juftlik = (shahar1, shahar2, masofa)

    if eng_uzoq_juftlik:
        s1, s2, mas = eng_uzoq_juftlik
        print(f"Eng uzoq yo'nalish: {s1} - {s2} ({mas:.1f})")


if __name__ == "__main__":
    shaharlar = {"A": (0, 0), "B": (3, 4), "C": (6, 0)}
    shaharlar_tahlili(shaharlar)
