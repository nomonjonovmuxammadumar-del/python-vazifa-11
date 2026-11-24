# Kutubxona statistikasi — Mini loyiha (15-topshiriq)

Ushbu loyiha kitoblar bazasini (`kitoblar.csv`) boshqarish, tahlil qilish va vizuallashtirish uchun mo'ljallangan CLI dasturidir.

## Imkoniyatlar
1. **Kitoblarni ko'rish**: Barcha mavjud kitoblar ro'yxatini jadval ko'rinishida chiqarish.
2. **Kitob qidirish**: Kitob nomi bo'yicha tezkor qidiruv.
3. **Kategoriya bo'yicha filtrlash**: Tanlangan yo'nalishdagi (masalan, Dasturlash, Tarix, Ilm-fan) kitoblarni saralab ko'rsatish.
4. **Eng ko'p o'qilgan kitob**: O'qilishlar soni eng yuqori bo'lgan kitobni aniqlash.
5. **Grafik chiqarish**: Matplotlib yordamida kategoriyalar bo'yicha o'qilganlik diagrammasini (Bar Chart) chizish va `kategoriya_grafigi.png` fayliga saqlash.
6. **Kitob qo'shish**: Yangi kitob ma'lumotlarini kiritish va `kitoblar.csv` faylini bir zumda yangilash.

## Dastur arxitekturasi
- `main.py` — Foydalanuvchi menyusi va konsol boshqaruvi.
- `kutubxona.py` — Barcha funksiyalarni o'zida jamlagan asosiy mantiq moduli.
- `kitoblar.csv` — Kitoblar haqidagi ma'lumotlar saqlanadigan ma'lumotlar bazasi.

## Ishga tushirish
```bash
python main.py
```
Yoki topshiriq namunasini sinash uchun:
```bash
python main.py 4
```
