import pandas as pd

def convert_data_types(df):
    # Veri tiplerini dönüştüren ana fonksiyon
    
    # 1. Tarih Sütunu (Sütun adının 'Tarih' olduğunu varsayıyoruz)
    # 'errors='coerce'' hatalı tarih formatlarını NaT (Not a Time) yapar
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # 2. Sayısal Sütunlar
    # (Sütun adlarının bunlar olduğunu varsayıyoruz)
    numeric_cols = ['Temperature_C', 'Humidity_pct', 'WindSpeed_kmh', 'Precipitation_mm']
    
    for col in numeric_cols:
        # 'errors='coerce'' sayıya dönüşemeyen değerleri (örn. '15 C') NaN yapar
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
    print("Veri tipleri dönüştürüldü (Tarih -> datetime, Sayısallar -> numeric).")
    return df