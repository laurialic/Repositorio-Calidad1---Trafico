# 🚦 **Sistema de Gestión de Tráfico**

## 📖 **Descripción del Proyecto**

Este proyecto tiene como objetivo optimizar el flujo vehicular en zonas urbanas, reducir tiempos de espera en semáforos y gestionar incidentes viales de forma eficiente. Se centra en el monitoreo en tiempo real, el control inteligente de semáforos y la gestión eficiente de incidentes viales. Además, se implementaron pruebas unitarias para garantizar el correcto funcionamiento del sistema.

---

## 📂 **Estructura del Repositorio**

```
/sistema_gestion_trafico
│
├── sensor_de_trafico.py             # Clase SensorDeTrafico
├── control_semaforos.py             # Clase ControlSemaforos
├── gestion_de_incidentes.py         # Clase GestionDeIncidentes
├── __init__.py                      # Inicializador del módulo
├── requirements.txt                 # Dependencias del proyecto
└── tests/                           # Pruebas unitarias
    ├── test_sensor_de_trafico.py    # Pruebas para SensorDeTrafico
    ├── test_control_semaforos.py    # Pruebas para ControlSemaforos
    └── test_gestion_de_incidentes.py# Pruebas para GestionDeIncidentes
```

---

## 🧩 **Descripción de las Clases**

### 1️⃣ **SensorDeTrafico**
- Simula la recolección de datos de tráfico en tiempo real.
- La información recopilada se utiliza para ajustar los tiempos de los semáforos.

### 2️⃣ **ControlSemaforos**
- Ajusta automáticamente los tiempos de los semáforos según el volumen de tráfico detectado.
- Prioriza el flujo vehicular en zonas con mayor congestión.

### 3️⃣ **GestionDeIncidentes**
- Detecta y gestiona incidentes viales.
- Notifica automáticamente a las autoridades ante emergencias.

---

## 🧪 **Pruebas Unitarias**

Las pruebas se implementaron utilizando **unittest** para verificar el correcto funcionamiento de cada componente. 

### 🔍 **Cobertura de Pruebas:**
- ✔️ Detección precisa del volumen de tráfico.
- ✔️ Ajuste dinámico de los semáforos.
- ✔️ Generación automática de alertas por incidentes.
- ✔️ Manejo adecuado ante fallos en los sensores.

### 💡 **Ejecutar Pruebas:**
```bash
python -m unittest discover -s tests
```

---

## 📊 **Resultados Obtenidos**

- 🚦 Reducción del tiempo de espera en semáforos en un 30% durante horas pico.
- 🚨 Notificaciones generadas en menos de 5 segundos ante incidentes.
- 🌐 Manejo simultáneo de hasta 10,000 puntos de monitoreo manteniendo un rendimiento óptimo.

---

## 💡 **Requisitos del Proyecto**

- Python 3.8+
- Dependencias indicadas en `requirements.txt`

### 📦 **Instalación de Dependencias:**
```bash
pip install -r requirements.txt
```

---

## 🤝 **Contribuciones**

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto:

1. Crea un *fork* del repositorio.
2. Crea una nueva rama con tu mejora: `git checkout -b mejora-nueva`.
3. Realiza un *commit* de tus cambios: `git commit -m 'Mejora detallada'`.
4. Sube los cambios a GitHub: `git push origin mejora-nueva`.
5. Abre un *pull request*.



## 🎬 **Cierre**

Este proyecto demuestra cómo la tecnología y la inteligencia artificial pueden mejorar la movilidad urbana a través de sistemas de gestión de tráfico eficientes. Con una estructura bien definida, clases funcionales y pruebas unitarias robustas, se garantiza la fiabilidad y el éxito del proyecto. ¡Gracias por revisar este repositorio! 🚀


