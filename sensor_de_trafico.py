class SensorDeTrafico:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.volumen_vehicular = 0

    def detectar_trafico(self, volumen):
        self.volumen_vehicular = volumen
        return f"Volumen detectado en {self.ubicacion}: {volumen} vehículos."
