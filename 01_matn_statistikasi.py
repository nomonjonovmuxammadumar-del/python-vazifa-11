import re
from collections import Counter


def matn_statistikasi(matn: str):
    sozlar = re.findall(r"\b\w+\b", matn.lower())
    sozlar_soni = len(sozlar)
    eng_uzun_soz = max(sozlar, key=len) if sozlar else ""
    harflar = [belgi.lower() for belgi in matn if belgi.isalpha()]
    harf_sanoq = Counter(harflar)
    eng_kop_harf = harf_sanoq.most_common(1)[0][0] if harf_sanoq else ""
    soz_sanoq = Counter(sozlar)
    takrorlanmaydigan = [soz for soz in sozlar if soz_sanoq[soz] == 1]
    
    return {
        "sozlar_soni": sozlar_soni,
        "eng_uzun_soz": eng_uzun_soz,
        "eng_kop_harf": eng_kop_harf,
        "takrorlanmaydigan": takrorlanmaydigan
    }


if __name__ == "__main__":
    matn = "Python dasturlash qiziqarli. Python imkoniyatlari keng."
    natija = matn_statistikasi(matn)

    print(f"So'zlar soni: {natija['sozlar_soni']}")
    print(f"Eng uzun so'z: {natija['eng_uzun_soz']}")
    print(f"Eng ko'p uchragan harf: {natija['eng_kop_harf']}")
    print(f"Takrorlanmaydigan so'zlar: {', '.join(natija['takrorlanmaydigan'])}")
