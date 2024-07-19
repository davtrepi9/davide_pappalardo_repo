"""Scenario: Una catena di ristoranti vuole analizzare le vendite giornaliere in diverse filiali.
Obiettivo: Utilizzare pandas per calcolare le vendite medie giornaliere per ogni filiale.
Dati: Il dataset contiene colonne "Data", "Filiale" e "Vendite".

Compiti:
Genera i dati da un file CSV.
Utilizza groupby() per raggruppare i dati per "Data" e "Filiale".
Calcola la media delle vendite giornaliere per filiale
Calcola quale filiale ha venduto di più
Salva tutti i valori e i risultati su un nuovo file(ES: csv)."""

import pandas as pd

#genero i dati da un file csv
df = pd.read_csv(r'C:\Users\Elron\Desktop\Python\davide_pappalardo_repo\churn\pythontest_19_07\dativendita.csv')
print("Dati vendita: ")
print(df)


#utilizzo groupby per raggruppare data e filiale
raggruppamento = df.groupby(['Data', 'Filiale'])['Vendite'].sum()
print("\nRaggruppamento per Data e Filiale:")
print(raggruppamento)

#media vendite giornaliere per filiale
mediavendite = df.groupby(['Data','Filiale'])['Vendite'].mean()
print("\nMedia delle vendite giornaliere per filiale:\n", mediavendite)

#filiale con max vendite
filiale = df.groupby('Filiale')['Vendite'].sum().idxmax()
massimo = df.groupby('Filiale')['Vendite'].sum().max()
print(f"\nLa città che ha venduto di più è stata {filiale}, con un totale di {massimo} vendite")

#salvo in una nuovo csv
mediavendite.to_csv('media_dativendita.csv', index=False)
print("\nCreato nuovo file csv")
