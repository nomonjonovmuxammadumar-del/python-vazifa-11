import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt


def get_csv_path(fayl_nomi: str = "kitoblar.csv") -> str:
    if os.path.exists(fayl_nomi):
        return fayl_nomi
    local_path = os.path.join(os.path.dirname(__file__), fayl_nomi)
    if os.path.exists(local_path):
        return local_path
    return fayl_nomi


def kitoblarni_oqish(fayl_nomi: str = "kitoblar.csv") -> list:
    path = get_csv_path(fayl_nomi)
    if not os.path.exists(path):
        return []

    kitoblar = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            kitoblar.append({
                "nom": row["nom"].strip(),
                "kategoriya": row["kategoriya"].strip(),
                "muallif": row["muallif"].strip(),
                "oqilgan": int(row["oqilgan"].strip())
            })
    return kitoblar


def kitoblarni_korish(fayl_nomi: str = "kitoblar.csv"):
    kitoblar = kitoblarni_oqish(fayl_nomi)
    if not kitoblar:
        print("Kutubxonada hech qanday kitob topilmadi.")
        return

    print("\n--- BARCHA KITOBLAR ---")
    print(f"{'№':<3} | {'Nom':<20} | {'Kategoriya':<15} | {'Muallif':<12} | {'O‘qilgan'}")
    print("-" * 65)
    for i, k in enumerate(kitoblar, 1):
        print(f"{i:<3} | {k['nom']:<20} | {k['kategoriya']:<15} | {k['muallif']:<12} | {k['oqilgan']} marta")
    print("-" * 65)


def kitob_qidirish(fayl_nomi: str = "kitoblar.csv", qidiruv: str = None):
    if qidiruv is None:
        qidiruv = input("Qidirilayotgan kitob nomini kiriting: ").strip()

    kitoblar = kitoblarni_oqish(fayl_nomi)
    topilganlar = [k for k in kitoblar if qidiruv.lower() in k["nom"].lower()]

    if topilganlar:
        print(f"\nTopilgan kitoblar ({len(topilganlar)} ta):")
        for k in topilganlar:
            print(f"- {k['nom']} ({k['muallif']}) | Kategoriya: {k['kategoriya']} | O'qilgan: {k['oqilgan']} marta")
    else:
        print(f"'{qidiruv}' nomli kitob topilmadi.")


def kategoriya_boyicha_filtr(fayl_nomi: str = "kitoblar.csv", kategoriya: str = None):
    if kategoriya is None:
        kategoriya = input("Kategoriyani kiriting: ").strip()

    kitoblar = kitoblarni_oqish(fayl_nomi)
    filtrlar = [k for k in kitoblar if k["kategoriya"].lower() == kategoriya.lower()]

    if filtrlar:
        print(f"\n'{kategoriya}' kategoriyasidagi kitoblar ({len(filtrlar)} ta):")
        for k in filtrlar:
            print(f"- {k['nom']} ({k['muallif']}) | O'qilgan: {k['oqilgan']} marta")
    else:
        print(f"'{kategoriya}' kategoriyasida kitoblar mavjud emas.")


def eng_kop_oqilgan_kitob(fayl_nomi: str = "kitoblar.csv"):
    kitoblar = kitoblarni_oqish(fayl_nomi)
    if not kitoblar:
        print("Kutubxona bo'sh.")
        return

    eng_kop = max(kitoblar, key=lambda x: x["oqilgan"])
    print("\nEng ko'p o'qilgan kitob:")
    print(f"{eng_kop['nom']} - {eng_kop['oqilgan']} marta")


def kategoriya_grafigi(fayl_nomi: str = "kitoblar.csv", rasm_fayl: str = "kategoriya_grafigi.png"):
    kitoblar = kitoblarni_oqish(fayl_nomi)
    if not kitoblar:
        print("Grafik chizish uchun ma'lumot yetarli emas.")
        return

    kat_oqilgan = defaultdict(int)
    for k in kitoblar:
        kat_oqilgan[k["kategoriya"]] += k["oqilgan"]

    kategoriyalar = list(kat_oqilgan.keys())
    oqilishlar = list(kat_oqilgan.values())

    plt.figure(figsize=(8, 5))
    bars = plt.bar(kategoriyalar, oqilishlar, color=["#3498db", "#9b59b6", "#e67e22", "#2ecc71"], edgecolor="black")
    plt.title("Kategoriyalar bo'yicha kitobxonlik statistikasi", fontsize=14, fontweight="bold")
    plt.xlabel("Kategoriyalar", fontsize=11)
    plt.ylabel("Jami o'qilishlar soni", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    for bar in bars:
        balandlik = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, balandlik + 0.5, f"{int(balandlik)}", ha="center", va="bottom")

    plt.tight_layout()
    plt.savefig(rasm_fayl, dpi=300)
    print(f"Kategoriya grafigi '{rasm_fayl}' fayliga saqlandi.")
    try:
        plt.show()
    except Exception:
        pass


def kitob_qoshish(
    fayl_nomi: str = "kitoblar.csv",
    nom: str = None,
    kategoriya: str = None,
    muallif: str = None,
    oqilgan: int = None
):
    path = get_csv_path(fayl_nomi)

    if nom is None:
        nom = input("Kitob nomi: ").strip()
    if kategoriya is None:
        kategoriya = input("Kategoriya: ").strip()
    if muallif is None:
        muallif = input("Muallif: ").strip()
    if oqilgan is None:
        while True:
            try:
                oqilgan = int(input("O'qilgan soni: ").strip())
                break
            except ValueError:
                print("Iltimos, musbat butun son kiriting.")

    fayl_mavjud = os.path.exists(path)

    with open(path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not fayl_mavjud:
            writer.writerow(["nom", "kategoriya", "muallif", "oqilgan"])
        writer.writerow([nom, kategoriya, muallif, oqilgan])

    print(f"'{nom}' kitobi muvaffaqiyatli saqlandi va CSV fayl yangilandi!")
