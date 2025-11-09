import numpy as np

def handle_duplicates(df):
    # Kopyaları yöneten ana fonksiyon

    # 1. Adım: Birebir aynı olan satırları sil
    df = df.drop_duplicates()
    print(f"Birebir kopyalar silindi. Kalan satır: {len(df)}")
    
    # 2. Adım: 'Tarih' ve 'Şehir' bazında grupla ve veriyi özetle
    # Bu, aynı gün/şehire ait birden fazla kaydı (farklı bile olsalar) tek satıra indirir
    # 'agg' fonksiyonu ile her sütuna ayrı kural tanımlıyoruz
    df_agg = df.groupby(['Date', 'City']).agg(
        # Sayısal: Ortalama
        Temperature_C=('Temperature_C', 'mean'),
        Humidity_pct=('Humidity_pct', 'mean'),
        WindSpeed_kmh=('WindSpeed_kmh', 'mean'),
        # Yağış: Toplam
        Precipitation_mm=('Precipitation_mm', 'sum'),
        # Kategorik: O gün için kaydedilen ilk kategoriyi al
        Weather=('Weather', 'first')
    ).reset_index() # reset_index() gruplanan sütunları (Tarih, Şehir) tekrar normal sütun yapar
   
    print(f"Veri 'Tarih' ve 'Şehir' bazında gruplandı. Kalan satır: {len(df_agg)}")
    return df_agg