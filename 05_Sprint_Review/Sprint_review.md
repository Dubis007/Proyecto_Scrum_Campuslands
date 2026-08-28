# ACTA DE SPRINT REVIEW — SPRINT 1

**Proyecto:** Sistema de Préstamo de Equipos Tecnológicos (MVP en Python)

---

## 1. Datos Generales de la Sesión

- **Fecha:** 27/08/2026
- **Hora de inicio / fin:** [9:30] a [9:40]
- **Duración:** 10 min
- **Modalidad:** Virtual
- **Carpeta de entrega:** `05_Sprint_Review/`

---

## 2. Asistentes y Roles

| Nombre Completo             | Rol                | Confirmación |
| :-------------------------- | :----------------- | :----------: |
| Juan David Esparza Castillo | Product Owner (PO) |     [x]      |
| Duban Camilo Bernal         | Scrum Master (SM)  |     [x]      |
| Karen Yaritza Escobar Pinto | Developer          |     [x]      |

---

## 3. Objetivo del Sprint (Sprint Goal)

> _"Construir y desplegar un MVP funcional por consola en Python que permita registrar equipos, registrar estudiantes y procesar préstamos con persistencia de datos en JSON, validado bajo ceremonias SCRUM."_

---

## 4. Incremento Demostrado

Durante la sesión, el equipo de desarrollo realizó la demostración en vivo por consola ejecutando los siguientes flujos:

- Registro de nuevo equipo tecnológico con validación de código único y estado inicial `Disponible`.
- Consulta de inventario listando disponibilidad y atributos de los equipos.
- Registro de estudiantes con validación de documento único y datos completos.
- Registro de préstamo asociando estudiante y equipo disponible, generando persistencia en JSON y cambiando el estado del equipo a `Prestado`.
- Prueba de caso negativo: bloqueo de préstamo al intentar seleccionar un equipo previamente ocupado.

---

## 5. Validación de Historias de Usuario

|    ID    | Historia de Usuario                          | Pts. | Criterio de Aceptación Clave                                      | Dictamen del PO |
| :------: | :------------------------------------------- | :--: | :---------------------------------------------------------------- | :-------------: |
| **HU01** | Registrar equipos tecnológicos en inventario |  3   | Código único, datos completos, persistencia en `equipos.json`.    |  **Aceptada**   |
| **HU02** | Consultar equipos y disponibilidad           |  2   | Listado en consola con formato y estado actual visible.           |  **Aceptada**   |
| **HU03** | Registrar estudiantes para préstamos         |  3   | Documento único, campos obligatorios, persistencia JSON.          |  **Aceptada**   |
| **HU04** | Registrar préstamo de equipo a estudiante    |  5   | Validación cruzada, persistencia y cambio de estado a `Prestado`. |  **Aceptada**   |

- **Total Story Points comprometidos:** 13 pts
- **Total Story Points aceptados:** 13 pts
- **Historias no aceptadas / devueltas al Backlog:** Ninguna

---

## 6. Observaciones y Feedback del Product Owner

- Se valida que el MVP cumple las reglas de negocio y restricciones técnicas solicitadas.
- La interfaz de consola responde adecuadamente y la persistencia en archivos JSON es consistente.
- Para el siguiente Sprint se priorizará la implementación de la **HU05 (Devolución de equipos)** y los módulos de consulta histórica (**HU06, HU07, HU08**).

---

## 7. Enlaces y Evidencias Adjuntas

- **Enlace a la grabación de la Review (5-10 min):** `[https://drive.google.com/drive/folders/1T6enUAYocAxd57YYJ2h4P_Pje6IjSEja?usp=sharing]`
- **Enlace al repositorio de código:** `[https://github.com/Dubis007/Proyecto_Scrum_Campuslands/tree/main/09_Codigo]`
- **Estado del Tablero Trello:** Tarjetas de HU01 a HU04 movidas a columna `Done`.
