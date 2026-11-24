def bolish(a: float, b: float) -> float:
    assert b != 0, "Nolga bo'lish mumkin emas."
    return a / b


def hisoblash_oqimi(son1_matn: str, son2_matn: str):
    try:
        a = float(son1_matn)
        b = float(son2_matn)
        natija = bolish(a, b)
        print("Natija:", natija)
    except ValueError:
        print("Xatolik: Faqat son kiritish lozim, matn kiritildi.")
    except (ZeroDivisionError, AssertionError) as e:
        print(f"Xatolik: {e}")
    finally:
        print("Dastur ishlashda davom etmoqda.")


if __name__ == "__main__":
    print("--- 1-sinov (Namuna: 20 / 0) ---")
    hisoblash_oqimi("20", "0")

    print("\n--- 2-sinov (Matn kiritilganda) ---")
    hisoblash_oqimi("salom", "5")

    print("\n--- 3-sinov (To'g'ri bo'linish) ---")
    hisoblash_oqimi("20", "4")
