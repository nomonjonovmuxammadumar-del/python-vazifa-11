def omborlarni_birlashtir(ombor1: dict, ombor2: dict) -> dict:
    birlashgan = ombor1.copy()

    for mahsulot, miqdor in ombor2.items():
        if mahsulot in birlashgan:
            birlashgan[mahsulot] += miqdor
        else:
            birlashgan[mahsulot] = miqdor

    return birlashgan


if __name__ == "__main__":
    ombor_1 = {"olma": 20, "anor": 12, "nok": 8}
    ombor_2 = {"olma": 15, "banan": 10, "nok": 5}

    natija = omborlarni_birlashtir(ombor_1, ombor_2)
    print(natija)
