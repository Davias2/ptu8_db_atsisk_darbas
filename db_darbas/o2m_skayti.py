from o2m_module import Pirkejas, Uzsakymas, Gaminys, GaminioUzsakymas, engine
from sqlalchemy.orm import sessionmaker


session = sessionmaker(bind=engine)()

def menu():
    print("---{ Sefo peiliai }---")
    print("Pasirinkite: ")
    print("|1| Pradekite nauja pirkima")
    print("|2| perziureti prekiu sarasa")
    print("|3| perziureti uzsakymu sarasa")
    print("|4| papildyti uzsakyma")
    print("|5| istrinti uzsakyma")
    print("|0| iseiti")
    pasirinkimas = input("Pasirinkite: ")
    return pasirinkimas

def naujas_pirkimas():
    i_vardas = input("Vardas: ")
    i_pavarde = input("Pavarde: ")
    i_el_pastas = input("Elektroninis pastas: ")
    naujas_pirkejas = Pirkejas(vardas=i_vardas, pavarde=i_pavarde, el_pastas=i_el_pastas)
    session.add(naujas_pirkejas)
    session.commit()
    print("Pirkejas pridetas! ")

def prekiu_sarasas():
    gaminiai = session.query(Gaminys).all()
    for gaminys in gaminiai:
        print(gaminys.id, gaminys.modelis, gaminys.rankenos_medziaga, gaminys.geleztes_ilgis_mm, gaminys.kaina_eurai)

def uzsakymu_sarasas():
    g_uzsakymai = session.query(GaminioUzsakymas).all()
    for g_uzsakymas in g_uzsakymai:
        print(g_uzsakymas.id, g_uzsakymas.uzsakymas.pirkejas, g_uzsakymas.gaminys.modelis, g_uzsakymas.kiekis)

def gauti_uzsakymo_id():
    uzsakymu_sarasas()
    try:
        id = int(input("Iveskite uzsakymo id: "))
    except ValueError:
        print("Error: ID turi buti skaicius")
    else:
        return session.query(Uzsakymas).filter_by(id=id).one()

def papildyti_uzsakyma(uzsakymas, **pakeitimai):
    for column, value in pakeitimai.items():
        if value:
            setattr(uzsakymas, column, value)
    session.commit()
    print(uzsakymas)

def atlikti_pakeitimai(uzsakymas):
    print(uzsakymas)
    print("Iveskite norimus pakeitimus")
    prekiu_sarasas()
    paketimimai = {
        "gaminys": input("Gaminys: "),
        "kiekis": int(input("Kiekis: "))
    }
    return paketimimai

def istrinti_uzsakyma(uzsakymas):
    print(f"Uzsakymas buvo sekmingai pasalintas kurio id {uzsakymas.id}!")
    session.delete(uzsakymas)
    session.commit()

while True:
    pasirinkimas = menu()
    if pasirinkimas == "0" or pasirinkimas == "":
        break
    elif pasirinkimas == "1":
        naujas_pirkimas()
    elif pasirinkimas == "2":
        prekiu_sarasas()
    elif pasirinkimas == "3":
        uzsakymu_sarasas()
    elif pasirinkimas == "4":
        uzsakymas = gauti_uzsakymo_id()
        papildyti_uzsakyma(uzsakymas, **atlikti_pakeitimai(uzsakymas))
    elif pasirinkimas == "5":
        istrinti_uzsakyma(gauti_uzsakymo_id())
    else:
        print(f"Error: neteisingas pasirinkimas {pasirinkimas}")