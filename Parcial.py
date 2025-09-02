
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

def obtener_entrada_validada(mensaje, tipo, limite=None):
    """
    Función auxiliar para validar la entrada del usuario.
    """
    while True:
        try:
            entrada = tipo(input(mensaje))
            if limite is not None and entrada <= 0:
                print("⚠️ El valor debe ser positivo. Intenta de nuevo.")
                continue
            return entrada
        except ValueError:
            print("❌ Entrada inválida. Por favor, introduce un número válido.")

def main():
    """
    Función principal que ejecuta el programa.
    """
    registro = RegistroDeViajes()
    
    # Datos de ejemplo para probar el programa
    ejemplo_viaje1 = Viaje("Ruta 42", 0.25, 30, datetime.datetime(2025, 9, 2))
    ejemplo_viaje2 = Viaje("Ruta 29", 0.50, 45, datetime.datetime(2025, 8, 30))
    ejemplo_viaje3 = Viaje("Ruta 33-A", 0.35, 20, datetime.datetime(2025, 9, 1))
    
    registro.agregar_viaje(ejemplo_viaje1)
    registro.agregar_viaje(ejemplo_viaje2)
    registro.agregar_viaje(ejemplo_viaje3)

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar un nuevo viaje")
        print("2. Ver resumen de la última semana")
        print("3. Ver todos los viajes")
        print("4. Salir")
        
        opcion = obtener_entrada_validada("Selecciona una opción: ", int)

        if opcion == 1:
            print("\n--- Nuevo Viaje ---")
            ruta = input("Nombre de la ruta: ")
            costo = obtener_entrada_validada("Costo del pasaje ($): ", float, limite=0)
            duracion = obtener_entrada_validada("Duración del viaje (minutos): ", int, limite=0)
            fecha_str = input("Fecha del viaje (dd-mm-yyyy): ")
            try:
                fecha = datetime.datetime.strptime(fecha_str, '%d-%m-%Y')
                nuevo_viaje = Viaje(ruta, costo, duracion, fecha)
                registro.agregar_viaje(nuevo_viaje)
            except ValueError:
                print("❌ Formato de fecha incorrecto. Usa dd-mm-yyyy.")

        elif opcion == 2:
            registro.mostrar_resumen_semanal()

        elif opcion == 3:
            registro.mostrar_todos_los_viajes()

        elif opcion == 4:
            print("¡Gracias por usar el sistema! 👋")
            break

        else:
            print("⚠️ Opción no válida. Por favor, selecciona del 1 al 4.")

if __name__ == "__main__":
    main()