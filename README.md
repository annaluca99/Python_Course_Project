# Python_Course_Project

# Sistema di Gestione Studenti (Python)

### Descrizione del progetto
Questo repository contiene l'esercitazione finale del corso di Python. Il progetto consiste in un semplice script che utilizza i principi della Programmazione Orientata agli Oggetti (OOP) per simulare la gestione dei dati e delle attività di uno studente universitario.

Il file principale definisce la classe Studente. Attraverso il costruttore della classe (__init__), ogni volta che viene creato un nuovo studente è possibile assegnargli delle informazioni personali uniche (stato dell'oggetto).

### Attributi della Classe
Ogni istanza della classe Studente memorizza i seguenti dati: Nome dello studente, cognome dello studente, età dello studente, matricola dello studente, e una lista inizialmente vuota che raccoglie i voti degli esami superati.

### Cosa fa lo script:
* **Creazione Profilo**: Registra nome, cognome, età e numero di matricola. Stampa a schermo un messaggio formale con i dati anagrafici e la matricola dello studente.
* **Gestione Libretto**: Permette di aggiungere voti in una lista interna.
* **Validazione**: Controlla che i voti inseriti siano validi (compresi tra 18 e 30). Riceve un voto in input. Verifica che sia valido (compreso tra 18 e 30) e, in caso affermativo, lo aggiunge alla lista dei voti dello studente. Gestisce le eccezioni stampando messaggi di errore in caso di insufficienza o voto oltre il massimo consentito.
* **Analisi Dati**: Calcola la media aritmetica dei voti presenti nel libretto. Calcola e stampa la media matematica dei voti presenti nella lista dello studente. Se la lista è vuota, gestisce il caso restituendo 0.
* **Azioni**: Include un metodo per simulare le ore di studio effettuate. Stampa un messaggio che indica quante ore di studio ha completato lo studente.