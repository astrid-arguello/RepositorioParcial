import datetime

class Viaje:
    """
    Representa un solo viaje con su ruta, costo, duración y fecha.
    """
    def __init__(self, ruta, costo, duracion, fecha):
        self._ruta = ruta
        self._costo = costo
        self._duracion = duracion
        self._fecha = fecha

    @property
    def ruta(self):
        return self._ruta

    @property
    def costo(self):
        return self._costo

    @property
    def duracion(self):
        return self._duracion

    @property
    def fecha(self):
        return self._fecha

    def __str__(self):
        return (f"Ruta: {self._ruta:<20} | Costo: ${self._costo:<5.2f} | "
                f"Duración: {self._duracion:<3} min | Fecha: {self._fecha.strftime('%d-%m-%Y')}")