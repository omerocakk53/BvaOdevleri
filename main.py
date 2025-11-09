import pandas as pd
import os

# --- BÖLÜM 1: TEMİZLEME (PREPROCESSING) İMPORTLARI ---
from script.read_csv_file import reading  # Kendi 'reading' fonksiyonun
from script.save_data import save_data      # Kendi 'save_data' fonksiyonun
from preprocessing.type_converter import convert_data_types
from preprocessing.categorical_cleaner import clean_categorical_data
from preprocessing.outlier_handler import handle_outliers
from preprocessing.duplicate_handler import handle_duplicates
from preprocessing.missing_value_handler import fill_missing_values

# --- BÖLÜM 2: ANALİZ (ANALYSIS) İMPORTLARI ---
# Yeni oluşturduğun analiz modüllerini buraya dahil ediyoruz
from analysis.summary_report import generate_full_report

# --- BÖLÜM 3: GÖRSELLEŞTİRME (VISUALIZATION) İMPORTLARI ---
from visualization.main_visualizer import generate_all_visualizations

def main():
    # --- BÖLÜM 1: TEMİZLEME (PREPROCESSING) ---
    
    # Dosya yolları
    raw_data_path = 'data/weather_dataset_1000.csv'
    cleaned_data_path = 'data/weather_cleaned.csv' # Temiz dosyanın kaydedileceği yer
    plots_output_dir = 'plots' # Grafiklerin kaydedileceği yer

    # 1. Veriyi Yükle
    df = reading(raw_data_path)
    if df is None:
        print("Veri yükleme hatası.")
        return

    nan_columns_and_rows = df.isna().sum()
    print("Başlangıçtaki eksik değer durumu:")
    print("-"*50 + "\n")
    print(nan_columns_and_rows)
    print("="*50 + "\n")

    print(f"Temizleme işlemi başlıyor... Orijinal satır sayısı: {len(df)}")
    print("="*50 + "\n")

    # 2. Kategorik Verileri Temizle
    df = clean_categorical_data(df)
    print("="*50 + "\n")

    # 3. Veri Tiplerini Dönüştür
    df = convert_data_types(df)
    print("="*50 + "\n")

    # 4. Aykırı Değerleri Yönet
    df = handle_outliers(df)
    print("="*50 + "\n")

    # 5. Kopyaları Yönet
    df = handle_duplicates(df)
    print("="*50 + "\n")

    # 6. Eksik Verileri Doldur
    df = fill_missing_values(df)
    print("="*50 + "\n")

    # 7. Temiz Veriyi Kaydet
    save_data(df, cleaned_data_path)

    print(f"Temizleme tamamlandı. Nihai satır sayısı: {len(df)}")
    print("="*50 + "\n")

    print("--- Temizlenmiş Veriden İlk 5 Satır ---")
    print(df.head()) # Temiz verinin son durumunu yazdır

    # --- BÖLÜM 2: ANALİZ (ANALYSIS) ---
    
    print("\n" + "="*50)
    print("--- ANALİZ AŞAMASI BAŞLADI ---")
    print("="*50 + "\n")
    
    # Temizleme aşamasında kaydettiğimiz temiz veriyi yeniden yüklüyoruz
    # Bu, iki aşamayı (preprocessing ve analysis) birbirinden net olarak ayırır
    df_clean = reading(cleaned_data_path)
    
    if df_clean is not None:
        # Analiz modüllerinden ana rapor fonksiyonunu çağır
        # Bu fonksiyon (summary_report.py) diğerlerini (central_tendency, dispersion)
        # çağırarak tam istatistik raporunu üretecek.
        generate_full_report(df_clean)
    else:
        print(f"Analiz için {cleaned_data_path} dosyası yüklenemedi.")

    generate_all_visualizations(df_clean, plots_output_dir)
    print("\nTüm işlemler (Temizleme, Analiz, Görselleştirme) tamamlandı.")
    print("\nTüm işlemler tamamlandı.")

if __name__ == "__main__":
    main()