import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from kutubxona import (
    kitoblarni_korish,
    kitob_qidirish,
    kategoriya_boyicha_filtr,
    eng_kop_oqilgan_kitob,
    kategoriya_grafigi,
    kitob_qoshish
)


def menyu():
    print("\n" + "=" * 35)
    print("      KUTUBXONA STATISTIKASI")
    print("=" * 35)
    print("1. Kitoblarni ko'rish")
    print("2. Kitob qidirish")
    print("3. Kategoriya bo'yicha filtrlash")
    print("4. Eng ko'p o'qilgan kitob")
    print("5. Grafik chiqarish")
    print("6. Kitob qo'shish")
    print("0. Chiqish")
    print("=" * 35)


def main():
    fayl = "kitoblar.csv"

    if len(sys.argv) > 1:
        tanlov = sys.argv[1].strip()
        print(f"Tanlov: {tanlov}")
        if tanlov == "1":
            kitoblarni_korish(fayl)
        elif tanlov == "2":
            qidiruv = sys.argv[2] if len(sys.argv) > 2 else "Python"
            kitob_qidirish(fayl, qidiruv)
        elif tanlov == "3":
            kat = sys.argv[2] if len(sys.argv) > 2 else "Dasturlash"
            kategoriya_boyicha_filtr(fayl, kat)
        elif tanlov == "4":
            eng_kop_oqilgan_kitob(fayl)
        elif tanlov == "5":
            kategoriya_grafigi(fayl)
        elif tanlov == "6":
            kitob_qoshish(fayl)
        return

    while True:
        menyu()
        tanlov = input("Tanlov: ").strip()

        if tanlov == "1":
            kitoblarni_korish(fayl)
        elif tanlov == "2":
            kitob_qidirish(fayl)
        elif tanlov == "3":
            kategoriya_boyicha_filtr(fayl)
        elif tanlov == "4":
            eng_kop_oqilgan_kitob(fayl)
        elif tanlov == "5":
            kategoriya_grafigi(fayl)
        elif tanlov == "6":
            kitob_qoshish(fayl)
        elif tanlov in ["0", "exit", "chiqish", "q"]:
            print("Dastur yakunlandi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov! Qayta urinib ko'ring.")


if __name__ == "__main__":
    main()
