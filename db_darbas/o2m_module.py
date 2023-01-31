from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
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
    gaminys_id = Column(Integer, ForeignKey("gaminys.id"))
    gaminys = relationship("Gaminys", back_populates="uzsakymai")
    medziaga_id = Column(Integer, ForeignKey("medziaga.id"))
    medziaga = relationship("Medziaga", back_populates="uzsakymai")
    kiekis = Column(Integer)
    
    def __str__(self):
        return f"ID {self.id}: pirkejo {self.pirkejas}, gaminio {self.gaminys}, rankenos medziagos {self.medziaga}, kiekis {self.kiekis}"


class Gaminys(Base):
    __tablename__ = "gaminys"
    id = Column(Integer, primary_key=True)
    modelis = Column(String)
    geleztes_ilgis_mm = Column(Integer)
    kaina_eurai = Column(Float)
    uzsakymai = relationship("Uzsakymas", back_populates="gaminys")
        
    def __str__(self):
        return f"ID {self.id}: modelis = {self.modelis}, geleztes ilgis mm = {self.geleztes_ilgis_mm}, kaina eurai = {self.kaina_eurai}"
        

class Medziaga(Base):
    __tablename__ = "medziaga"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)
    uzsakymai = relationship("Uzsakymas", back_populates="medziaga")

    def __str__(self):
        return f"ID {self.id}: pavadinimas {self.pavadinimas}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)