from o2m_module import Pirkejas, Uzsakymas, Gaminys, Medziaga, engine
from sqlalchemy.orm import sessionmaker


session = sessionmaker(bind=engine)()

def menu():
    print("---{ Sefo peiliai }---")
    print("Pasirinkite: ")
    print("|1| Perziureti gaminius")
    print("|2| Perziureti medziagas")
    print("|3| Pradeti nauja uzsakyma")
    print("|4| Perziureti uzsakymus")
    print("|5| Perziureti pirkeju sarasa")
    print("|6| Istrinti uzsakyma")
    print("|0| iseiti")
    pasirinkimas = input("Pasirinkite: ")
    return pasirinkimas

def perziureti_gaminius():
    gaminiai = session.query(Gaminys).all()
    for gaminys in gaminiai:
        print(gaminys.id, gaminys.modelis, gaminys.geleztes_ilgis_mm, gaminys.kaina_eurai)

def perziureti_medziagas():
    medziagos = session.query(Medziaga).all()
    for medziaga in medziagos:
        print(medziaga.id, medziaga.pavadinimas)

def naujas_uzsakymas():
    i_vardas = input("Vardas: ")
    i_pavarde = input("Pavarde: ")
    i_el_pastas = input("Elektroninis pastas: ")
    naujas_pirkejas = Pirkejas(vardas=i_vardas, pavarde=i_pavarde, el_pastas=i_el_pastas)
    perziureti_gaminius()
    i_gaminys = int(input("Pasirinkite gaminio ID: "))
    perziureti_medziagas()
    i_medziaga = int(input("Rankenos medziaga ID: "))
    i_kiekis = int(input("Iveskite norima kieki: "))
    naujas_uzsakymas = Uzsakymas(pirkejas=naujas_pirkejas, gaminys_id=i_gaminys, medziaga_id=i_medziaga, kiekis=i_kiekis)
    session.add(naujas_pirkejas)
    session.add(naujas_uzsakymas)
    session.commit()
    print("Pirkejas ir gaminys prideti! ")

def perziureti_uzsakymus(query=session.query(Uzsakymas)):
    if query and len(query.all()) > 0:
        for naujas_uzsakymas in query.all():
            print(naujas_uzsakymas)
    else:
        print("Uzsakymas nebuvo rastas!")

def perziureti_pirkeju_sarasa():
    pirkejai = session.query(Pirkejas).all()
    for pirkejas in pirkejai:
        print(pirkejas.id, pirkejas.vardas, pirkejas.pavarde, pirkejas.el_pastas)

def gauti_uzsakymo_id():
    perziureti_uzsakymus()
    try:
        id = int(input("Iveskite uzsakymo ID: "))
    except ValueError:
        print("Error: ID turi buti skaicius")
    else:
        return session.query(Uzsakymas).filter_by(id=id).one()

def istrinti_uzsakyma(uzsakymas):
    print(f"Uzsakymas buvo sekmingai pasalintas kurio ID {uzsakymas.id}")
    session.delete(uzsakymas)
    session.commit()

while True:
    pasirinkimas = menu()
    if pasirinkimas == "0" or pasirinkimas == "":
        break
    elif pasirinkimas == "1":
        perziureti_gaminius()
    elif pasirinkimas == "2":
        perziureti_medziagas()
    elif pasirinkimas == "3":
        naujas_uzsakymas()
    elif pasirinkimas == "4":
        perziureti_uzsakymus()
    elif pasirinkimas == "5":
        perziureti_pirkeju_sarasa()
    elif pasirinkimas == "6":
        istrinti_uzsakyma(gauti_uzsakymo_id())
    else:
        print(f"Error: neteisingas pasirinkimas {pasirinkimas}")