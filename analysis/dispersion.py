import pandas as pd

def calculate_variance(df, numeric_cols):
    # Verilen sütunların varyansını hesaplıyor
    return df[numeric_cols].var()

def calculate_std_dev(df, numeric_cols):
    # Verilen sütunların standart sapmasını hesaplıyor
    return df[numeric_cols].std()

def calculate_range(df, numeric_cols):
    # Verilen sütunların min ve max değerlerini aralık olarak hesaplıyor
    min_vals = df[numeric_cols].min()
    max_vals = df[numeric_cols].max()
    return min_vals, max_vals

def get_dispersion(df, numeric_cols):
    # Tüm dağılım ölçülerini bir DataFrame'de birleştiriyoruz
    print("--- Dağılım Ölçüleri Hesaplanıyor ---")
    
    dispersion_df = pd.DataFrame(index=numeric_cols)
    dispersion_df['Varyans (Variance)'] = calculate_variance(df, numeric_cols)
    dispersion_df['Standart Sapma (Std Dev)'] = calculate_std_dev(df, numeric_cols)
    
    min_vals, max_vals = calculate_range(df, numeric_cols)
    dispersion_df['Minimum (Min)'] = min_vals
    dispersion_df['Maksimum (Max)'] = max_vals
    
    return dispersion_df