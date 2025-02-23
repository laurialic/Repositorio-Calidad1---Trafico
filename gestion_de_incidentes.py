class GestionDeIncidentes:
    def __init__(self):
        self.incidentes = []

    def reportar_incidente(self, descripcion):
        self.incidentes.append(descripcion)
        return f"Incidente reportado: {descripcion}"
