# Documentación de Pruebas Unitarias: Sistema de Control de Tráfico

## Objetivo
Diseñar e implementar pruebas unitarias para validar el correcto funcionamiento de los componentes clave del sistema de control de tráfico. Estas pruebas aseguran una cobertura adecuada y la detección oportuna de errores. Se han implementado en **Python** utilizando **pytest** y están disponibles en el repositorio de Git del proyecto.

---

## Estructura del Proyecto
```
├── sistema_trafico.py          # Código principal del sistema
├── test_sistema_trafico.py     # Archivo con las pruebas unitarias
├── README.md                   # Documentación del proyecto
└── requirements.txt            # Dependencias del proyecto
```

---

## Descripción de las Pruebas Unitarias

### 1. test_semaforo_cambiar_estado
- **Propósito:** Verificar que el semáforo cambia de estado correctamente y maneja estados inválidos.
- **Caso de uso relacionado:** Cambio de luces en el semáforo para regular el flujo de tráfico.
- **Cobertura:**
  - Cambios válidos: `rojo → verde → amarillo`.
  - Manejo de estado inválido (por ejemplo, `"azul"`).

---

### 2. test_semaforo_estado_inicial
- **Propósito:** Asegurar que el semáforo se inicializa en el estado `rojo` por defecto.
- **Caso de uso relacionado:** Seguridad vial al iniciar o reiniciar el sistema.
- **Cobertura:**
  - Verificación del estado inicial de un semáforo recién creado.

---

### 3. test_controlador_agregar_semaforo
- **Propósito:** Validar que el controlador pueda agregar semáforos correctamente.
- **Caso de uso relacionado:** Gestión y expansión del sistema de tráfico mediante la adición de nuevos semáforos.
- **Cobertura:**
  - Verificación de la lista de semáforos del controlador tras la adición.

---

### 4. test_controlador_cambiar_estados
- **Propósito:** Comprobar que el controlador puede cambiar el estado de todos los semáforos simultáneamente y manejar estados inválidos.
- **Caso de uso relacionado:** Sincronización del tráfico en intersecciones.
- **Cobertura:**
  - Cambio de estado válido en todos los semáforos.
  - Manejo de entrada inválida al cambiar el estado.

---

## Instrucciones para Ejecutar las Pruebas

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar las pruebas:
```bash
pytest test_sistema_trafico.py
```

3. Interpretar resultados:
- Los tests exitosos se marcarán en verde.
- Cualquier fallo se detallará en la salida de `pytest` para su revisión.

---

## Notas Finales
- Se garantiza la cobertura de diferentes caminos y condiciones posibles en los casos de uso seleccionados.
- Las pruebas se han diseñado para ser claras, concisas y fáciles de mantener.
- El proyecto se encuentra disponible en el repositorio de Git para su revisión.
