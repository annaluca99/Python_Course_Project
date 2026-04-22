# Creiamo la classe Studente, con alcuni attributi:
class Studente:

    def __init__(self, nome, cognome, eta, matricola):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.voti = []

    # La classe contiene questi metodi:
    def presentati(self):
        """Stampa una presentazione dello studente"""
        presentazione = f"Ciao! Mi chiamo {self.nome} {self.cognome}, ho {self.eta} anni e la mia matricola è {self.matricola}."
        print(presentazione)

    def aggiungi_voto(self, voto):
        # Controlliamo che il voto sia tra 18 e 30
        if 18 <= voto <= 30:
            self.voti.append(voto)
            print(f"Voto {voto} registrato correttamente per {self.nome}.")
        elif voto < 18:
            print(
                f"Esame non superato: il voto {voto} è insufficiente e non verrà aggiunto."
            )
        else:
            print("Errore: un voto non può essere superiore a 30.")

    def calcola_media(self):
        """Restituisce la media dei voti. Se non ci sono voti, restituisce 0"""
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)

    def studia(self, ore):
        """Descrive l'attività di studio"""
        print(f"{self.nome} ha studiato sodo per {ore} ore oggi!")


# --- (Esecuzione) --- #testiamo il codice
# 1. Creazione di due istanze (oggetti) della classe Studente
studente1 = Studente("Matteo", "Verdi", 25, "44053")
studente2 = Studente("Cristiano", "Rossi", 21, "20251")

print("--- PRESENTAZIONE ---")
studente1.presentati()
studente2.presentati()

print("\n--- ATTIVITÀ ---")
# Azioni studente 1
studente1.studia(4)
studente1.aggiungi_voto(28)
studente1.aggiungi_voto(30)

# Azioni studente 2
studente2.studia(6)
studente2.aggiungi_voto(24)

print("\n--- RISULTATI FINALI ---")
# Dimostrazione che ogni istanza mantiene i propri dati
print(f"Media di {studente1.nome}: {studente1.calcola_media():.2f}")
print(f"Media di {studente2.nome}: {studente2.calcola_media():.2f}")
