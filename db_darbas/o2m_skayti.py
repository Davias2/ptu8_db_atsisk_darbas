from o2m_module import Pirkejas, Uzsakymas, Gaminys, GaminioUzsakymas, Medziaga, engine
from sqlalchemy.orm import sessionmaker


session = sessionmaker(bind=engine)()

def menu():
    print("---{ Sefo peiliai }---")
    print("Pasirinkite: ")
    print("|1| Pradekite nauja pirkima")
    print("|2| perziureti medziagas")
    print("|3| perziureti prekiu sarasa")
    print("|4| perziureti gaminiu uzsakymu sarasa")
    print("|5| papildyti uzsakyma")
    print("|6| istrinti uzsakyma")
    print("|0| iseiti")
    pasirinkimas = input("Pasirinkite: ")
    return pasirinkimas

def naujas_pirkimas():
    i_vardas = input("Vardas: ")
    i_pavarde = input("Pavarde: ")
    i_el_pastas = input("Elektroninis pastas: ")
    naujas_pirkejas = Pirkejas(vardas=i_vardas, pavarde=i_pavarde, el_pastas=i_el_pastas)
    prekiu_sarasas()
    i_gaminys = int(input("Gaminio ID: "))
    perziureti_medziagas()
    i_medziaga = int(input("Rankenos medziaga id: "))
    i_kiekis = int(input("Iveskite norima kieki: "))
    naujas_gaminys = GaminioUzsakymas(gaminys_id=i_gaminys, kiekis=i_kiekis, medziaga_id=i_medziaga)
    session.add(naujas_pirkejas)
    session.add(naujas_gaminys)
    session.commit()
    print("Pirkejas ir gaminys prideti! ")

def perziureti_medziagas():
    medziagos = session.query(Medziaga).all()
    for medziaga in medziagos:
        print(medziaga.id, medziaga.pavadinimas)

def prekiu_sarasas():
    gaminiai = session.query(Gaminys).all()
    for gaminys in gaminiai:
        print(gaminys.id, gaminys.modelis, gaminys.geleztes_ilgis_mm, gaminys.kaina_eurai)

def gaminiu_uzsakymu_sarasas(query=session.query(GaminioUzsakymas)):
    if query and len(query.all()) > 0:
        for naujas_pirkinys in query.all():
            print(naujas_pirkinys)
# def uzsakymu_sarasas():
#     g_uzsakymai = session.query(GaminioUzsakymas).all()
#     for g_uzsakymas in g_uzsakymai:
#        print(g_uzsakymas.id, g_uzsakymas.uzsakymas, g_uzsakymas.gaminys, g_uzsakymas.kiekis)

def gauti_uzsakymo_id():
    gaminiu_uzsakymu_sarasas()
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
        perziureti_medziagas()
    elif pasirinkimas == "3":
        prekiu_sarasas()
    elif pasirinkimas == "4":
        gaminiu_uzsakymu_sarasas()
    elif pasirinkimas == "5":
        uzsakymas = gauti_uzsakymo_id()
        papildyti_uzsakyma(uzsakymas, **atlikti_pakeitimai(uzsakymas))
    elif pasirinkimas == "6":
        istrinti_uzsakyma(gauti_uzsakymo_id())
    else:
        print(f"Error: neteisingas pasirinkimas {pasirinkimas}")