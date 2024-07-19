
import gestioneClienti as gc
import gestioneerrori as error
 
gestione = gc.GestioneClienti()

while True:
        print("\nMenu:")
        print("1. Caricare i dati")
        print("2. Informazioni sul dataset")
        print("3. Descrizione del dataset")
        print("4. Conteggio valori di Churn")
        print("5. Rimuovere anomalie")
        print("6. Pulizia dei dati")
        print("7. Imputazione dati mancanti")
        print("8. Aggiungere categoria Costo_per_GB")
        print("9. Dati di gruppo")
        print("10. Correlazioni")
        print("11. Conversione colonna Churn")
        print("12. Normalizzazione dei dati")
        print("0. Esci")
        seleziona = input("Scegli un'opzione: ")
        
        if seleziona.isalpha():
                print("Errore Input ")
                break
        if seleziona.isspace():
                print("Errore Input ")

        if seleziona == '1':
            gestione.leggi_df()
        elif seleziona == '2':
            gestione.get_info()
        elif seleziona == '3':
            gestione.get_describe()
        elif seleziona == '4':
            gestione.get_value_counts()
        elif seleziona == '5':
            gestione.rimuovi_anomalie()
        elif seleziona == '6':
            gestione.pulizia_dati()
        elif seleziona == '7':
            gestione.imputa_dati_mancanti()
        elif seleziona == '8':
            gestione.aggiungi_categoria()
        elif seleziona == '9':
            gestione.dati_gruppo()
        elif seleziona == '10':
            gestione.correlazioni()
        elif seleziona == '11':
            gestione.conversione_churn()
        elif seleziona == '12':
            gestione.normalizzazione()
        elif seleziona == '0':
            print("- - - EXIT - - - ")
            break
        else:
            print("Input non valido ! Ripeti.")