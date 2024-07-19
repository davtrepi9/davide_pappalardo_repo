import gestorevendite as new

while True:
    print("\nMenu:")
    print("1. Crea un Dataframe ")
    print("2. Aggiungi la colonna totale vendite ")
    print("3. Totale vendite per ciascun prodotto ")
    print("4. Trovare il prodotto più venduto in termini di quantità ")
    print("5. Identificare la città con il maggior volume di vendite totali ")
    print("6. Creare un nuovo DataFrame che mostri solo le vendite superiori a 8000")
    print("7. Ordinare il DataFrame originale per il totale vendite in ordine decrescente ")
    print("8. Visualizzare il numero di vendite per ogni città")
    print("9. Esci")

    seleziona = input("Scegli un'opzione: ")
        
    if seleziona.isalpha():
            print("Errore Input ")
            break
    if seleziona.isspace():
            print("Errore Input ")

    if seleziona == '1':
        
        df=new.crea_dataframe()

    elif seleziona == '2':
    
        new.aggiungi_categoria(df)

    elif seleziona == '3':
        
        new.raggruppa(df)

    elif seleziona == '4':
        
        new.max(df)

    elif seleziona == '5':
        
        new.max_città(df)

    elif seleziona == '6':
        
        new.vendite_sup(df)

    elif seleziona == '7':
        
        new.ordina(df)

    elif seleziona == '8':
        
        new.città(df)

    elif seleziona == '9':
        break
    else:
        print("Scelta non valida. Riprova.")