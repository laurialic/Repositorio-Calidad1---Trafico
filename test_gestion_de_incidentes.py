import unittest
from gestion_de_incidentes import GestionDeIncidentes

class TestGestionDeIncidentes(unittest.TestCase):
    def test_reportar_incidente(self):
        gestion = GestionDeIncidentes()
        resultado = gestion.reportar_incidente("Accidente menor en calle 5")
        self.assertIn("Accidente menor", resultado)
        self.assertEqual(len(gestion.incidentes), 1)

if __name__ == '__main__':
    unittest.main()
