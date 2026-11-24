import csv
import os
from collections import defaultdict


def savdo_tahlili(fayl_nomi: str = "savdo.csv"):
    if not os.path.exists(fayl_nomi):
        print(f"Xatolik: {fayl_nomi} topilmadi.")
        return

    kategoriya_daromad = defaultdict(int)

    with open(fayl_nomi, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            kategoriya = row["kategoriya"].strip()
            narx = int(row["narx"].strip())
            miqdor = int(row["miqdor"].strip())
            tushum = narx * miqdor
            kategoriya_daromad[kategoriya] += tushum

    for kategoriya, jami in kategoriya_daromad.items():
        formatlangan = f"{jami:,}".replace(",", " ")
        print(f"{kategoriya}: {formatlangan} so'm")

    if kategoriya_daromad:
        eng_daromadli = max(kategoriya_daromad, key=kategoriya_daromad.get)
        print(f"Eng daromadli kategoriya: {eng_daromadli}")


if __name__ == "__main__":
    savdo_tahlili("savdo.csv")
