# 🌦️ Weather Data Analysis Project

Bu proje, **Veri Bilimine Giriş** dersi kapsamında hazırlanmış bir veri analizi çalışmasıdır.  
Amaç, Türkiye'deki farklı şehirlerden toplanan hava durumu verilerini temizlemek, analiz etmek ve görselleştirmektir.

---

## 📁 Proje Yapısı

```
├── data/
│   └── weather_dataset_1000.csv        # Ham veri seti
│
├── scripts/
│   ├── main.py                         # Ana çalıştırılabilir betik
│   ├── categorical_cleaner.py          # Kategorik veri temizleme modülü
│   ├── outlier_handler.py              # Aykırı değer tespiti ve düzeltme modülü
│   ├── duplicate_handler.py            # Tekrarlayan kayıtları temizleme modülü
│   └── missing_value_handler.py        # Eksik değer doldurma modülü
│
├── analysis/
│   └── statistics_summary.csv          # Analiz sonuçlarının özet dosyası
│
├── plots/
│   ├── temperature_trend.png           # Zaman serisi grafiği
│   ├── humidity_by_city.png            # Şehirlere göre nem oranı grafiği
│   └── precipitation_histogram.png     # Yağış miktarı histogramı
│
├── report/
│   └── Veri_Bilimine_Giris_Raporu_Omer_Ocak.docx  # Rapor dosyası
│
└── README.md
```

---

## ⚙️ Kurulum ve Çalıştırma

### 1️⃣ Gerekli Kütüphaneleri Kur
```bash
pip install pandas numpy matplotlib seaborn
```

### 2️⃣ Ana Betiği Çalıştır
```bash
python scripts/main.py
```

### 3️⃣ Sonuçlar
- Temizlenmiş veri `cleaned_data.csv` olarak oluşturulur.  
- İstatistiksel özetler `analysis/` klasöründe kaydedilir.  
- Görseller `plots/` klasöründe oluşturulur.  
- Rapor dosyası `report/` klasöründedir.

---

## 🧠 Analiz Özeti

- Ortalama sıcaklık: **15.32°C**  
- Ortalama nem: **%65.39**  
- Yağışların büyük kısmı **0–2 mm** aralığındadır.  
- Antalya en yüksek, İzmir en düşük nem oranına sahiptir.

---

## 🧩 Kullanılan Teknolojiler

- **Python 3.11+**
- **pandas** – veri işleme  
- **numpy** – istatistiksel hesaplamalar  
- **matplotlib / seaborn** – görselleştirme  

---

## 📄 Rapor

Tüm sürecin detaylı anlatımı için:  
📘 `report/Veri_Bilimine_Giris_Raporu_Omer_Ocak.docx`

---

## 👨‍💻 Yazar

**Ömer Ocak**  
Veri Bilimine Giriş – Ara Sınav Ödevi  
2025

---

## 🧾 Lisans

Bu proje yalnızca eğitim amacıyla hazırlanmıştır. Ticari kullanımlar için izin alınmalıdır.
