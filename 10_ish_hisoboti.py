import os


def ish_hisoboti(fayl_nomi: str = "ish_vaqti.txt"):
    if not os.path.exists(fayl_nomi):
        print(f"Xatolik: {fayl_nomi} topilmadi.")
        return

    jami_soat = 0
    eng_kop_xodim = None
    maks_soat = -1

    with open(fayl_nomi, "r", encoding="utf-8") as f:
        for qator in f:
            qator = qator.strip()
            if not qator:
                continue

            qismlar = qator.split(maxsplit=1)
            if len(qismlar) < 2:
                continue

            ism, soat_str = qismlar[0], qismlar[1]

            try:
                soat = int(soat_str)
                jami_soat += soat
                if soat > maks_soat:
                    maks_soat = soat
                    eng_kop_xodim = (ism, soat)
            except ValueError:
                print(f"Ogohlantirish: {ism} uchun soat qiymati noto'g'ri.")

    print(f"Jami ish soati: {jami_soat}")
    if eng_kop_xodim:
        print(f"Eng ko'p ishlagan: {eng_kop_xodim[0]} - {eng_kop_xodim[1]} soat")


if __name__ == "__main__":
    ish_hisoboti("ish_vaqti.txt")
