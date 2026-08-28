# Proyecto_Scrum_Campuslands

### 7. Plan de Pruebas, Casos Ejecutados y Resultados

Se ejecutó un plan de pruebas funcionales para validar los criterios de aceptación:

| Caso de Prueba | Funcionalidad Evaluada

| Escenario / Entrada | Resultado Esperado        | Resultado Obtenido | Estado |
| ------------------- | ------------------------- | ------------------ | ------ |
| **CP-01**           | Registro de Equipo (HU01) |

| Datos válidos: Código `EQ-101`, Portátil, Dell, Latitude 3420

| Registro exitoso, estado "Disponible" y guardado en JSON.

| Registro exitoso en `equipos.json` con estado "Disponible".

| **PASÓ** |
| **CP-02** | Unicidad de Código (HU01) | Código existente: `EQ-101` | Alerta de duplicidad y cancelación del registro. | Advertencia mostrada; no se duplicó el registro. | **PASÓ** |
| **CP-03** | Registro Estudiante (HU03)

| Doc `1098765432`, Carlos Pérez, `cperez@edu.co`, Sistemas

| Estudiante registrado correctamente en JSON.

| Datos almacenados correctamente en `estudiantes.json`.

| **PASÓ** |
| **CP-04** | Registro de Préstamo (HU04)

| Estudiante `1098765432` + Equipo `EQ-101` (Disponible)

| Préstamo generado; equipo cambia a "Prestado".

| Préstamo registrado; equipo actualizado a "Prestado".

| **PASÓ** |
| **CP-05** | Validación de Disponibilidad (HU04)

| Intento de prestar `EQ-101` (Ya en estado "Prestado")

| Operación bloqueada informando no disponibilidad.

| Mensaje de advertencia; no se generó el préstamo duplicado. | **PASÓ** |
| **CP-06** | Registro de Devolución (HU05)

| Préstamo activo de `EQ-101`<br> | Préstamo finalizado con fecha; equipo vuelve a "Disponible".

| Devolución procesada; equipo en estado "Disponible".

| **PASÓ** |
| **CP-07** | Consulta Préstamos Activos (HU06)

| Consulta general con registros activos e inactivos

| Lista únicamente transacciones activas.

| Listado filtrado correcto en consola.

| **PASÓ** |
| **CP-08** | Historial Consolidado (HU07)

| Solicitud de historial completo

| Bitácora cronológica completa.

| Listado integral mostrado correctamente.

| **PASÓ** |

---
