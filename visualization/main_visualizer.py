import os
import pandas as pd

# Diğer modüllerimizdeki fonksiyonları import et
from visualization.time_series import plot_temperature_over_time
from visualization.categorical import plot_avg_humidity_by_city
from visualization.distribution import plot_precipitation_histogram

def generate_all_visualizations(df, output_dir='plots'):
    # Bu fonksiyon tüm grafikleri oluşturur ve 'plots' dizinine kaydeder
    
    # output_dir (plots/ dizini) yoksa oluştur
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Dizin oluşturuldu: {output_dir}")
        
    print("\n" + "="*50)
    print("--- GÖRSELLEŞTİRME AŞAMASI BAŞLADI ---")
    print("="*50 + "\n")
    
    # --- Grafik 1 ---
    plot_1_path = os.path.join(output_dir, '1_temperature_over_time.png')
    plot_temperature_over_time(df, plot_1_path)
    
    # --- Grafik 2 ---
    plot_2_path = os.path.join(output_dir, '2_avg_humidity_by_city.png')
    plot_avg_humidity_by_city(df, plot_2_path)
    
    # --- Grafik 3 ---
    plot_3_path = os.path.join(output_dir, '3_precipitation_histogram.png')
    plot_precipitation_histogram(df, plot_3_path)
    
    print("\n--- GÖRSELLEŞTİRME TAMAMLANDI ---")
    print(f"Tüm grafikler '{output_dir}' dizinine kaydedildi.")