import datetime

class RegistroDeViajes:
    """
    Gestiona una colección de viajes y calcula estadísticas.
    """
    def __init__(self):
        self._viajes = []

    def agregar_viaje(self, viaje):
        self._viajes.append(viaje)
        print("✅ ¡Viaje registrado con éxito!")

    def _obtener_viajes_semanales(self):
        hoy = datetime.date.today()
        hace_siete_dias = hoy - datetime.timedelta(days=7)
        return [viaje for viaje in self._viajes if hace_siete_dias <= viaje.fecha.date() <= hoy]

    def mostrar_resumen_semanal(self):
        viajes_semanales = self._obtener_viajes_semanales()
        if not viajes_semanales:
            print("🚫 No hay viajes registrados en la última semana.")
            return

        gasto_total = sum(v.costo for v in viajes_semanales)
        tiempo_total = sum(v.duracion for v in viajes_semanales)

        print("\n--- Resumen Semanal ---")
        print(f"💰 Gasto total: ${gasto_total:.2f}")
        print(f"⏱️ Tiempo total invertido: {tiempo_total} minutos\n")

    def mostrar_todos_los_viajes(self):
        if not self._viajes:
            print("🚫 Aún no has registrado ningún viaje.")
            return

        print("\n--- Viajes Registrados ---")
        # Ordenar por fecha, de más reciente a más antigua
        viajes_ordenados = sorted(self._viajes, key=lambda v: v.fecha, reverse=True)
        for viaje in viajes_ordenados:
            print(viaje)
        print("----------------------------\n")