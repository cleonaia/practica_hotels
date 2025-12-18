class Hotel():
    def __init__(self, nom, codi_hotel, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles):
        if type(numero) != int:
            raise TypeError("numero ha de ser un valor enter")
        if numero < 0:
            raise ValueError("numero ha de ser un valor positiu o zero")
        if type(codi_barri) != int:
            raise TypeError("codi_barri ha de ser un valor enter")
        if codi_barri <= 0:
            raise ValueError("codi_barri ha de ser un valor positiu")
        if type(codi_postal) != int:
            raise TypeError("codi_postal ha de ser un valor enter")
        if type(latitud) != float:
            raise TypeError("latitud ha de ser un valor real")
        if type(longitud) != float:
            raise TypeError("longitud ha de ser un valor real")
        if type(estrelles) != int:
            raise TypeError("estrelles ha de ser un valor enter")
        if estrelles not in range(1,6):
            raise ValueError("estrelles ha de ser un valor entre 1 i 5")
        self.nom = str(nom)
        self.codi_hotel = str(codi_hotel)
        self.carrer = str(carrer)
        self.numero = int(numero)
        self.codi_barri = int(codi_barri)
        self.codi_postal = int(codi_postal)
        self.telefon = str(telefon)
        self.latitud = float(latitud)
        self.longitud = float(longitud)
        self.estrelles = int(estrelles)
    def __str__(self):
        return f"{self.nom} ({self.codi_hotel}) {self.carrer},{self.numero} {self.codi_postal} (barri: {self.codi_barri}) {self.telefon} ({self.latitud},{self.longitud}) {self.estrelles} estrelles"

    def __gt__(self, altre_hotel):
        if self.estrelles > altre_hotel.estrelles:
            return True
        else:
            return False
    def distancia(self,latitud2,longitud2):
        if type(latitud2) != float:
            raise TypeError("latitud ha de ser un valor real")
        if type(longitud2) != float:
            raise TypeError("longitud ha de ser un valor real")
        import math
        radi_terra = 6378.137
        latitud1 = self.latitud * math.pi / 180
        longitud1 = self.longitud * math.pi / 180
        latitud2 = latitud2 * math.pi / 180
        longitud2 = longitud2 * math.pi / 180
        dist = math.acos(math.sin(latitud1)*math.sin(latitud2)+math.cos(latitud1)*math.cos(latitud2)*math.cos(longitud2-longitud1))*radi_terra
        return dist

def codi_in_llista_hotels(llista_hotels, codi_hotel):
    for hotel in llista_hotels:
        if hotel.codi_hotel == str(codi_hotel):
            return True
    return False

def importar_hotels(nom_fitxer, separador=';'):
    hotels = []
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as f:
            next(f)  # Skip header
            for linia in f:
                linia = linia.strip()
                if not linia:
                    continue
                dades = linia.split(separador)
                equipament = dades[0].strip()
                
                # Separar nom i codi de l'hotel
                if ' - HB-' in equipament:
                    parts = equipament.split(' - HB-')
                    nom = parts[0].strip()
                    codi_hotel_str = 'HB-' + parts[1]
                else:
                    nom = equipament
                    codi_hotel_str = 'HB-000000'
                
                carrer = dades[1].strip()
                numero = int(dades[2])
                codi_barri = int(dades[3])
                codi_postal = int(dades[4])
                telefon = dades[5].strip()
                latitud = float(dades[6])/1000000
                longitud = float(dades[7])/1000000
                estrelles = int(dades[8])
                
                if not codi_in_llista_hotels(hotels, codi_hotel_str):
                    hotel = Hotel(nom, codi_hotel_str, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles)
                    hotels.append(hotel)
        print(f"S'han importat correctament {len(hotels)} hotels")
        return hotels
    except FileNotFoundError:
        raise FileNotFoundError("fitxer no trobat")
            
class Barri:
    def __init__(self, nom, codi_districte):
        if type(codi_districte) != int or codi_districte <= 0:
            raise TypeError("codi_districte ha de ser un valor enter positiu")
        self.nom = nom
        self.codi_districte = codi_districte
    
    def __str__(self):
        return f"{self.nom} (districte: {self.codi_districte})"
        
def importar_barris(nom_fitxer, separador=';'):
    dic_barris = {}
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as f:
            next(f)  # Skip header
            for linia in f:
                linia = linia.strip()
                if not linia:
                    continue
                dades = linia.split(separador)
                codi_barri = int(dades[0])
                codi_districte = int(dades[1])
                nom_barri = dades[2]
                barri = Barri(nom_barri, codi_districte)
                dic_barris[codi_barri] = barri
        print(f"S'han importat correctament {len(dic_barris)} barris")
        return dic_barris
    except FileNotFoundError:
        raise FileNotFoundError("fitxer no trobat")
            
