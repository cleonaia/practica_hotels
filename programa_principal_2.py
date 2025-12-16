class Hotel:
    def __init__(self, nom, estrelles):
        self.nom = nom
        self.estrelles = estrelles

    def ordenar_per_estrelles(ll_hotels):
        ll_hotels2 = ll_hotels.copy()
        def hotels(h): 
            return h.estrelles
        ll_hotels2.sort(key= hotels, reverse=True)
        return ll_hotels2

    def mostrar_nom_hotels(ll_hotels):
        for hotel in ll_hotels:
            print(f"nom: {hotel.nom} codi: {hotel.estrelles}")
    def buscar_per_nom(ll_hotels, nom):
        llista = []
        for hotel in ll_hotels:
            if nom.lower() in hotel.nom.lower():
                llista.append(hotel.nom)
        return llista
    def buscar_per_estrelles(ll_hotels, estrelles):
        llista = []
        for hotel in ll_hotels:
            if hotel.estrelles == estrelles:
                llista.append(hotel.nom)
        return llista
                
    def buscar_hotels():
    criteri = input("Introdueix criteri de cerca (1 - per nom, 2 - per estrelles): ").strip()

    if criteri == '1':
        nom = input("Introudueix el nom de l'hotel a buscar:")
        resultats = buscar_per_nom(hotels, nom)
        if resultats:
            print(f"S'han trobat {len(resultats)} hotels amb aquest nom")
            mostrar_noms_hotels(resultats)
        else:
            print("No s'han trobat hotels")
    elif criteri == '2':
        while True:
            valor = input("Introdueix el número d'estrelles a buscar:").strip()
            try:
                n = int(valor)
            except ValueError:
                print("Error: el número d'estrelles ha de ser un valor enter")
                continue
            if not (1 <= n <= 5):
                print("Error: el número d'estrelles ha de ser un valor entre 1 i 5")
                continue
            resultats = buscar_per_estrelles(hotels, n)
            if resultats:
                print(f"S'han trobat {len(resultats)} hotels de {n} estrelles")
                mostrar_noms_hotels(resultats)
            else:
                print("No s'han trobat hotels")
            break
    else:
        print("Error: criteri de cerca no vàlid")



    def hotel_mes_proper(ll_hotels, latitud, longitud):
        for hotel in ll_hotels:
            if not min(ll_hotels,key = distancia):
                return None, None
            else:
                return min(ll_hotels,key = distancia)


    def mostrar_menu():
        print("---MENÚ PRINCIPAL---")
        print("1 - Veure hotels")
        print("2 - Veure hotels per estrelles")
        print("3 - Buscar hotels")
        print("4 - Buscar hotel proper")
        print("S - Sortir")


from classes import importar_hotels, importar_barris, importar_districtes, omplir_llista_barris, mostrar_menu, mostrar_hotels
FITXER_HOTELS = "hotels.csv"
FITXER_BARRIS = "barris.csv"
FITXER_DISTRICTES = "districtes.csv"
SEPARADOR = ';'
AUTORS = "Leo Aguayo, Zhengli Sunzhu"

llista_hotels = []
dicc_barris = {}
dicc_districtes = {}

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

    opcio = ''

    while opcio.upper() != 'S':
        mostrar_menu()
        opcio = input("Introdueix una opció: ").strip()

        if opcio == '1':
            mostrar_hotels(llista_hotels)
        elif opcio == '2':
            hotels_ordenats = Hotel.ordenar_per_estrelles(llista_hotels)
            mostrar_hotels(hotels_ordenats)
        elif opcio == '3':
            buscar_hotels(llista_hotels)
        elif opcio == '4':
            try:
                latitut = float(input("Introdueix la latitud: ").strip())
                longitud = float(input("Introdueix la longitud: ").strip())
                hotel_proper = hotel_mes_proper(llista_hotels, latitut, longitud)
                if hotel_proper:
                    print("L'hotel més proper és:")
                    mostrar_hotels([hotel_proper])
                else:
                    print("No hi ha hotels a la llista.")
            except ValueError:
                print("Error: latitud i longitud han de ser valors numèrics.")
        elif opcio.upper() == 'S':
            print("Sortint del programa")
        else:
            print("Opció no permesa")
finally:
    print(f"© {AUTORS}")
