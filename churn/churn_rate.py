"""Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
vari attributi del cliente e la loro fedeltà.



Dataset: 
5 min
ID_Cliente: Identificativo unico per ogni cliente
Età: Età del cliente
Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
Tariffa_Mensile: Quanto il cliente paga al mese
Dati_Consumati: GB di dati consumati al mese
Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
Churn: Se il cliente ha lasciato la compagnia (Sì/No)


Caricamento e Esplorazione Iniziale:
#5 min
Caricare i dati da un file CSV.
Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con
valori mancanti.

Pulizia dei Dati:
#10-20 min
Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).

Analisi Esplorativa dei Dati (EDA):
#10 min
Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.

Preparazione dei Dati per la Modellazione:
# ? 
Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.

Analisi Statistica e Predittiva:
# ?
Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata
su altri fattori.
Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve)."""


import pandas as pd
import numpy as np
import gestioneerrori as er

class gestioneClienti:
    
    def __init__(self):
        self.df = None
    
    
    def crea_df():
        cliente = {
            'ID_Cliente': range(1, 21),
            'Età': np.random.randint(18, 70, size=20),
            'Durata_Abbonamento': np.random.randint(1, 12, size=20),
            'Tariffa_Mensile': np.random.randint(20, 100, size=20),
            'Dati_Consumati': np.random.randint(1, 50, size=20),
            'Servizio_Clienti_Contatti': np.random.randint(0, 10, size=20),
            'Churn': np.random.choice(['Y', 'N'], size=20)
        }

        df = pd.DataFrame(cliente)
        df.to_csv('clienti.csv', index=False)
        print(df)
        return df

    def leggi_df(self):
        self.df = pd.read_csv('clienti.csv')
        print(self.df)
        return self.df

    def get_info(self):
        info = self.df.info()
        print("\n")
        print(info)
        return info

    def get_describe(self):
        describe = self.df.describe()
        print("\n")
        print(describe)
        return describe

    def get_value_counts(self):
        value_churn = self.df['Churn'].value_counts()
        print("\n")
        print(value_churn)
        return value_churn


# Utilizzo della classe gestioneClienti
gc = gestioneClienti()
df = gc.crea_df()
gc.leggi_df()
gc.get_info()
gc.get_describe()
gc.get_value_counts()
