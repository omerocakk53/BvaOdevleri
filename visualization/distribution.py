import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_precipitation_histogram(df, save_path):
    # Bu fonksiyon yağış miktarının dağılımını (histogram) gösterir
    
    print(f"Grafik oluşturuluyor: Yağış Miktarı Histogramı")
    
    # Verinin çoğu '0' yağış olduğu için, sadece yağış olan günlere bakmak
    # dağılımı daha iyi gösterir
    rained_days = df[df['Precipitation_mm'] > 0]
    
    plt.figure(figsize=(10, 6))
    
    # Seaborn histogram (KDE=True dağılım eğrisini çizer)
    sns.histplot(rained_days['Precipitation_mm'], bins=30, kde=True)
    
    plt.title('Yağış Miktarı Dağılımı (Sadece Yağış Olan Günler)')
    plt.xlabel('Yağış Miktarı (mm)')
    plt.ylabel('Gün Sayısı (Frekans)')
    
    # Grafiği kaydet
    plt.savefig(save_path)
    plt.close()
    print(f"Grafik kaydedildi: {save_path}")