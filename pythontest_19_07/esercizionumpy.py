"""Scenario: Un laboratorio scientifico registra le temperature ogni ora.
Obiettivo: Utilizzare numpy per calcolare la temperatura media, minima e massima registrata.
Dati: Un array numpy di temperature registrate in una giornata.

Compiti:
Crea una dataset di dati da almeno 24 posizioni
Calcola la temperatura media 
Trova la temperatura massima e minima.
Determina la temperatura più probabile per le prossime 4 posizioni rispetto a un aumento costante di 0,2 gradi al giorno ogni settimana. """


import numpy as np

#periodo estivo 25 a 40 gradi , 24 posizioni
array_temp = np.random.randint(25, 40, size=24)  

#calcolo temperatura media
media_temp = np.mean(array_temp)
print(f"Media delle temperature {media_temp}.")

#calcolo max e min temperatura
max_temp = np.max(array_temp)
min_temp = np.min(array_temp)
print(f"Max temperatura registrata: {max_temp}.")
print(f"Min temperatura registrata: {min_temp}.")

#previsione temperatura probabile
aumento_costante = (0.2 / 24) / 7 
previsione_temperature = array_temp[-1] + aumento_costante * np.arange(1, 5)
print("Previsione temperature per le prossime 4 ore:")
print(previsione_temperature)
