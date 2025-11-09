import pandas as pd
from analysis.central_tendency import get_central_tendency
from analysis.dispersion import get_dispersion

def generate_full_report(df):
    
    # Analiz Kontrol Yöneticisi

    print("\n--- TANIMLAYICI İSTATİSTİKLER RAPORU BAŞLADI ---")
    print("="*50 + "\n")
    
    numeric_cols = ['Temperature_C', 'Humidity_pct', 'WindSpeed_kmh', 'Precipitation_mm']
    
    cols_exist = all(col in df.columns for col in numeric_cols)
    if not cols_exist:
        print(f"Hata: İstatistik için gerekli sütunlar bulunamadı: {numeric_cols}")
        return

    # 1. Merkezi Eğilim Raporu
    # get_central_tendency() fonksiyonundan DataFrame'i al
    tendency_report = get_central_tendency(df, numeric_cols)
    # DataFrame'i .to_string() ile YAZDIR (float_format kullanarak)
    print(tendency_report.to_string(float_format='{:.2f}'.format))
    print("\n")

    # 2. Dağılım Raporu
    # get_dispersion() fonksiyonundan DataFrame'i al
    dispersion_report = get_dispersion(df, numeric_cols)
    # DataFrame'i .to_string() ile YAZDIR
    print(dispersion_report.to_string(float_format='{:.2f}'.format))
    print("\n")    
    print("\n--- İSTATİSTİK RAPORU TAMAMLANDI ---")