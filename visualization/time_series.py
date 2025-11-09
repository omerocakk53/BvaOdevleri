import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_temperature_over_time(df, save_path):
    # Bu fonksiyon Türkiye genelindeki ortalama sıcaklığın zamanla değişimini çizer
    
    print(f"Grafik oluşturuluyor: Sıcaklığın Zamana Göre Değişimi")
    
    # Tarih sütununu tekrar datetime'a çevirelim (CSV'den okununca object olabilir)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Tüm şehirlerin günlük ortalama sıcaklığını al
    daily_avg_temp = df.groupby('Date')['Temperature_C'].mean().reset_index()
    
    # Tarihe göre sırala
    daily_avg_temp = daily_avg_temp.sort_values(by='Date')
    
    plt.figure(figsize=(15, 7))
    plt.plot(daily_avg_temp['Date'], daily_avg_temp['Temperature_C'], label='Günlük Ortalama Sıcaklık')
    
    # Trendi görmek için 30 günlük hareketli ortalama (rolling mean) ekleyelim
    daily_avg_temp['30_Day_MA'] = daily_avg_temp['Temperature_C'].rolling(window=30).mean()
    plt.plot(daily_avg_temp['Date'], daily_avg_temp['30_Day_MA'], color='red', label='30 Günlük Hareketli Ortalama')
    
    plt.title('Türkiye Geneli Günlük Ortalama Sıcaklık Değişimi')
    plt.xlabel('Tarih')
    plt.ylabel('Ortalama Sıcaklık (°C)')
    plt.legend()
    plt.grid(True)
    
    # Grafiği kaydet
    plt.savefig(save_path)
    plt.close() # Grafiği kapat (hafıza için önemli)
    print(f"Grafik kaydedildi: {save_path}")