
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

    

