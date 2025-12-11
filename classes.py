def codi_in_llista_hotels(llista_hotels, nom_hotel):
    for hotel in llista_hotels:
        if hotel.codi == codi:
            return True
    return False

class Barri:
    def __init__(self, nom, codi_districte):
        if type(codi_districte) != int or codi_districte <= 0:
            raise ValueError("El codi del districte ha de ser un enter positiu.")
        self.nom = nom
        self.codi_districte = codi_districte
    
    def __str__(self):
        return f"Barri: {self.nom}, Codi Districte: {self.codi_districte}"
class Districte:
    def __init__(self, nom, extensio, poblacio):
        if type(poblacio) != int or poblacio < 0:
            raise ValueError("La població ha de ser un enter no negatiu.")
        if type(extensio) != (int or float) or extensio <= 0:
            raise ValueError("L'extensió ha de ser un nombre positiu.")
        self.nom = nom
        self.extensio = extensio
        self.poblacio = poblacio
    def __str__(self):
        return f"{self.nom}, {self.extensio} km^2, {self.poblacio} habitants) barris: {str_barris}"
    def densitat(self):
        return self.poblacio / self.extensio

def importar_districtes(nom_fitxer, separador):
    dic_districtes = {}
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip() 
                if not line:
                    continue
                parts = line.split(separador)
                codi = int(parts[0])
                nom = parts[1]
                extensio = float(parts[2])
                poblacio = int(parts[3])
                dic_districtes[codi] = Districte(nom, extensio, poblacio)
        print(f"S'han importat correctament {len(dic_districtes)} districtes")
        return dic_districtes
    except FileNotFoundError:
        raise FileNotFoundError("fitxer no trobat")

def omplir_llista_barris(dic_districtes, dic_barris):
    for districte in dic_districtes.values():
        if districte.llista_barris:
            print("El diccionari de districtes ja conté informació dels barris")
            return
    for codi_barri, barri in dic_barris.items():
        codi_districte = barri.codi_districte
        if codi_districte in dic_districtes:
            dic_districtes[codi_districte].llista_barris.append(barri.nom)

def mostrar_menu():
    print("---MENÚ PRINCIPAL---\n")
    print("1 - Veure hotels\n")
    print("S - Sortir del programa")
