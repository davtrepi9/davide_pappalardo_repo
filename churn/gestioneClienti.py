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
# 20 min
Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.

Analisi Statistica e Predittiva:
# ?
Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata
su altri fattori.
Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve)."""


import pandas as pd
import numpy as np
import gestioneerrori as errori


errori = errori.Error()

class GestioneClienti:
    
    def __init__(self):
        self.df = None

    def leggi_df(self):
        self.df = pd.read_csv('clienti.csv')
        print(self.df)
        return self.df

    def get_info(self):
        try:
            info = self.df.info()
            print("\n")
            print(info)
            return info
        except AttributeError:
            errori.gestioneAttributeError()

    def get_describe(self):
        try:
            describe = self.df.describe()
            print("\n")
            print(describe)
            return describe
        except AttributeError:
            errori.gestioneAttributeError()

    def get_value_counts(self):
        try:
            value_churn = self.df['Churn'].value_counts()
            print("\n")
            print(value_churn)
            return value_churn
        except TypeError:
            errori.gestioneTypeError()

    def rimuovi_anomalie(self):
        try:
            self.df.loc[(self.df['Età'] < 18) | (self.df['Età'] > 90), 'Età'] = np.nan
            self.df.loc[self.df['Durata_Abbonamento'] <= 0, 'Durata_Abbonamento'] = np.nan
            self.df.loc[(self.df['Tariffa_Mensile'] <= 0) | (self.df['Tariffa_Mensile'] > 1000), 'Tariffa_Mensile'] = np.nan
            self.df.loc[(self.df['Dati_Consumati'] <= 0) | (self.df['Dati_Consumati'] > 1000), 'Dati_Consumati'] = np.nan
            self.df.loc[(self.df['Servizio_Clienti_Contatti'] < 0) | (self.df['Servizio_Clienti_Contatti'] > 100), 'Servizio_Clienti_Contatti'] = np.nan
            print(self.df)
            GestioneClienti.salva_csv(self.df)
            return self.df
        except AttributeError:
            errori.gestioneAttributeError()

    def pulizia_dati(self):
        try:
            self.df.dropna(subset=['ID_Cliente'])
            print(self.df)
            GestioneClienti.salva_csv(self.df)
            return self.df
        except AttributeError:
            errori.gestioneAttributeError()

    def imputa_dati_mancanti(self):
        try:
            self.df['Età'] = self.df['Età'].fillna(self.df['Età'].mean())
            self.df['Durata_Abbonamento'] = self.df['Durata_Abbonamento'].fillna(self.df['Durata_Abbonamento'].median())
            self.df['Tariffa_Mensile'] = self.df['Tariffa_Mensile'].fillna(self.df['Tariffa_Mensile'].mean())
            self.df['Dati_Consumati'] = self.df['Dati_Consumati'].fillna(self.df['Dati_Consumati'].median())
            self.df['Servizio_Clienti_Contatti'] = self.df['Servizio_Clienti_Contatti'].fillna(self.df['Servizio_Clienti_Contatti'].mode()[0])
            self.df['Churn'] = self.df['Churn'].fillna('No')
            print(self.df)
            GestioneClienti.salva_csv(self.df)
            return self.df

        except TypeError:
            errori.gestioneTypeError()

    def aggiungi_categoria(self):
        try:
            print("\n")
            self.df['Costo_per_GB']=self.df['Tariffa_Mensile']/self.df['Dati_Consumati']
            print("\n La categoria è stata aggiunta: \n", self.df)
            return True
        except TypeError:
            errori.gestioneTypeError()

    def dati_gruppo(self):
        try:
            m_età_tariffa = self.df.groupby('Età')['Tariffa_Mensile'].mean()
            print("\n",m_età_tariffa)
            m_churn_durata = self.df.groupby('Churn')['Tariffa_Mensile'].mean()
            print("\n", m_churn_durata)
            m_età_durata = self.df.groupby('Durata_Abbonamento')['Età'].mean()
            print("\n", m_età_durata)
        except AttributeError:
            errori.gestioneAttributeError()

    def correlazioni(self):
        try:
            print(self.df.corr(method = 'pearson',numeric_only = True))
        except AttributeError:
            errori.gestioneAttributeError()

    def conversione_churn(self):
            try:
                self.df['Churn']=self.df['Churn'].map(lambda x: 1 if x == "Sì" else 0)
                print(self.df)
                GestioneClienti.salva_csv(self.df)
                return self.df
            except TypeError:
                errori.gestioneTypeError()

    def normalizzazione(self):
        try:
            for colonna in ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti']:
                self.df[colonna] = (self.df[colonna] - self.df[colonna].mean()) / self.df[colonna].std()
                print(self.df)
            return self.df
        except TypeError:
            errori.gestioneTypeError()

    def salva_csv(df):
        df.to_csv('clienti.csv', index=False)
        print(" -- CSV AGGIORNATO -- ")
        

#CSV INIZIALE DI RIFERIMENTO 
"""ID_Cliente,Età,Durata_Abbonamento,Tariffa_Mensile,Dati_Consumati,Servizio_Clienti_Contatti,Churn
1.0,-28.0,39.0,29.36,45.2,6.0,
2.0,-55.0,48.0,,15.97,1.0,Sì
3.0,27.0,54.0,51.28,22.36,3.0,Sì
4.0,32.0,52.0,93.5,36.53,1.0,No
5.0,,53.0,66.76,,5.0,No
6.0,31.0,,78.61,18.34,0.0,Sì
,34.0,7.0,21.06,8.88,4.0,No
8.0,69.0,7.0,63.42,7.93,5.0,No
,46.0,,88.98,12.39,6.0,No
10.0,43.0,57.0,57.11,10.45,,Sì
11.0,69.0,,43.05,8.69,6.0,Sì
,54.0,39.0,69.63,9.14,6.0,
13.0,66.0,17.0,32.95,2.75,4.0,No
14.0,54.0,18.0,29.73,9.07,6.0,Sì
,44.0,,28.91,41.52,3.0,No
16.0,69.0,15.0,34.96,,3.0,Sì
17.0,39.0,16.0,22.82,34.44,9.0,Sì
18.0,44.0,46.0,24.91,2.78,6.0,No
19.0,24.0,,26.75,6.74,7.0,Sì
20.0,42.0,57.0,76.71,7.09,5.0,No"""

