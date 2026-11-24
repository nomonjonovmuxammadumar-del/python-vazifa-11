# python-vazifa-11

# Python Foundation — 3-oy: Takrorlash uchun 15 ta amaliy topshiriq

Ushbu repository **Python Foundation** kursi 3-oy yakuniy takrorlash amaliy topshiriqlarini o'z ichiga oladi. Loyihada ma'lumot tuzilmalari (string, list, tuple, dict, set), funksiyalar (*args, **kwargs, lambda, map, filter), istisnolarni boshqarish (try-except, assert), fayllar bilan ishlash (TXT, JSON, CSV), Matplotlib kutubxonasida vizuallashtirish hamda mini-loyiha ishlab chiqilgan.

---

## 📁 Loyiha tuzilmasi

```text
pyhton vazifa 11/
├── 01_matn_statistikasi.py        # 01. Matn tahlili va statistikasi
├── 02_yetkazib_berish.py           # 02. Yetkazib berish buyurtmalari tahlili
├── 03_sayoxat_yonalishlari.py      # 03. Shaharlar koordinatasi va masofa hisoblash
├── 04_ombordagi_mahsulotlar.py     # 04. Ikki ombor lug'atlarini birlashtirish
├── 05_tadbir_ishtirokchilari.py    # 05. To'plamlar (set) bo'yicha tahlil
├── 06_kafe_buyurtmalari.py         # 06. *args va **kwargs bilan kafe buyurtmasi
├── 07_reytinglarni_saralash.py     # 07. filter(), map() va lambda yordamida saralash
├── 08_fayl_nomlarini_tekshirish.py # 08. Fayl nomlari va kengaytmalarini tekshirish
├── 09_xatolarni_tuzatish.py        # 09. Istisnolarni boshqarish va assert
├── 10_ish_hisoboti.py              # 10. TXT fayldan ish vaqtini hisoblash
├── ish_vaqti.txt                   # 10-topshiriq uchun ma'lumot fayli
├── 11_json_konfiguratsiya.py       # 11. JSON sozlamalarini o'qish va yangilash
├── sozlamalar.json                 # 11-topshiriq uchun sozlamalar fayli
├── 12_csv_savdo_tahlili.py         # 12. CSV fayldan savdo tahlili
├── savdo.csv                       # 12-topshiriq uchun savdo ma'lumotlari
├── 13_csv_filtrlash.py             # 13. CSV ma'lumotlarini filtrlash va yozish
├── talabalar.csv                   # 13-topshiriq boshlang'ich ma'lumotlari
├── filtrlangan_talabalar.csv       # 13-topshiriq natijaviy fayli
├── 14_grafiklar_tahlil.py          # 14. Matplotlib grafiklari (Line, Bar, Hist)
├── grafiklar.png                   # 14-topshiriq chizmasi rasmi
├── 15_kutubxona_loyihasi.py        # 15-topshiriq: ildiz orqali ishga tushirish
├── 15_kutubxona/                   # 15-topshiriq: Mini-loyiha papkasi
│   ├── main.py                     # Mini-loyiha asosiy CLI menyusi
│   ├── kutubxona.py                # Barcha vazifalar funksiyalari moduli
│   ├── kitoblar.csv                # Kitoblar bazasi
│   └── README.md                   # Mini-loyiha yo'riqnomasi
├── .gitignore
└── README.md
```

---

## ⚙️ O'rnatish va talablar

Dasturlarni ishga tushirish uchun **Python 3.8+** va **matplotlib** kutubxonasi talab qilinadi:

```bash
pip install matplotlib
```

---

## 🚀 Topshiriqlarni ishga tushirish yo'riqnomasi

### 01. Matn statistikasi
Matndagi so'zlar soni, eng uzun so'z, eng ko'p uchragan harf va takrorlanmaydigan so'zlarni aniqlaydi.
```bash
python 01_matn_statistikasi.py
```

### 02. Yetkazib berish buyurtmalari
Har bir buyurtmaning narx va miqdorini hisoblab, eng qimmat buyurtmani topadi.
```bash
python 02_yetkazib_berish.py
```

