def reytinglarni_qayta_ishlash(natijalar: list):
    yuqori_70 = list(filter(lambda x: x["ball"] > 70, natijalar))
    yuqori_ismlar = [x["ism"] for x in yuqori_70]
    print(f"70 dan yuqori: {', '.join(yuqori_ismlar)}")

    oshirilgan_ballar = list(map(lambda x: round(x["ball"] * 1.1, 1), natijalar))
    print(f"10% oshirilgan ballar: {oshirilgan_ballar}")

    saralangan = sorted(natijalar, key=lambda x: x["ball"], reverse=True)
    saralangan_ismlar = [x["ism"] for x in saralangan]
    print(f"Saralangan: {', '.join(saralangan_ismlar)}")


if __name__ == "__main__":
    natijalar = [
        {"ism": "Aziza", "ball": 82},
        {"ism": "Jasur", "ball": 64},
        {"ism": "Madina", "ball": 91},
        {"ism": "Sardor", "ball": 70}
    ]
    reytinglarni_qayta_ishlash(natijalar)
