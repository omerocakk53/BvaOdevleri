def save_data(df, filepath):
    # Temizlenmiş DataFrame'i yeni bir CSV dosyasına kaydeder
    print(f"Temizlenmiş veri kaydediliyor: {filepath}")
    df.to_csv(filepath, index=False)
    print(f"Temizlenmiş veri kaydedildi: {filepath}")