# Informe Final de Cumplimiento: Sistema de Préstamo de Equipos Tecnológicos (MVP)

## 1. Identificación y evidencias

- **Proyecto:** Sistema de Préstamo de Equipos Tecnológicos, MVP en Python.
- **Repositorio:** [Proyecto Scrum Campuslands](https://github.com/Dubis007/Proyecto_Scrum_Campuslands).
- **Tablero:** [Tablero del proyecto en Trello](https://trello.com/b/pJxnmiJQ/proyecto-scrum-backlog-campuslands).
- **Videos y demostración:** [Videos.md](../10_Videos/Videos.md), donde se encuentra el enlace a la carpeta de Google Drive.

Este informe resume el resultado del Sprint y remite a los documentos fuente para el detalle. No duplica la información que ya está registrada en las demás carpetas.

## 2. Equipo Scrum

Los integrantes, roles, responsabilidades y datos generales del proyecto están documentados en [`Product_Backlog.md`](../01_Product_Backlog/Product_Backlog.md) y en las actas de [`Sprint_review.md`](../05_Sprint_Review/Sprint_review.md) y [`Retrospectiva.md`](../06_Retrospectiva/Retrospectiva.md).

## 3. Propósito y resultado del Sprint

El MVP busca digitalizar mediante una aplicación de consola en Python el registro de equipos, estudiantes y préstamos, con persistencia en archivos JSON.

El Sprint 1 comprometió y aceptó HU01-HU04, por un total de **13 Story Points**. El alcance, las ocho historias, sus prioridades, criterios de aceptación y la planificación completa se encuentran en [`Product_Backlog.md`](../01_Product_Backlog/Product_Backlog.md) y [`Sprint_planning.pdf`](../02_Sprint_Planning/Sprint_planning.pdf).

La implementación aceptada cubre el registro y consulta de equipos, el registro y consulta de estudiantes y el registro de préstamos con validación de existencia y disponibilidad. HU05-HU08 quedaron pendientes para un Sprint posterior, según el backlog y el dictamen de la Review.

## 4. Ceremonias y evidencias Scrum

- [`Sprint_planning.pdf`](../02_Sprint_Planning/Sprint_planning.pdf): Sprint Goal, alcance y estimación.
- [`Daily_Scrum_1.pdf`](../03_Daily_Scrum/Daily_Scrum_1.pdf): evidencia documental de las reuniones Daily Scrum. Las grabaciones están en [`Videos.md`](../10_Videos/Videos.md).
- [`Sprint_review.md`](../05_Sprint_Review/Sprint_review.md): demostración, historias aceptadas, resultados y feedback del Product Owner.
- [`Retrospectiva.md`](../06_Retrospectiva/Retrospectiva.md): análisis del Sprint y tres acciones de mejora.
- [`Impedimentos.md`](../04_Impedimentos/Impedimentos.md): impedimento registrado y acción propuesta.

## 5. Implementación y pruebas

El detalle de la arquitectura, los módulos, las validaciones, las rutas de persistencia y las limitaciones actuales del código está en [`09_Codigo/`](../09_Codigo/). El plan, los escenarios y los resultados de las pruebas CP-01 a CP-05 están en [`Pruebas.md`](../07_Pruebas/Pruebas.md).

De acuerdo con el código revisado, el menú actual expone inventario, disponibilidad, estudiantes, registro de equipos y préstamos. No expone devolución, historial general ni eliminación de equipos. Tampoco existe un módulo independiente `archivos.py`; la persistencia JSON está implementada dentro de los módulos existentes.

Los archivos [`equipos.json`](../09_Codigo/datos/equipos.json), [`estudiantes.json`](../09_Codigo/datos/estudiantes.json) y [`prestamos.json`](../09_Codigo/datos/prestamos.json) existen, pero se encuentran vacíos en el estado revisado del repositorio.

## 6. Organización y observaciones del repositorio

La estructura completa de entregables se encuentra en la raíz del repositorio. El acceso a las evidencias audiovisuales está centralizado en [`10_Videos/Videos.md`](../10_Videos/Videos.md), que enlaza la carpeta de Google Drive donde se encuentran todos los videos.

El estado formal del Sprint se toma de la Sprint Review: HU01-HU04 fueron aceptadas y las tarjetas fueron registradas como `Done`. La columna general del backlog conserva el valor `Pendiente`, por lo que el acta de Review es la fuente utilizada para establecer el resultado final del Sprint.

## 7. Conclusión

El Sprint 1 entregó un MVP de consola funcional para inventario, estudiantes y registro de préstamos, con persistencia JSON y validaciones de unicidad y disponibilidad. El siguiente incremento debe abordar HU05-HU08 y acompañar su implementación con pruebas y evidencias actualizadas.
