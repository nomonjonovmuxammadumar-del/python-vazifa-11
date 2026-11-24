import csv
import os
import sys


def talabalarni_filtrla(
    kirish_fayli: str = "talabalar.csv",
    chiqish_fayli: str = "filtrlangan_talabalar.csv",
    yonalish: str = None
):
    if not os.path.exists(kirish_fayli):
        print(f"Xatolik: {kirish_fayli} topilmadi.")
        return

    if yonalish is None:
        yonalish = input("Yo'nalish: ").strip()

    tanlangan_talabalar = []

    with open(kirish_fayli, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["yonalish"].strip().lower() == yonalish.strip().lower():
                tanlangan_talabalar.append({
                    "ism": row["ism"].strip(),
                    "yosh": row["yosh"].strip(),
                    "yonalish": row["yonalish"].strip(),
                    "ball": int(row["ball"].strip())
                })

    saralangan = sorted(tanlangan_talabalar, key=lambda x: x["ball"], reverse=True)

    with open(chiqish_fayli, mode="w", newline="", encoding="utf-8") as f:
        fieldnames = ["ism", "yosh", "yonalish", "ball"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in saralangan:
            writer.writerow(item)

    print(f"\n{len(saralangan)} ta talaba topildi.")
    print(f"Natijalar {chiqish_fayli} fayliga yozildi.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        tanlov = sys.argv[1]
    else:
        tanlov = "Python"
        print(f"Yo'nalish: {tanlov}")
    talabalarni_filtrla(yonalish=tanlov)
