from deportista import Deportista
from persona import Persona

class Futbolista (Persona, Deportista):
    listaFutbolistas = []
    # Inicializador
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados =   golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)
    
    # Método toString
    def __str__(self):
        mensaje = f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"
        return mensaje
    
    # Métodos get y set.
    # GolesMarcados
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setDeporte(self, golesMarcados):
        self._golesMarcados = golesMarcados
    
    # TarjetasRojas
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    # PiernaHabil
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil    

    # Lista Futbolista
    @classmethod
    def getListaFutbolistas(cls):
        return cls.listaFutbolistas
    
    @classmethod
    def setListaFutbolistas(cls, listaFutbolistas):
        cls.listaFutbolistas = listaFutbolistas