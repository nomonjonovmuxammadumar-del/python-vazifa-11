def buyurtmalarni_hisobla(buyurtmalar: list):
    eng_qimmat_buyurtma = None
    maks_qiymat = -1

    for b in buyurtmalar:
        mahsulot = b["mahsulot"]
        narx = b["narx"]
        miqdor = b["miqdor"]
        qiymat = narx * miqdor
        print(f"{mahsulot}: {qiymat} so'm")

        if qiymat > maks_qiymat:
            maks_qiymat = qiymat
            eng_qimmat_buyurtma = (mahsulot, qiymat)

    if eng_qimmat_buyurtma:
        print(f"Eng qimmat buyurtma: {eng_qimmat_buyurtma[0]} - {eng_qimmat_buyurtma[1]} so'm")


if __name__ == "__main__":
    buyurtmalar = [
        {"mahsulot": "Kitob", "narx": 45000, "miqdor": 2},
        {"mahsulot": "Ruchka", "narx": 5000, "miqdor": 10},
        {"mahsulot": "Sumka", "narx": 180000, "miqdor": 1}
    ]
    buyurtmalarni_hisobla(buyurtmalar)