### 03. Sayohat yo'nalishlari
Koordinatalar orasidagi masofani Evklid formulasi `√((x2-x1)² + (y2-y1)²)` yordamida hisoblaydi va eng uzoq juftlikni chiqaradi.
```bash
python 03_sayoxat_yonalishlari.py
```

### 04. Ombordagi mahsulotlar
Ikkita ombor lug'atini (dict) birlashtirib, bir xil mahsulotlar miqdorini jamlaydi.
```bash
python 04_ombordagi_mahsulotlar.py
```

### 05. Tadbir ishtirokchilari
To'plamlar (set) yordamida barcha tadbirlarda, faqat bittasida va kamida ikkitasida qatnashganlarni topadi.
```bash
python 05_tadbir_ishtirokchilari.py
```

### 06. Kafe buyurtmalari
Funksiyada `*args` (mahsulotlar) va `**kwargs` (mijoz ma'lumotlari) qabul qilinadi, noma'lum taomlar bo'yicha ogohlantirish beriladi.
```bash
python 06_kafe_buyurtmalari.py
```

### 07. Reytinglarni saralash
`filter()`, `map()` va `lambda` orqali 70 dan yuqorilarni saralash, 10% ball qo'shish va kamayish tartibida joylashtirish.
```bash
python 07_reytinglarni_saralash.py
```

### 08. Fayl nomlarini tekshirish
PDF, JPG va PNG kengaytmalarini tekshiradi, bo'sh joylarni `_` bilan almashtiradi, boshqa formatlarni yaroqsiz qilib ajratadi.
```bash
python 08_fayl_nomlarini_tekshirish.py
```

### 09. Xatolarni aniqlash va tuzatish (Exception Handling & Assert)
Nolga bo'lish va matn kiritilish xatoliklarini to'xtamasdan ushlaydi, `assert` tekshiruviga ega.
```bash
python 09_xatolarni_tuzatish.py
```

### 10. TXT fayldan ish hisoboti
`ish_vaqti.txt` faylini o'qiydi, noto'g'ri soat qiymatlarini ogohlantiradi va jami soat hamda eng ko'p ishlagan xodimni topadi.
```bash
python 10_ish_hisoboti.py
```

### 11. JSON konfiguratsiya
`sozlamalar.json` faylidan sozlamalarni o'qiydi, mavzu (light/dark) va bildirishnomani foydalanuvchi xohishiga qarab yangilab, faylga qayta yozadi.
```bash
python 11_json_konfiguratsiya.py
```

### 12. CSV savdo tahlili
`savdo.csv` faylidan kategoriyalar bo'yicha tushumni hisoblaydi va eng daromadlisini chiqaradi.
```bash
python 12_csv_savdo_tahlili.py
```

### 13. CSV ma'lumotlarini filtrlash
`talabalar.csv` faylidan tanlangan yo'nalish bo'yicha talabalarni saralab, `filtrlangan_talabalar.csv` yangi fayliga yozadi.
```bash
python 13_csv_filtrlash.py
```

### 14. Grafiklar orqali tahlil
Matplotlib yordamida chiziqli grafik (Line Chart), ustunli grafik (Bar Chart) va gistogramma (Histogram) chizadi hamda `grafiklar.png` fayliga saqlaydi.
```bash
python 14_grafiklar_tahlil.py
```

### 15. Mini-loyiha: Kutubxona statistikasi
Kitoblar bazasini boshqarish uchun to'liq interaktiv konsol ilovasi:
```bash
python 15_kutubxona_loyihasi.py
# yoki
cd 15_kutubxona
python main.py
```

Menyu imkoniyatlari:
1. Kitoblarni ko'rish (barcha ro'yxat)
2. Kitob qidirish (nomi bo'yicha)
3. Kategoriya bo'yicha filtrlash
4. Eng ko'p o'qilgan kitob
5. Grafik chiqarish (Bar Chart ko'rinishida `kategoriya_grafigi.png` ga saqlash)
6. Yangi kitob qo'shish (bir zumda CSV fayl yangilanadi)
0. Chiqish

---

## 📌 Muallif
Ushbu topshiriqlar to'plami Python Foundation dasturi talablariga to'liq mos keladi va har bir dastur mustaqil ravishda sinovdan o'tkazilgan.
