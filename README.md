# Esempio di app completa

Qui c'è un templete di esempio per un applicazione che:
1) crea un modello di regressione lineare 
2) importa il modello in un API generata con fastAPI
3) fornisce interfaccia utente con streamlit


## Modello: 
- acquisizione ed elaborazione dati
- creazione del feature e target e relativi train set e test set
- test del modello e valutazione della sua accuratezza 
- esportazione dello stesso usando file pkl


## API
- importazione del modello all'avvio del servizio
- struttura dati che permetta di passare i dati in ingresso corretti
- definizione della chiamata


## Frontend
- UI che permetta di inserire i dati in maniera congrua con quanto richiesto dal modello

## Avvio servizi

### API 
Lanciare con python il servizio di fastAPI semplicemente lanciando il file (solitamente main.py). Attenzione alle porte, il server uvicorn solitamente gira sulla porta 8000 ma è possibile definirlo quando si impartisce la direttiva 

    uvicorn.run(port='numero_porta')


### Streamlit 

    streamlit run percorso/nome_file.py

Per streamlit è necessario lanciare il servizio.