import json
import os
import sys


def sozlamalarni_yangila(fayl_nomi: str = "sozlamalar.json", mavzu: str = None, bildirishnoma: bool = None):
    if not os.path.exists(fayl_nomi):
        print(f"Xatolik: {fayl_nomi} topilmadi.")
        return

    with open(fayl_nomi, "r", encoding="utf-8") as f:
        sozlamalar = json.load(f)

    if mavzu is None:
        mavzu_kiritish = input("Mavzu (light/dark): ").strip().lower()
        mavzu = mavzu_kiritish if mavzu_kiritish else sozlamalar.get("mavzu", "light")

    if bildirishnoma is None:
        bild_kiritish = input("Bildirishnoma (ha/yo'q): ").strip().lower()
        bildirishnoma = bild_kiritish in ["ha", "yes", "true", "1"]

    sozlamalar["mavzu"] = mavzu
    sozlamalar["bildirishnoma"] = bildirishnoma

    with open(fayl_nomi, "w", encoding="utf-8") as f:
        json.dump(sozlamalar, f, indent=2, ensure_ascii=False)

    print("\nYangilangan fayl mazmuni:")
    print(json.dumps(sozlamalar, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) > 2:
        mavzu_arg = sys.argv[1]
        bild_arg = sys.argv[2].lower() in ["ha", "true", "1"]
        sozlamalarni_yangila("sozlamalar.json", mavzu_arg, bild_arg)
    else:
        sozlamalarni_yangila("sozlamalar.json")
