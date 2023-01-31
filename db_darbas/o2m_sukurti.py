from sqlalchemy.orm import sessionmaker
from o2m_module import Pirkejas, Uzsakymas, Gaminys, GaminioUzsakymas, Medziaga, engine
from datetime import datetime
session = sessionmaker(bind=engine)()

gyuto = Gaminys(modelis="Gyuto: universalus", geleztes_ilgis_mm="210", kaina_eurai="185")
santoku = Gaminys(modelis="Santoku: mesai, zuvei, darzovems", geleztes_ilgis_mm="180", kaina_eurai="168")
kiritsuke = Gaminys(modelis="Kiritsuke: zuvei", geleztes_ilgis_mm="290", kaina_eurai="195")
bunka = Gaminys(modelis="Bunka: universalus", geleztes_ilgis_mm="175", kaina_eurai="129")
petty = Gaminys(modelis="Petty: zolelems, darzovems", geleztes_ilgis_mm="160", kaina_eurai="111")
paring = Gaminys(modelis="Paring: grybams", geleztes_ilgis_mm="145", kaina_eurai="93")
nakiri = Gaminys(modelis="Nakiri: darzovems", geleztes_ilgis_mm="165", kaina_eurai="124")
usuba = Gaminys(modelis="Usuba: darzoves", geleztes_ilgis_mm="180", kaina_eurai="197")
deba = Gaminys(modelis="Deba: zuvei, mesai", geleztes_ilgis_mm="150", kaina_eurai="120")
yanagi = Gaminys(modelis="Yanagi: zuvei", geleztes_ilgis_mm="260", kaina_eurai="235")
sujihiki = Gaminys(modelis="Sujuhiki: mesai", geleztes_ilgis_mm="240", kaina_eurai="218")
honesuki = Gaminys(modelis="Honesuki: nukaulinti kaulus", geleztes_ilgis_mm="160", kaina_eurai="160")
hankotsu = Gaminys(modelis="Hankotsu: nukaulinti karkasa", geleztes_ilgis_mm="145", kaina_eurai="120")

medziaga1 = Medziaga(pavadinimas="Triskiautė magnolija")
medziaga2 = Medziaga(pavadinimas="Europinis kukmedis")
medziaga3 = Medziaga(pavadinimas="Afrikos juodmedis")

vartotojas = Pirkejas(vardas="Jonas", pavarde="Jonaitis", el_pastas="JJ@gmail.com")
uzsakymas = Uzsakymas(pirkejas=vartotojas, data=datetime.now(), statusas="vykdomas")

p_uzsakymas = GaminioUzsakymas(uzsakymas=uzsakymas, gaminys=gyuto, kiekis=2)

session.add_all([gyuto, santoku, kiritsuke, bunka, petty, paring, nakiri, usuba, deba, yanagi, sujihiki, honesuki, hankotsu])
session.add_all([medziaga1, medziaga2, medziaga3])
session.add(vartotojas)
session.add(uzsakymas)
session.add(p_uzsakymas)
session.commit()
