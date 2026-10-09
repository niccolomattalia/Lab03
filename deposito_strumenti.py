from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.__nome = nome
        self.__responsabile = responsabile
        self.__strumenti = []
        self.__prestiti = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome


    @property
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter
    def responsabile(self,responsabile):
        self.__responsabile = responsabile

    def carica_file_strumenti(self, file_path):
        listaStrumenti = []
        with open(file_path, "r") as inp:
            for i in inp:
                if i == "\n":
                    continue

                lista = i.strip().split(',')
                if len(lista) < 5:
                    continue

                s = Strumento()
                s.codice = lista[0]
                s.tipo = lista[1]
                s.marca = lista[2]
                s.anno = int(lista[3])
                s.val = float(lista[4])
                listaStrumenti.append(s)

            self.__strumenti = listaStrumenti


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        if len(self.__strumenti) != 0:
            cont = (self.__strumenti[-1]).codice[1:]
            cont = int(cont)
            cont+=1
        else:
            cont = 1

        s=Strumento()
        s.codice = f"S{cont}"
        s.tipo = tipo
        s.marca = marca
        s.anno = anno_acquisto
        s.val = valore
        self.__strumenti.append(s)
        return s



    def strumenti_ordinati_per_marca(self):
        lista = sorted(self.__strumenti, key=attrgetter('marca'))
        return lista

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        ok = False
        for l in self.__strumenti:
            if l.codice == id_strumento:
                ok = True
                break

        if ok:
            if len(self.__prestiti) != 0:
                cont = int((self.__prestiti[-1].codice[1:]))
                cont +=1
                for i in self.__prestiti:
                    if i.id_strumento == id_strumento:
                        raise Exception("strumento gia' in prestito")
            else:
                cont = 1

            p = Prestito()
            p.data = data
            p.id_strumento = id_strumento
            p.cognome_allievo = cognome_allievo
            p.codice = f"P{cont}"
            self.__prestiti.append(p)
            return p
        else:
            raise Exception("Strumento non esistente")

    def termina_prestito(self, id_prestito):
        vero = True
        for i in self.__prestiti:
            if i.codice == id_prestito:
                self.__prestiti.remove(i)
                vero = False
                break
        if vero:
            raise Exception("Non è stato trovato il codice del prestito inserito")



class Strumento:

    def __init__(self):
        self.__codice = ""
        self.__tipo = ""
        self.__marca = ""
        self.__anno = 0
        self.__val = 0

    @property
    def codice(self):
        return self.__codice

    @codice.setter
    def codice(self,codice):
        self.__codice = codice



    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo



    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca



    @property
    def anno(self):
        return self.__anno

    @anno.setter
    def anno(self, anno):
        self.__anno = anno



    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val):
        self.__val = val


    def __str__(self):
        return f"{self.__codice}, {self.__tipo}, {self.__marca}, {self.__anno}, {self.__val}"


    def __repr__(self):
        return self.__str__()




class Prestito:

    def __init__(self):
        self.__codice = 0
        self.__data = ""
        self.__id_strumento = ""
        self.__cognome_allievo = ""

    @property
    def codice(self):
        return self.__codice

    @codice.setter
    def codice(self,codice):
        self.__codice = codice



    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data = data

    @property
    def id_strumento(self):
        return self.__id_strumento

    @id_strumento.setter
    def id_strumento(self, id_strumento):
        self.__id_strumento = id_strumento

    @property
    def cognome_allievo(self):
        return self.__cognome_allievo

    @cognome_allievo.setter
    def cognome_allievo(self, cognome_allievo):
        self.__cognome_allievo = cognome_allievo


    def __str__(self):
        return f"{self.__codice}, {self.__data}, {self.__id_strumento}, {self.__cognome_allievo}"


    def __repr__(self):
        return self.__str__()

