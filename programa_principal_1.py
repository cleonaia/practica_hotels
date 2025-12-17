class Hotel():
    def __init__(self, nom, codi_hotel, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles):
        if type(codi_hotel) != int:
            raise TypeError("El codi de l'hotel ha de ser un enter")
        if type(numero) != 0 or type(numero) < 0:
            raise ValueError("El numero ha de ser un valor positiu o zero")
        if type(codi_barri) != int:
            raise ValueError("codi_barri ha de ser un valor positiu")
        if type(codi_postal) != int:
            raise TypeError("El codi postal ha de ser un enter")
        if type(latitud) != float:
            raise TypeError("La latitud ha de ser un valor real")
        if type(longitud) != float:
            raise TypeError("La longitud ha de ser un valor real")
        if type(estrelles) not in range(1,6):
            raise TypeError("Les estrelles han de ser un valor entre 1 i 5")
        self.nom = str(nom)
        self.codi_hotel = int(codi_hotel)
        self.carrer = str(carrer)
        self.numero = int(numero)
        self.codi_barri = int(codi_barri)
        self.codi_postal = int(codi_postal)
        self.telefon = str(telefon)
        self.latitud = float(latitud)
        self.longitud = float(longitud)
        self.estrelles = int(estrelles)
    def __str__(self):
        return f"{self.nom} {self.codi_hotel}) {self.carrer}, {self.numero} {self.codi_postal} (barri: {self.codi_barri}) {self.telefon} ({self.latitud}, {self.longitud}) {self.estrelles} estrelles"

    def __gt__(self, altre_hotel):
        if self.estrelles > altre_hotel.estrelles:
            return True
        else:
            return False
    def distancia(self,latitud2,longitud2):
        if type(latitud2) != float:
            raise TypeError("La latitud ha de ser un valor real")
        if type(longitud2) != float:
            raise TypeError("La longitud ha de ser un valor real")
        import math
        radi_terra = 6378.137
        latitud = self.latitud * math.pi / 180
        longitud = self.longitud * math.pi / 180
        latitud2 = latitud2 * math.pi / 180
        longitud2 = longitud2 * math.pi / 180
        dist = arccos(sin(self.latitud)*sin(self.latitud2)+cos(self.latitud)*cos(self.latitud2)*cos(self.longitud2-self.longitud))*radi_terra

def codi_in_llista_hotels(llista_hotels, nom_hotel):
    for hotel in llista_hotels:
        if hotel.codi == codi:
            return True
    return False

def importar_hotels (nom_fitxer):
        try:
            with open(nom_fitxer, 'r', encoding='utf-8') as f:
                next(f)
                for linia in f:
                    linia = linia.strip()
                    if not linia:
                        continue
                    dades = linia.split(";")
                    nom_codi = dades[0].split('-')
                    if len(nom_codi) == 2:
                        nom = nom_codi[0].strip()
                        codi_hotel = nom_codi[1].replace('HB-', '')
                    else:
                        nom = dades[0].strip()
                        codi_hotel = ''
                    codi_hotel = int(dades[0].split('HB-')[1]) if 'HB-' in dades[0] else 0
                    carrer = dades[1].strip()
                    numero = int(dades[2])
                    codi_barri = int(dades[3])
                    codi_postal = int(dades[4])
                    telefon = dades[5].strip()
                    latitud = float(dades[6])/1000000
                    longitud = float(dades[7]) / 1000000
                    estrelles = int(dades[8])
                    if not codi_in_llista_hotels(codi_hotel, hotels):
                        hotel = Hotel(nom, codi_hotel, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles)
                        hotels.append(hotel)
            print(f"S'han importat correctament {len(hotels)} hotels")
            return hotels
        except FileNotFoundError:
            raise FileNotFoundError("fitxer no trobat")
            
class Barri:
    def __init__(self, nom, codi_districte):
        if type(codi_districte) != int or codi_districte <= 0:
            raise ValueError("El codi del districte ha de ser un enter positiu.")
        self.nom = nom
        self.codi_districte = codi_districte
    
    def __str__(self):
        return f"Barri: {self.nom}, Codi Districte: {self.codi_districte}"
        
def importar_barris(nom_fitxer):
        try:
            barris = {}
            if type(codi_barri) != int or codi_barri < 0:
                raise TypeError("codi_barri ha de ser un valor positiu")
            with open(nom_fitxer, 'r', encoding='utf-8') as f:
                if f > 1:
                    for linia in f:
                        linia.strip()
            barri = int(input("Codi del barri:"))
            x = Hotel(nom_fitxer)
            if type(barri) != int:
                raise TypeError("El codi del barri ha de ser un enter")
            nom_fitxer.close()
            return f"s'han importat correctament {len(barris)} barris"
        except FileNotFoundError:
            raise FileNotFoundError("fitxer no trobat")
            
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

from classes import importar_hotels, importar_barris, importar_districtes, omplir_llista_barris, mostrar_menu, mostrar_hotels

FITXER_HOTELS = "hotels.csv"
FITXER_BARRIS = "barris.csv"
FITXER_DISTRICTES = "districtes.csv"
SEPARADOR = ';'
AUTORS = "Leo Aguayo, Zhengli Sunshu"

llista_hotels = []
dic_barris = {}
dic_districtes = {}

try:
    llista_hotels = importar_hotels(FITXER_HOTELS, SEPARADOR)
    dic_barris = importar_barris(FITXER_BARRIS, SEPARADOR)
    dic_districtes = importar_districtes(FITXER_DISTRICTES, SEPARADOR)
except FileNotFoundError as e:
    print(f"Error llegint fitxers: {e}")
except Exception as e:
    print(f"Error processant els fitxers: {e}")
else:
    omplir_llista_barris(dic_districtes, dic_barris)
    # Bucle principal del programa ane opcions 4-7
    while True:
        mostrar_menu()
        opcio = input("Introdueix una opció: ").strip()
        if opcio == '1':
            mostrar_hotels(llista_hotels)
        elif opcio in ('S', 's'):
            print("Sortint del programa")
            break
        else:
            print("Opció no permesa")
finally:
    print(f"© {AUTORS}")
