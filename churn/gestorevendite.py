"""Pandas

Esercizio 2: Manipolazione e Aggregazione dei Dati

Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con
pandas.

Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse
città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.

1.Caricare i dati in un DataFrame.
2.Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
Quantità e Prezzo Unitario.
3.Raggruppare i dati per Prodotto e calcolare il totale delle vendite per
ciascun prodotto.
4.Trovare il prodotto più venduto in termini di Quantità.
5.Identificare la città con il maggior volume di vendite totali.
6.Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo
valore (es., 1000 euro).
7.Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine
decrescente.
8.Visualizzare il numero di vendite per ogni città."""


import pandas as pd
import gestioneerrori as ge

class Gestore():

    """vendite = {
        'prodotto': ["Computer", "Smartphone", "Tastiera", "Mouse","Computer"],
        'quantità': [30,50,70,90,20],
        'prezzo unitario': [800,400,100,50,800],
        'città': ['Roma', 'Milano', 'Roma', 'Napoli','Milano']
    }"""

#1.Caricare i dati in un DataFrame.
def crea_dataframe():
    df = pd.read_csv('vendita.csv')
    #df = pd.DataFrame(vendite)
    print(df)
    return df

#2.Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra Quantità e Prezzo Unitario.

def aggiungi_categoria(df):
        print("\n")
        df['totale vendite']=df['prezzo unitario']*df['quantità']
        print("\n La categoria è stata aggiunta: \n", df)
   

#3.Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto.

def raggruppa(df):
    try:
        gruppo = df.groupby('prodotto')['totale vendite'].sum()
        print("\n I prodotti raggruppati e sommati tra di loro sono: \n", gruppo)
    except KeyError:
        ge.gestioneKeyError()
#4.Trovare il prodotto più venduto in termini di Quantità.   
def max(df):
    nome = df.groupby('prodotto')['quantità'].sum().idxmax()
    massimo = df.groupby('prodotto')['quantità'].sum().max()
    print(f"\nIl prodotto che è stato venduto di più è {nome}, con un totale di {massimo} vendite")


#5.Identificare la città con il maggior volume di vendite totali.
def max_città(df):
    try:
        nome = df.groupby('città')['totale vendite'].sum().idxmax()
        massimo = df.groupby('città')['totale vendite'].sum().max()
        print(f"\nLa città che ha venduto di più è stata {nome}, con un totale di {massimo} vendite")
    except KeyError:
        ge.gestioneKeyError()
#6.Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore (es., 1000 euro).

def vendite_sup(df):
    try:
        valore = 8000
        nuovo_df = df[df['totale vendite']>valore]
        print(f"\nLe vendite superiori a {valore} sono: {nuovo_df}")
    except KeyError:
        ge.gestioneKeyError()

#7.Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente.
def ordina(df):
    try:
        df = df.sort_values(by='totale vendite', ascending=False)
        print("\nIl dataframe ordinato è:\n",df)
    except KeyError:
        ge.gestioneKeyError()

#8.Visualizzare il numero di vendite per ogni città.
def città(df):
    try:
        gruppo = df.groupby('città')['totale vendite'].sum()
        print("\nIl numero di vendite per città è :",gruppo)
    except KeyError:
        ge.gestioneKeyError()
    


