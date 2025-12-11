from classes import importar_hotels, importar_barris, importar_districtes, omplir_llista_barris, mostrar_menu

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
