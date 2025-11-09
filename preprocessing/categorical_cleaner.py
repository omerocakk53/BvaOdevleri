import numpy as np

def clean_categorical_data(df):
    # sütunları temizleyen ana fonksiyon
    df = _clean_city_names(df)
    df = _categorize_weather_conditions(df)
    print("veriler temizlendi (Şehir ve Weather ).")
    return df

def _clean_city_names(df):
    # Şehir isimlerindeki temel hataları düzeltir
    # Boşlukları temizle ve baş harfleri büyük yap
    df['City'] = df['City'].str.strip().str.title()
    # Yaygın yazım hatalarını düzelt
    corrections = {
        'Izmir': 'İzmir',
        'Istanbul': 'İstanbul',
        'Ankra': 'Ankara',
        'Izmr': 'İzmir',
    }
    df['City'] = df['City'].replace(corrections)
    return df

def _categorize_weather_conditions(df):
    # Önce küçük harf ve boşluk temizliği
    df['Weather'] = df['Weather'].str.strip().str.lower()
    # boş değerli satırı kaldırma
    df = df.dropna(subset=['Weather'])
    return df