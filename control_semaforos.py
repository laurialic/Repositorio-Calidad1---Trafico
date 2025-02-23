class ControlSemaforos:
    def __init__(self, sensor):
        self.sensor = sensor
        self.tiempo_verde = 30

    def ajustar_tiempo(self):
        if self.sensor.volumen_vehicular > 50:
            self.tiempo_verde = 60
        else:
            self.tiempo_verde = 30
        return self.tiempo_verde
