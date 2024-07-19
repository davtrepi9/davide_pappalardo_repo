"""Scenario: Una azienda vuole analizzare la performance giornaliera delle vendite e delle ore lavorative dei suoi dipendenti 
per ottimizzare le operazioni.
Obiettivo: Utilizzare Pandas e Numpy per calcolare le vendite medie per ora lavorativa e identificare giorni di alta e bassa efficienza.

Compiti:
Generazione dei Dati:
Utilizza numpy per generare un array di date per 30 giorni.
Genera dati casuali per "Vendite" e "Ore Lavorative" utilizzando numpy per ciascun giorno.
Crea un DataFrame pandas con colonne "Data", "Vendite", "Ore Lavorative".
Analisi delle Vendite:
Calcola le vendite medie per ora lavorativa per ogni giorno.
Identifica i giorni con la massima e la minima
Salva tutti i valori e i risultati su un nuovo file(ES: csv)."""


import numpy as np
import pandas as pd

#genero 30 date
date = np.arange('2024-04', '2024-05', dtype='datetime64[D]')
print("\nDate generate:")
print(date)

#genero 30 vendite e 30 ore lavorative
vendite = np.random.randint(200, 1000, size=30)
ore_lavorative = np.random.randint(4, 10, size=30)

#creo il dataframe

df = pd.DataFrame({
    "Data" : date,
    "Vendite" : vendite,
    "Ore Lavorative" : ore_lavorative
})

print("\n Dataframe generato: ")
print(df)

#calcolo vendite medie per ora lavorativa per ogni giorno
mediavendite = df.groupby(['Data','Ore Lavorative'])['Vendite'].mean()
print("\nMedia delle vendite orarie per ogni giorno:\n", mediavendite)

#giorni con max/min vendite
data = df.groupby('Data')['Vendite'].sum().idxmax()
massimo = df.groupby('Data')['Vendite'].sum().max()
minimo = df.groupby('Data')['Vendite'].sum().min()

print(f"\nLa data in cui si è venduto di più è stata {data}, con un totale di {massimo} vendite")
print(f"\nLa data in cui si è venduto di meno ha di più è stata {data}, con un totale di {minimo} vendite")