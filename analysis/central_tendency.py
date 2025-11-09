import pandas as pd

def calculate_mean(df, numeric_cols):
    # Verilen sütunların ortalamalarını hesaplıyor
    return df[numeric_cols].mean()

def calculate_median(df, numeric_cols):
    # Verilen sütunların medyanını hesaplıyor
    return df[numeric_cols].median()

def calculate_mode(df, numeric_cols):
    # Verilen sütunların modunu hesaplıyor en sık görülen değeri buluyor
    # Mod birden fazla olabiliyor, biz ilkini alıyoruz
    return df[numeric_cols].mode().iloc[0]

def get_central_tendency(df, numeric_cols):
    # Tüm merkezi eğilim ölçülerini bir DataFrame'de birleştiriyoruz
    print("--- Merkezi Eğilim Ölçüleri Hesaplanıyor ---")
    
    tendency_df = pd.DataFrame(index=numeric_cols)
    tendency_df['Ortalama (Mean)'] = calculate_mean(df, numeric_cols)
    tendency_df['Medyan (Median)'] = calculate_median(df, numeric_cols)
    tendency_df['Mod (Mode)'] = calculate_mode(df, numeric_cols)
    
    return tendency_df