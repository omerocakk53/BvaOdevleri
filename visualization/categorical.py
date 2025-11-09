import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_avg_humidity_by_city(df, save_path):
    # Bu fonksiyon her şehrin ortalama nem oranını bir bar chart ile gösterir
    
    print(f"Grafik oluşturuluyor: Şehir Bazlı Ortalama Nem Oranı")
    
    # Şehirlere göre ortalama nemi hesapla
    city_humidity = df.groupby('City')['Humidity_pct'].mean().reset_index()
    
    # Daha iyi görselleştirme için nem oranına göre büyükten küçüğe sırala
    city_humidity = city_humidity.sort_values(by='Humidity_pct', ascending=False)
    
    plt.figure(figsize=(12, 8)) # (Genişlik, Yükseklik)
    
    # Seaborn ile yatay bar plot (y='City' olması isimlerin okunmasını kolaylaştırır)
    sns.barplot(x='Humidity_pct', y='City', data=city_humidity, palette='Blues_d')
    
    plt.title('Şehir Bazlı Ortalama Nem Oranları (%)')
    plt.xlabel('Ortalama Nem (%)')
    plt.ylabel('Şehir')
    
    # Etiketlerin grafiğe sığmasını sağla
    plt.tight_layout()
    
    # Grafiği kaydet
    plt.savefig(save_path)
    plt.close()
    print(f"Grafik kaydedildi: {save_path}")