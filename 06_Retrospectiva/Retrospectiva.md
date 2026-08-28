# ACTA DE SPRINT RETROSPECTIVE — SPRINT 1

**Proyecto:** Sistema de Préstamo de Equipos Tecnológicos (MVP en Python)

---

## 1. Datos Generales de la Sesión

- **Fecha:** [28/08/2026]
- **Hora de inicio / fin:** [10:00] a [10:03]
- **Duración:** 3 Min
- **Modalidad:** Virtual
- **Carpeta de entrega:** `06_Retrospectiva/`

---

## 2. Asistentes y Roles

| Nombre Completo             | Rol                | Confirmación |
| :-------------------------- | :----------------- | :----------: |
| Juan David Esparza Castillo | Product Owner (PO) |     [x]      |
| Duban Camilo Bernal         | Scrum Master (SM)  |     [x]      |
| Karen Yaritza Escobar Pinto | Developer          |     [x]      |

---

## 3. Análisis Retrospectivo del Equipo

### 3.1 ¿Qué hicimos bien y debemos mantener?

- **Modularidad del código:** La separación en módulos independientes (`archivos.py`, `equipos.py`, `estudiantes.py`, `prestamos.py`) facilitó el trabajo paralelo sin conflictos en el repositorio.
- **Sincronización en las Daily Scrum:** Las sesiones diarias permitieron detectar bloqueos a tiempo y mantener el tablero Trello actualizado.
- **Criterios de aceptación claros:** La definición previa de reglas de validación en el Planning permitió que todas las historias seleccionadas fueran aprobadas en la Review sin reprocesos.

### 3.2 ¿Qué problemas tuvimos?

- Dificultades iniciales al estructurar los identificadores y el formato de datos dentro de `prestamos.json`.
- Falta de uniformidad en la gestion de ramas de git.
- Ejecución de pruebas manuales al final del ciclo en lugar de validaciones intermedias por cada función.

### 3.3 ¿Qué causó esos problemas?

- No se acordó el esquema JSON detallado antes de iniciar la programación de la lógica transaccional.
- Falta de un estándar de convención de ramas compartido desde el día uno.
- Priorización del avance en código funcional postergando la documentación de casos de prueba.

### 3.4 ¿Qué debemos cambiar en el próximo Sprint?

- Definir la estructura de datos y contratos entre módulos antes de escribir código.
- Integrar pruebas unitarias/manuales inmediatas conforme se finaliza cada función técnica.

---

## 4. Compromisos de Mejora Continua (3 Acciones Concretas)

|  N°   | Acción Concreta                                                                                                                                                                                              |         Responsable          | Mecanismo de Verificación                                                      |
| :---: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------: | :----------------------------------------------------------------------------- |
| **1** | **Definición previa de esquemas JSON:** Elaborar un archivo borrador con la estructura de datos requerida para devoluciones e historiales antes de iniciar el código de las historias restantes.             |          Developers          | Estructura JSON aprobada por el equipo en el Planning del Sprint 2.            |
| **2** | **Estándar de Conventional Commits:** Utilizar prefijos obligatorios en cada commit (`feat:`, `fix:`, `docs:`, `test:`) y trabajar mediante ramas `feature/` con revisión previa a la integración en `main`. |       SM / Developers        | Historial de commits en el repositorio remoto con nomenclatura uniforme.       |
| **3** | **Validación continua de casos de prueba:** Diligenciar la matriz de pruebas y ejecutar los escenarios positivos/negativos inmediatamente tras finalizar cada módulo, sin esperar al cierre del Sprint.      | Developer asignado a QA / PO | Matriz en `07_Pruebas/` actualizada a la par del avance de tarjetas en Trello. |

---

## 5. Cierre y Aprobación

El equipo en pleno aprueba las conclusiones registradas y se compromete a implementar las tres acciones de mejora acordadas a partir del inicio de la siguiente iteración.

- **Firma Scrum Master:** `[Duban Camilo Bernal]`
- **Firma Product Owner:** `[Juan David Esparza Castillo]`
