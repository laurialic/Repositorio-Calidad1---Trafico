import unittest
from sensor_de_trafico import SensorDeTrafico

class TestSensorDeTrafico(unittest.TestCase):
    def test_detectar_trafico(self):
        sensor = SensorDeTrafico("Avenida Central")
        resultado = sensor.detectar_trafico(70)
        self.assertEqual(sensor.volumen_vehicular, 70)
        self.assertIn("70 vehículos", resultado)

if __name__ == '__main__':
    unittest.main()
