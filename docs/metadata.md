INFORMAZIONI E METADATA

1. FONTE DATI
Dataset: Brazilian E-Commerce Public Dataset by Olist
Fonte: Kaggle (https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
Provider: Olist Store

2. ELABORAZIONE DATI
La preparazione del dataset è stata effettuata utilizzando Python con le seguenti operazioni:

Fase di ETL:
- Integrazione di tre dataset principali: sales_data.csv, customer_data.csv, product_data.csv
- Aggregazione dati per order_id, customer_id, order_date e product_category
- Calcolo del total_amount per ogni ordine
- Conversione delle date in formato datetime
- Rimozione dei valori nulli
- Ordinamento per data

Librerie Python utilizzate:
- pandas
- numpy
- pathlib

3. STRUTTURA DASHBOARD
La dashboard è organizzata in quattro pagine:
- Overview: KPI principali e metriche aggregate
- Analisi Vendite per Paese: trend e distribuzioni geografiche
- Pattern di Acquisto: analisi dettagliate e combinazioni prodotti
- Metadata: informazioni tecniche e credits

4. CREDITS
- Dataset originale: Olist Store (Brazilian E-Commerce)
- Elaborazione dati e visualizzazione: [Il tuo nome]
- Data creazione: 09/12/2024
- Ultimo aggiornamento: 09/12/2024
- Repository: [Link GitHub]

5. NOTE TECNICHE
- Strumento: Microsoft Power BI Desktop
- Periodo analizzato: 2023
- Aggiornamento dati: [Frequenza]