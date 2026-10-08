from operator import attrgetter
class Strumenti:
    def __init__(self, codice, nome, marca, anno, costo):
        self.codice = str(codice)
        self.nome = str(nome)
        self.marca = str(marca)
        self.anno = str(anno)
        self.costo = str(costo)
    def __str__(self):
        return f"{self.codice} {self.nome} {self.marca} {self.anno} {self.costo}"

class Prestiti:
    def __init__(self,codice,data, id_strumento, cognome_allievo):
        self.codice = str(codice)
        self.data = str(data)
        self.id_strumento = str(id_strumento)
        self.cognome_allievo = str(cognome_allievo)

    def __str__(self):
        return f"{self.id_strumento} {self.cognome_allievo} {self.data}"
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}
        self.prestito = {}
        self.contatore_strumenti = 0
        self.contatore_prestiti = 0

        @property
        def responsabile(self):
            return self.responsabile
        @responsabile.setter
        def responsabile(self, nuovo_responsabile):
            if not nuovo_responsabile or not nuovo_responsabile.rstrip():
                raise ValueError("Il nuovo nome del responsabile non può essere vuoto!")
            self.responsabile = nuovo_responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            infile = open(file_path, 'r', encoding='utf-8')
            for line in infile:
                word = line.rstrip(",").split(",")
                codice = word[0]
                nome = word[1]
                marca = word[2]
                anno = word[3]
                costo = word[4]
                nuovo_strumento = Strumenti (codice,nome, marca, anno, costo)
                self.strumenti[codice] = nuovo_strumento
            infile.close()
            return nuovo_strumento
        except FileNotFoundError:
            return None


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        self.contatore_strumenti +=1
        nuovo_codice = f"S{self.contatore_strumenti}"
        nuovo_strumento = Strumenti(
            codice=nuovo_codice,
            nome = tipo,
            marca = marca,
            anno = anno_acquisto,
            costo = valore
        )
        self.strumenti[nuovo_codice] = nuovo_strumento
        return nuovo_strumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        lista_strumenti = list(self.strumenti.values())
        strumenti_ordinati = sorted(lista_strumenti, key= attrgetter('marca'))
        return strumenti_ordinati


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.strumenti:
            raise Exception("Lo strumento non esiste nel sistema")
        for prestito_attivo in self.prestito.values():
            if prestito_attivo.id_struemnto == id_strumento:
                raise Exception("Lo strumento è già in prestito")
        self.contatore_prestiti += 1
        nuovo_codice_prestiti = f"P{self.contatore_prestiti}"
        nuovo_prestito_obj = Prestiti(
            codice=nuovo_codice_prestiti,
            data=data,
            id_strumento= id_strumento,
            cognome_allievo = cognome_allievo
        )
        self.prestito[nuovo_codice_prestiti] = nuovo_prestito_obj
        return nuovo_prestito_obj



    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.prestito:
            raise Exception("Il codice del prestito inserito non esiste nel sistema")
        prestito_rimosso = self.prestito.pop(id_prestito)
        return prestito_rimosso

