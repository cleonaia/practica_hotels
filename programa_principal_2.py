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
