import numpy as np

def fill_missing_values(df):
    # Eksik verileri mantıklı yöntemlerle doldurur
    
    print("Eksik veriler (NaN) dolduruluyor...")
    
    # 1. Enterpolasyon için veriyi sıralamak şarttır
    # Önce Şehir, sonra Tarih'e göre sırala
    df = df.sort_values(by=['City', 'Date'])
    
    # 2. groupby('Şehir') ile her şehrin kendi zaman serisi üzerinde enterpolasyon yapıyoruz
    # 'transform' orijinal DataFrame'in index'ini korur
    cols_to_interpolate = ['Temperature_C', 'Humidity_pct', 'WindSpeed_kmh']
    for col in cols_to_interpolate:
        df[col] = df.groupby('City')[col].transform(lambda x: x.interpolate(method='linear'))

    # 3. Yağış: Boşluklar (NaN) '0' (sıfır) yağış anlamına gelir
    df['Precipitation_mm'] = df['Precipitation_mm'].fillna(0)
    
    # 4. Weather: boş alanları sil
    df = df.dropna(subset=['Weather'])

    # RecordID alanını ekle ilk sütuna
    df.insert(0, 'RecordID', np.arange(1, len(df) + 1))
    
    # 5. HALA NaN kaldıysa (örn. bir şehrin ilk verisi NaN ise enterpolasyon çalışmaz)
    # Bu son kalanları sütun ortalaması ile doldur
    for col in cols_to_interpolate:
        df[col] = df[col].fillna(df[col].mean())
        
    return df