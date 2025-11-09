import numpy as np

def handle_outliers(df):
    # Alan bilgisine dayalı absürt (imkansız) değerleri yönetir
    # Bu değerleri NaN (boş) olarak işaretleyeceğiz ki sonra doldurulsunlar
    
    print("Aykırı değerler (outliers) yönetiliyor...")
    
    # 1. Sıcaklık: -40 / +55 derece aralığı dışındakiler
    df.loc[(df['Temperature_C'] > 55) | (df['Temperature_C'] < -40), 'Temperature_C'] = np.nan
    
    # 2. Nem: 0-100 aralığı dışındakiler
    df.loc[(df['Humidity_pct'] > 100) | (df['Humidity_pct'] < 0), 'Humidity_pct'] = np.nan
    
    # 3. Yağış Miktarı: Negatif olamaz
    # Bunu 0 yapmak, NaN yapmaktan daha mantıklıdır
    df.loc[df['Precipitation_mm'] < 0, 'Precipitation_mm'] = np.nan
    
    # 4. Rüzgar Hızı: 200 km/s üzeri
    df.loc[df['WindSpeed_kmh'] >= 200, 'WindSpeed_kmh'] = np.nan
    return df