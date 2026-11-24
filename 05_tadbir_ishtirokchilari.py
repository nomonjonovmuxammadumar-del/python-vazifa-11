def tadbirlarni_tahlil_qil(tadbir1: set, tadbir2: set, tadbir3: set):
    barcha_tadbirlarda = tadbir1 & tadbir2 & tadbir3

    faqat_bitta = (
        (tadbir1 - tadbir2 - tadbir3)
        | (tadbir2 - tadbir1 - tadbir3)
        | (tadbir3 - tadbir1 - tadbir2)
    )

    kamida_ikkita = (
        (tadbir1 & tadbir2)
        | (tadbir2 & tadbir3)
        | (tadbir1 & tadbir3)
    )

    barcha_odamlar = []
    for toplanm in [tadbir1, tadbir2, tadbir3]:
        for kishi in toplanm:
            if kishi not in barcha_odamlar:
                barcha_odamlar.append(kishi)

    barchada_tartibli = [k for k in barcha_odamlar if k in barcha_tadbirlarda]
    faqat_bitta_tartibli = [k for k in barcha_odamlar if k in faqat_bitta]
    kamida_ikkita_tartibli = [k for k in barcha_odamlar if k in kamida_ikkita]

    print(f"Barcha tadbirlarda: {', '.join(barchada_tartibli)}")
    print(f"Faqat bitta tadbirda: {', '.join(faqat_bitta_tartibli)}")
    print(f"Kamida ikkita tadbirda: {', '.join(kamida_ikkita_tartibli)}")


if __name__ == "__main__":
    tadbir_1 = {"Ali", "Vali", "Sami", "Lola"}
    tadbir_2 = {"Ali", "Sami", "Nodir"}
    tadbir_3 = {"Ali", "Lola", "Nodir"}

    tadbirlarni_tahlil_qil(tadbir_1, tadbir_2, tadbir_3)
