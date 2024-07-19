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
import gestioneerrori as er

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
            er.gestioneAttributeError()

    def get_describe(self):
        try:
            describe = self.df.describe()
            print("\n")
            print(describe)
            return describe
        except AttributeError:
            er.gestioneAttributeError()

    def get_value_counts(self):
        try:
            value_churn = self.df['Churn'].value_counts()
            print("\n")
            print(value_churn)
            return value_churn
        except TypeError:
            er.gestioneTypeError()

    def rimuovi_anomalie(self):
        try:
            self.df.loc[(self.df['Età'] < 18) | (self.df['Età'] > 90), 'Età'] = np.nan
            self.df.loc[self.df['Durata_Abbonamento'] <= 0, 'Durata_Abbonamento'] = np.nan
            self.df.loc[(self.df['Tariffa_Mensile'] <= 0) | (self.df['Tariffa_Mensile'] > 1000), 'Tariffa_Mensile'] = np.nan
            self.df.loc[(self.df['Dati_Consumati'] <= 0) | (self.df['Dati_Consumati'] > 1000), 'Dati_Consumati'] = np.nan
            self.df.loc[(self.df['Servizio_Clienti_Contatti'] < 0) | (self.df['Servizio_Clienti_Contatti'] > 100), 'Servizio_Clienti_Contatti'] = np.nan
            print(self.df)
            return self.df
        except AttributeError:
            er.gestioneAttributeError()

    def pulizia_dati(self):
        try:
            df = self.df.dropna(subset=['ID_Cliente'])
            print(df)
            return df
        except AttributeError:
            er.gestioneTypeError()

    def imputa_dati_mancanti(self):
        try:
            df = self.df['Età'] = self.df['Età'].fillna(self.df['Età'].mean())
            df = self.df['Durata_Abbonamento'] = self.df['Durata_Abbonamento'].fillna(self.df['Durata_Abbonamento'].median())
            df = self.df['Tariffa_Mensile'] = self.df['Tariffa_Mensile'].fillna(self.df['Tariffa_Mensile'].mean())
            df = self.df['Dati_Consumati'] = self.df['Dati_Consumati'].fillna(self.df['Dati_Consumati'].median())
            df = self.df['Servizio_Clienti_Contatti'] = self.df['Servizio_Clienti_Contatti'].fillna(self.df['Servizio_Clienti_Contatti'].mode()[0])
            df = self.df['Churn'] = self.df['Churn'].fillna('No')
            return df
        except TypeError:
            er.gestioneTypeError()

    def aggiungi_categoria(self):
        try:
            print("\n")
            self.df['Costo_per_GB']=self.df['Tariffa_Mensile']/self.df['Dati_Consumati']
            print("\n La categoria è stata aggiunta: \n", self.df)
            return True
        except TypeError:
            er.gestioneTypeError()

    def dati_gruppo(self):
        try:
            m_età_tariffa = self.df.groupby('Età')['Tariffa_Mensile'].mean()
            print("\n",m_età_tariffa)
            m_churn_durata = self.df.groupby('Churn')['Tariffa_Mensile'].mean()
            print("\n", m_churn_durata)
            m_età_durata = self.df.groupby('Durata_Abbonamento')['Età'].mean()
            print("\n", m_età_durata)
        except AttributeError:
            er.gestioneAttributeError()

    def correlazioni(self):
        try:
            print(self.df.corr(method = 'pearson',numeric_only = True))
        except AttributeError:
            er.gestioneAttributeError()

    def conversione_churn(self):
            try:
                self.df['Churn'] = self.df['Churn'].map({'N': 0, 'Y': 1})
                print(self.df)
                return self.df

            except TypeError:
                er.gestioneTypeError()

    def normalizzazione(self):
        try:
            for colonna in ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti']:
                self.df[colonna] = (self.df[colonna] - self.df[colonna].mean()) / self.df[colonna].std()
                print(self.df)
            return self.df
        except TypeError:
            er.gestioneTypeError()


