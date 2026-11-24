import os


def fayllarni_tekshir(fayllar: list):
    yaroqli_kengaytmalar = {".pdf", ".jpg", ".png"}

    yaroqli = []
    yaroqsiz = []

    for fayl in fayllar:
        _, ext = os.path.splitext(fayl)
        if ext.lower() in yaroqli_kengaytmalar:
            tozalangan_nom = fayl.replace(" ", "_")
            yaroqli.append(tozalangan_nom)
        else:
            yaroqsiz.append(fayl)

    print("Yaroqli:")
    for f in yaroqli:
        print(f)

    print("\nYaroqsiz:")
    for f in yaroqsiz:
        print(f)

    return yaroqli, yaroqsiz


if __name__ == "__main__":
    fayllar = [
        "Hisobot 2026.pdf",
        "profil rasmi.jpg",
        "video.mp4",
        "jadval.xlsx",
        "diagramma.png"
    ]
    fayllarni_tekshir(fayllar)
