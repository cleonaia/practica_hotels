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



    def hotel_mes_proper(hotels, latitud, longitud): 



    def mostrar_menu():
        print("---MENÚ PRINCIPAL---")
        print("1 - Veure hotels")
        print("2 - Veure hotels per estrelles")
        print("3 - Buscar hotels")
        print("4 - Buscar hotel proper")
        print("S - Sortir")

