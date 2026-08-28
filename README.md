# Sistema de Préstamo de Equipos Tecnológicos

MVP desarrollado en Python para gestionar el inventario de equipos tecnológicos, los estudiantes y el registro de préstamos de una institución educativa.

## Estado del proyecto

El Sprint 1 entregó y validó las historias HU01-HU04, equivalentes a 13 Story Points. El incremento permite registrar y consultar equipos, registrar y consultar estudiantes y crear préstamos validando la existencia del estudiante, la existencia del equipo y su disponibilidad.

Las historias HU05-HU08, relacionadas con devoluciones, consultas de préstamos y eliminación de equipos, permanecen pendientes para un Sprint posterior. El detalle del alcance y los criterios de aceptación está en [`01_Product_Backlog/Product_Backlog.md`](01_Product_Backlog/Product_Backlog.md).

## Requisitos

- Python 3.10 o una versión posterior.
- No se requieren paquetes externos.

## Ejecución

Desde la raíz del repositorio, ejecuta:

```bash
cd 09_Codigo
python main.py (o si tienes la extension para correr archivos python, haz click en el boton)
```

## Opciones disponibles

El menú principal permite:

1. Consultar todos los equipos.
2. Consultar únicamente los equipos disponibles.
3. Registrar un estudiante.
4. Mostrar los estudiantes registrados.
5. Registrar un equipo.
6. Registrar un préstamo.
7. Salir.

## Estructura del código

| Archivo o carpeta                                      | Responsabilidad                                    |
| :----------------------------------------------------- | :------------------------------------------------- |
| [`09_Codigo/main.py`](09_Codigo/main.py)               | Punto de entrada y menú principal.                 |
| [`09_Codigo/equipos.py`](09_Codigo/equipos.py)         | Registro, lectura y consulta del inventario.       |
| [`09_Codigo/estudiantes.py`](09_Codigo/estudiantes.py) | Registro, validación y consulta de estudiantes.    |
| [`09_Codigo/prestamos.py`](09_Codigo/prestamos.py)     | Validación y registro de préstamos.                |
| [`09_Codigo/datos/`](09_Codigo/datos/)                 | Archivos JSON de equipos, estudiantes y préstamos. |

Los archivos JSON se crean o actualizan durante la ejecución. En el estado inicial del repositorio están vacíos.

## Documentación del proyecto

El README contiene únicamente la información de acceso y ejecución. El detalle de cada artefacto se conserva en su carpeta correspondiente:

- [`01_Product_Backlog/`](01_Product_Backlog/): historias de usuario, prioridades, criterios de aceptación y Story Points.
- [`02_Sprint_Planning/`](02_Sprint_Planning/): Sprint Planning y Sprint Goal en PDF.
- [`03_Daily_Scrum/`](03_Daily_Scrum/): evidencia de las reuniones Daily Scrum.
- [`04_Impedimentos/Impedimentos.md`](04_Impedimentos/Impedimentos.md): impedimentos y acciones propuestas.
- [`05_Sprint_Review/Sprint_review.md`](05_Sprint_Review/Sprint_review.md): demostración y validación del incremento.
- [`06_Retrospectiva/Retrospectiva.md`](06_Retrospectiva/Retrospectiva.md): análisis y acciones de mejora.
- [`07_Pruebas/Pruebas.md`](07_Pruebas/Pruebas.md): casos de prueba y resultados.
- [`08_Informe_Final/Informe_final.md`](08_Informe_Final/Informe_final.md): resumen final y referencias del proyecto.
- [`10_Videos/`](10_Videos/): carpeta reservada para evidencias audiovisuales; los enlaces disponibles están en el informe final.

## Enlaces externos

- [Repositorio del proyecto](https://github.com/Dubis007/Proyecto_Scrum_Campuslands)
- [Tablero de Trello](https://trello.com/b/pJxnmiJQ/proyecto-scrum-backlog-campuslands)
- [Videos y demostración](https://drive.google.com/drive/u/1/folders/1c-dbEQzobV8-gM08pLgER85Y6HMWYCjn)

## Equipo Scrum

Los integrantes y sus roles están registrados en el [Product Backlog](01_Product_Backlog/Product_Backlog.md) y en las actas de [Sprint Review](05_Sprint_Review/Sprint_review.md) y [Retrospectiva](06_Retrospectiva/Retrospectiva.md).
