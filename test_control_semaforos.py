import unittest
from sensor_de_trafico import SensorDeTrafico
from control_semaforos import ControlSemaforos

class TestControlSemaforos(unittest.TestCase):
    def test_ajustar_tiempo(self):
        sensor = SensorDeTrafico("Avenida Central")
        control = ControlSemaforos(sensor)
        sensor.detectar_trafico(70)
        self.assertEqual(control.ajustar_tiempo(), 60)
        sensor.detectar_trafico(30)
        self.assertEqual(control.ajustar_tiempo(), 30)

if __name__ == '__main__':
    unittest.main()
