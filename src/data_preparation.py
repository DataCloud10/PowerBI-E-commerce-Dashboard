import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

# Definizione percorsi
ROOT_DIR = Path(__file__).parent.parent
DATA_RAW = ROOT_DIR / 'data' / 'raw'
DATA_PROCESSED = ROOT_DIR / 'data' / 'processed'

print("Inizializzazione preparazione dati...")

try:
    # 1. Caricamento dei dati
    print("\nCaricamento files...")
    sales = pd.read_csv(DATA_RAW / 'sales_data.csv')
    customers = pd.read_csv(DATA_RAW / 'customer_data.csv')
    products = pd.read_csv(DATA_RAW / 'product_data.csv')
    
    print(f"Caricati:")
    print(f"- {len(sales)} righe di vendite")
    print(f"- {len(customers)} clienti")
    print(f"- {len(products)} prodotti")
    
    # 2. Unione dei dati
    print("\nCombinazione datasets...")
    df = sales.merge(customers, on='customer_id', how='left')
    df = df.merge(products[['product_id', 'category']], on='product_id', how='left')
    
    # 3. Preparazione dataset finale
    print("Preparazione dataset finale...")
    final_df = df.groupby([
        'order_id', 
        'customer_id', 
        'date',
        'category'
    ]).agg({
        'revenue': 'sum',
        'quantity': 'sum',
        'price': 'mean',
        'age': 'first',
        'gender': 'first',
        'country': 'first'
    }).reset_index()
    
    # 4. Rinomina colonne per chiarezza
    final_df = final_df.rename(columns={
        'date': 'order_date',
        'category': 'product_category'
    })
    
    # 5. Pulizia e formattazione
    print("Pulizia e formattazione...")
    final_df['order_date'] = pd.to_datetime(final_df['order_date'])
    final_df = final_df.sort_values('order_date')
    final_df = final_df.dropna()
    
    # 6. Salvataggio
    output_file = DATA_PROCESSED / 'prepared_ecommerce_data.csv'
    print(f"\nSalvataggio dati in {output_file}...")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    final_df.to_csv(output_file, index=False)
    
    print("\nPreparazione completata con successo!")
    print(f"Dataset salvato in: {output_file}")
    print("\nPrime righe del dataset finale:")
    print(final_df.head())

except FileNotFoundError as e:
    print("\nERRORE: File non trovato!")
    print("Assicurati che i seguenti file siano nella cartella corrente:")
    print("- sales_data.csv")
    print("- customer_data.csv")
    print("- product_data.csv")
    
except Exception as e:
    print(f"\nERRORE durante l'elaborazione: {str(e)}")