class Districte:
    def __init__(self, nom, extensio, poblacio):
        if type(poblacio) != int or poblacio <= 0:
            raise TypeError("poblacio ha de ser un valor enter positiu")
        if type(extensio) != float or extensio <= 0:
            raise TypeError("extensio ha de ser un valor real positiu")
        self.nom = nom
        self.extensio = extensio
        self.poblacio = poblacio
        self.llista_barris = []
    def __str__(self):
        str_barris = ", ".join(self.llista_barris) if self.llista_barris else "N/D"
        return f"{self.nom} ({self.extensio} kms2, {self.poblacio} habitants) barris: {str_barris}"
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
    print("\n--- MENÚ PRINCIPAL ---")
    print("1 - Veure hotels")
    print("2 - Veure hotels per estrelles")
    print("3 - Buscar hotels")
    print("4 - Buscar hotel proper")
    print("5 - Llistat alfabetic d'hotels")
    print("6 - Carrers amb hotels")
    print("7 - Estadistica per barris")
    print("8 - Estadistica per districtes") 
    print("9 -Internacionalitzar per telefons")
    print("S - Sortir del programa")

def mostrar_hotels(llista_hotels):
    if not llista_hotels:
        print("No hi ha hotels")
        return
    for hotel in llista_hotels:
        print(hotel)

def ordenar_per_estrelles(llista_hotels):
    llista_copia = llista_hotels.copy()
    llista_copia.sort(key=lambda h: h.estrelles)
    return llista_copia

def mostrar_noms_hotels(llista_hotels):
    for hotel in llista_hotels:
        print(f"{hotel.nom} ({hotel.codi_hotel})")

def buscar_per_nom(llista_hotels, nom_buscar):
    nom_buscar_lower = nom_buscar.lower()
    resultats = [h for h in llista_hotels if nom_buscar_lower in h.nom.lower()]
    return resultats

def buscar_per_estrelles(llista_hotels, estrelles):
    resultats = list(filter(lambda h: h.estrelles == estrelles, llista_hotels))
    return resultats

def buscar_hotels(llista_hotels):
    criteri = input("Introdueix criteri de cerca (1 - per nom, 2 - per estrelles): ").strip()
    
    if criteri == '1':
        nom = input("Introdueix el nom de l'hotel a buscar: ").strip()
        resultats = buscar_per_nom(llista_hotels, nom)
        if resultats:
            print(f"S'han trobat {len(resultats)} hotels amb aquest nom")
            mostrar_noms_hotels(resultats)
        else:
            print("No s'han trobat hotels")
    
    elif criteri == '2':
        while True:
            try:
                estrelles = int(input("Introdueix el número d'estrelles a buscar: ").strip())
                if estrelles not in range(1, 6):
                    print("Error: el número d'estrelles ha de ser un valor entre 1 i 5")
                    continue
                break
            except ValueError:
                print("Error: el número d'estrelles ha de ser un valor enter")
        
        resultats = buscar_per_estrelles(llista_hotels, estrelles)
        if resultats:
            print(f"S'han trobat {len(resultats)} hotels de {estrelles} estrelles")
            mostrar_noms_hotels(resultats)
        else:
            print("No s'han trobat hotels")
    
    else:
        print("Error: criteri de cerca no vàlid")

def hotel_mes_proper(llista_hotels, latitud, longitud):
    if not llista_hotels:
        return None, None
    
    hotel_min = llista_hotels[0]
    dist_min = hotel_min.distancia(latitud, longitud)
    
    for hotel in llista_hotels[1:]:
        dist = hotel.distancia(latitud, longitud)
        if dist < dist_min:
            dist_min = dist
            hotel_min = hotel
    
    return hotel_min, dist_min
def ordenar_per_nom(llista_hotels):
    llista_copia = list(llista_hotels.copy())
    llista_copia.sort(key=lambda hotel: hotel.nom)
    return llista_copia
def carrers_amb_hotels(llista_hotels):
    noms_carrers = set()
    for hotel in llista_hotels:
        noms_carrers.add(hotel.carrer)
    return noms_carrers
def estrelles_per_barri(llista_hotels,codi_barri):
    diccionari = codi_barri.copy()
    for hotel in llista_hotels:
        codi = llista_hotels.codi_barri
        llista_hotels = diccionari[codi].nom
        diccionari[codi_barri] = llista_hotels
    return diccionari
def densitat_per_districte(llista_hotels, codi_barri, codi_districte):
    diccionari = {}
    for hotel in llista_hotels:
        suma = 0
        if hotel in codi_barri and hotel in codi_districte:
            suma += 1
    for diccionari in range(len(diccionari)):
        suma1 = 0
        for i in diccionari:
            suma1 += int(diccionari[i])
    return suma1/len(diccionari)

def carrers_amb_hotel(llista_hotels):
    carrets = set()
    for hotel in llista_hotels:
        carrets.add(hotel.carrer)
    return list(carets)

def afegir_prefixe_int(self):
    if len(self.telefon) == 0 or self.telefon[0] != '+':
        self.telefon = '+34' + self.telefon
    return self.telefon


def modficiar_telefon(llista_hotels):
    list(map(lambda hotel: afegir_prefixe_int(hotel), llista_hotels))
