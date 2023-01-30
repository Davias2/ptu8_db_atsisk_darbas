from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///db_darbas/sefo_peiliai.db')
Base = declarative_base()


class Pirkejas(Base):
    __tablename__ = "pirkejas"
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    el_pastas = Column(String)
    uzsakymai = relationship("Uzsakymas", back_populates="pirkejas")
    
    def __str__(self):
        return f"ID {self.id}: vardas {self.vardas}, pavarde {self.pavarde}, el_pastas {self.el_pastas}"
        

class Uzsakymas(Base):
    __tablename__ = "uzsakymas"
    id = Column(Integer, primary_key=True)
    pirkejas_id = Column(Integer, ForeignKey("pirkejas.id"))
    pirkejas = relationship("Pirkejas", back_populates="uzsakymai")
    data = Column(DateTime)
    statusas = Column(String)
    gaminio_uzsakymai = relationship("GaminioUzsakymas", back_populates="uzsakymas")

    def __str__(self):
        return f"ID {self.id}: pirkejas {self.pirkejas.vardas}, data {self.data}, statusas {self.statusas}"


class Gaminys(Base):
    __tablename__ = "gaminys"
    id = Column(Integer, primary_key=True)
    modelis = Column(String)
    rankenos_medziaga = Column(String)
    geleztes_ilgis_mm = Column(Integer)
    kaina_eurai = Column(Float)
    gaminio_uzsakymai = relationship("GaminioUzsakymas", back_populates="gaminys")
        
    def __str__(self):
        return f"ID {self.id}: modelis {self.modelis}, rankenos_medziaga {self.rankenos_medziaga}, geleztes_ilgis_mm {self.geleztes_ilgis_mm}, kaina_eurai {self.kaina_eurai}"
        

class GaminioUzsakymas(Base):
    __tablename__ = "gaminio_uzsakymas"
    id = Column(Integer, primary_key=True)
    uzsakymas_id = Column(Integer, ForeignKey("uzsakymas.id"))
    uzsakymas = relationship("Uzsakymas", back_populates="gaminio_uzsakymai")
    gaminys_id = Column(Integer, ForeignKey("gaminys.id"))
    gaminys = relationship("Gaminys", back_populates="gaminio_uzsakymai")
    kiekis = Column(Integer)

    def __str__(self):
        return f"ID {self.id}: uzsakymo id {self.uzsakymas_id}, gaminys {self.gaminys.modelis}, kiekis {self.kiekis}"

if __name__ == "__main__":
    Base.metadata.create_all(engine)